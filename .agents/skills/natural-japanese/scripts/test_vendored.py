"""配置先のパスとMarkdownコメント処理の回帰テスト（標準ライブラリのみ）。"""

import unittest
from pathlib import Path

import calibrate
from textcore import mask_markdown_structure


class VendoredLayoutTests(unittest.TestCase):
    def test_corpus_and_reports_belong_to_repository_root(self):
        root = Path(__file__).resolve().parents[4]
        self.assertTrue((root / "AGENTS.md").is_file())
        self.assertEqual(calibrate.CORPUS_DIR, root / "corpus")
        self.assertEqual(calibrate.REPORTS_DIR, root / "corpus" / "reports")


class MarkdownCommentTests(unittest.TestCase):
    def test_unpaired_fences_inside_comments_preserve_following_prose(self):
        for fence in ("```", "~~~", "```python", "~~~~"):
            with self.subTest(fence=fence):
                source = f"<!--\n{fence}\nレビュー用メモ\n-->\n本文を検査する。\n"
                masked = mask_markdown_structure(source)
                self.assertEqual(masked.split("\n")[4], "本文を検査する。")
                self.assertNotIn("レビュー用メモ", masked)
                self.assertEqual(len(masked.split("\n")), len(source.split("\n")))

    def test_comment_closure_preserves_prose_on_same_line(self):
        source = "<!--\n```\n-->本文を検査する。\n"
        masked = mask_markdown_structure(source)
        self.assertEqual(masked.split("\n")[2], "   本文を検査する。")

    def test_comment_openers_inside_code_do_not_hide_following_prose(self):
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                source = f"{fence}\n<!--\n{fence}\n本文を検査する。\n"
                masked = mask_markdown_structure(source)
                self.assertEqual(masked.split("\n")[3], "本文を検査する。")
                self.assertNotIn("<!--", masked)

    def test_real_fence_after_comment_still_masks_code(self):
        source = "<!--\n~~~\n-->\n```python\nコードを隠す。\n```\n本文を検査する。\n"
        masked = mask_markdown_structure(source)
        self.assertNotIn("コードを隠す。", masked)
        self.assertIn("本文を検査する。", masked)


if __name__ == "__main__":
    unittest.main()
