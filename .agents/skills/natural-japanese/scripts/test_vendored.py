# /// script
# requires-python = ">=3.10"
# dependencies = ["sudachipy>=0.6.8", "sudachidict-core>=20240409"]
# ///
"""配置先のパスと、各検査経路のMarkdownコメント処理の回帰テスト。"""

import unittest
from pathlib import Path

import calibrate
from outline import build_outline
from terms import build_term_inventory
from textcore import mask_html_comments, mask_markdown_structure


class VendoredLayoutTests(unittest.TestCase):
    def test_corpus_and_reports_belong_to_repository_root(self):
        root = Path(__file__).resolve().parents[4]
        self.assertTrue((root / "AGENTS.md").is_file())
        self.assertEqual(calibrate.CORPUS_DIR, root / "corpus")
        self.assertEqual(calibrate.REPORTS_DIR, root / "corpus" / "reports")


class MarkdownCommentTests(unittest.TestCase):
    def test_comment_masker_preserves_offsets_and_code_examples(self):
        source = "```html\n<!--\n```\n<!--非表示-->本文。\n"
        masked = mask_html_comments(source)
        self.assertEqual(masked, "```html\n<!--\n```\n          本文。\n")
        self.assertEqual(len(masked), len(source))

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


class CallerRegressionTests(unittest.TestCase):
    def test_outline_retains_headings_and_prose_after_html_code_example(self):
        for fence in ("```", "~~~", "````"):
            with self.subTest(fence=fence):
                source = f"{fence}html\n<!--\n# 非表示\n{fence}\n\n# APIの説明\n\nAPIで情報を取得します。\n"
                self.assertEqual(build_outline(source), [
                    {"line": 6, "kind": "heading", "level": 1, "text": "APIの説明"},
                    {"line": 8, "kind": "lead", "level": None, "text": "APIで情報を取得します。"},
                ])

    def test_terms_retains_prose_and_excludes_terms_in_code(self):
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                source = f"{fence}html\n<!--\n# SQL\n{fence}\n\nAPIで情報を取得します。\n"
                inventory = build_term_inventory(source)
                api = next(item for item in inventory if item['term'] == 'API')
                self.assertEqual(api['first_line'], 6)
                self.assertEqual(api['count'], 1)
                self.assertNotIn('SQL', [item['term'] for item in inventory])

    def test_fences_inside_real_comments_are_ignored_by_both_callers(self):
        source = "<!--\n```\n# SQL\n-->\n# APIの説明\n\nAPIで情報を取得します。\n"
        self.assertEqual([item['text'] for item in build_outline(source)],
                         ['APIの説明', 'APIで情報を取得します。'])
        inventory = build_term_inventory(source)
        self.assertIn('API', [item['term'] for item in inventory])
        self.assertNotIn('SQL', [item['term'] for item in inventory])


if __name__ == "__main__":
    unittest.main()
