# /// script
# requires-python = ">=3.10"
# dependencies = ["sudachipy>=0.6.8", "sudachidict-core>=20240409"]
# ///
"""配置先のパスと、各検査経路のMarkdownコメント処理の回帰テスト。"""

import unittest
import contextlib
import io
import json
import tempfile
from types import SimpleNamespace
from unittest.mock import patch
from pathlib import Path

import calibrate
from outline import build_outline
from terms import build_term_inventory
from lint import run_lint
from semantic import doc_sentences_with_lines
from textcore import Finding
from textcore import mask_html_comments, mask_markdown_structure


class VendoredLayoutTests(unittest.TestCase):
    def test_corpus_and_reports_belong_to_repository_root(self):
        root = Path(__file__).resolve().parents[4]
        self.assertTrue((root / "AGENTS.md").is_file())
        self.assertEqual(calibrate.CORPUS_DIR, root / "corpus")
        self.assertEqual(calibrate.REPORTS_DIR, root / "corpus" / "reports")


class MarkdownCommentTests(unittest.TestCase):
    def test_inline_comment_literals_preserve_following_text(self):
        for ticks in ('`', '``', '```'):
            with self.subTest(ticks=ticks):
                source = f"HTMLコメントは {ticks}<!--{ticks} で始めます。\n本文を検査する。\n"
                self.assertEqual(mask_html_comments(source), source)
                self.assertIn('本文を検査する。', mask_markdown_structure(source))

    def test_real_comments_after_inline_code_are_still_masked(self):
        source = "記号は `<!--`。<!--非表示-->本文。\n後続。\n"
        self.assertEqual(mask_html_comments(source), "記号は `<!--`。          本文。\n後続。\n")

    def test_backticks_inside_real_comment_do_not_hide_comment_closure(self):
        source = "<!-- ` -->本文。`\n後続。\n"
        self.assertEqual(mask_html_comments(source), "          本文。`\n後続。\n")

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
    def test_literal_comment_openers_across_all_inspection_paths(self):
        cases = {
            'metadata': "---\ntitle: 'API <!-- syntax'\nexample: '```'\n---\n",
            'inline': "HTMLコメントは `<!--` で始めます。\n",
            'nested_backticks': "HTMLコメントは `` `<!--` `` で始めます。\n",
            'multiline_inline': "HTMLコメントは `<!--\n説明` で始めます。\n",
            'fence': "```html\n<!--\n```\n",
            'link_url': "[説明](https://example.com/<!--)\n",
            'balanced_link': "[説明](https://example.com/foo_(bar)/<!--)\n",
            'nested_link': "[説明](https://example.com/a_(b_(c))/<!--)\n",
            'escaped_link': r"[説明](https://example.com/a_\(b\)/<!--)" + '\n',
            'angle_link': '[説明](<https://example.com/a_(b)/<!--> "補足 (例)")\n',
            'multiline_link_title': '[説明](https://example.com/a_(b)/<!--\n "補足 (例)")\n',
            'image_link': '![説明](https://example.com/a_(b)/<!-- "補足 )")\n',
            'autolink': "<https://example.com/<!-->\n",
            'escaped': r"HTMLコメント記号は \<!-- です。" + '\n',
        }
        for name, prefix in cases.items():
            with self.subTest(case=name):
                source = prefix + '\n# APIの説明\n\n重要なのは、APIで情報を取得することです。\n'
                line = len(source.splitlines())
                self.assertTrue(any(item['text'] == 'APIの説明' for item in build_outline(source)))
                api = next(item for item in build_term_inventory(source) if item['term'] == 'API')
                self.assertEqual(api['count'], 2)
                findings, _ = run_lint(source)
                self.assertTrue(any(item.line == line for item in findings))
                self.assertTrue(any(no == line for no, _ in doc_sentences_with_lines(source)))
                self.assertEqual(len(mask_html_comments(source)), len(source))

    def test_real_unclosed_comments_still_mask_through_eof(self):
        source = '実際のコメント<!--\n# SQL\nAPIで情報を取得します。\n'
        self.assertNotIn('SQL', str(build_outline(source)))
        self.assertNotIn('API', [item['term'] for item in build_term_inventory(source)])
        self.assertNotIn('API', mask_markdown_structure(source))

    def test_gfm_table_blocks_are_excluded_by_every_caller(self):
        for header, delimiter, row in (
            ('Name | Value', '--- | ---', 'API | 重要なのは、説明です。'),
            ('| Name | Value |', '| :--- | ---: |', '| API | 重要なのは、説明です。 |'),
            (r'Name\|Alias | Value', ':---: | ---', r'API\|SQL | 重要なのは、説明です。'),
        ):
            with self.subTest(header=header):
                source = f'{header}\n{delimiter}\n{row}\n\n# 本文\n\n重要なのは、本文を読むことです。\n'
                self.assertEqual([x['line'] for x in build_outline(source)], [5, 7])
                self.assertNotIn('API', [x['term'] for x in build_term_inventory(source)])
                findings, _ = run_lint(source)
                self.assertFalse(any(x.line <= 3 for x in findings))
                self.assertTrue(any(x.line == 7 for x in findings))
                self.assertEqual([no for no, _ in doc_sentences_with_lines(source)], [7])
                masked = mask_markdown_structure(source, preserve_offsets=True)
                self.assertEqual(len(masked), len(source))

    def test_pipe_in_prose_without_table_delimiter_is_retained(self):
        source = 'API | SQLを比較します。\n\n後続の本文です。\n'
        self.assertIn('API', mask_markdown_structure(source))
        self.assertIn('API', str(build_outline(source)))
        self.assertIn('API', [x['term'] for x in build_term_inventory(source)])

    def test_table_requires_matching_header_and_delimiter_columns(self):
        source = 'API | SQL\n--- | --- | ---\n本文です。\n'
        self.assertIn('API', mask_markdown_structure(source))
        self.assertIn('API', str(build_outline(source)))

    def test_balanced_link_mask_keeps_label_offsets_and_real_comments(self):
        source = '[API](https://example.com/a_(b)/SQL/<!--) <!--非表示-->本文です。\n'
        masked = mask_markdown_structure(source, preserve_offsets=True)
        self.assertEqual(len(masked), len(source))
        self.assertIn('[API]', masked)
        self.assertIn('本文です。', masked)
        self.assertNotIn('SQL', masked)
        self.assertNotIn('非表示', masked)
        terms = build_term_inventory(source)
        self.assertEqual(next(x for x in terms if x['term'] == 'API')['count'], 1)
        self.assertNotIn('SQL', [x['term'] for x in terms])

    def test_term_count_and_context_exclude_code_and_urls(self):
        source = '`API` [説明](https://example.com/API)' + ' ' * 100 + 'API（定義）を使います。\n'
        api = next(item for item in build_term_inventory(source) if item['term'] == 'API')
        self.assertEqual(api['count'], 1)
        self.assertTrue(api['has_gloss_hint'])
        self.assertIn('定義', api['context'])
        self.assertNotIn('example.com', api['context'])
        self.assertNotIn('`', api['context'])

    def test_heading_terms_and_body_share_masked_counting_buffer(self):
        source = '# API `SQL` [説明](https://example.com/API)\n\nAPIを使います。\n'
        inventory = build_term_inventory(source)
        api = next(item for item in inventory if item['term'] == 'API')
        self.assertEqual(api['count'], 2)
        self.assertEqual(api['first_line'], 1)
        self.assertNotIn('SQL', [item['term'] for item in inventory])
        masked = mask_markdown_structure(source, preserve_offsets=True, include_headings=True)
        self.assertEqual(len(masked), len(source))

    def test_all_callers_retain_prose_after_inline_comment_opener(self):
        for ticks in ('`', '``', '```'):
            with self.subTest(ticks=ticks):
                source = f"HTMLコメントは {ticks}<!--{ticks} で始めます。\n\n# APIの説明\n\n重要なのは、APIで情報を取得することです。\n"
                self.assertTrue(any(item['line'] == 3 and item['text'] == 'APIの説明'
                                    for item in build_outline(source)))
                self.assertTrue(any(item['term'] == 'API' for item in build_term_inventory(source)))
                findings, _ = run_lint(source)
                self.assertTrue(any(item.line == 5 for item in findings))

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


class CalibrationSampleFloorTests(unittest.TestCase):
    def estimate(self, human_lengths, ai_lengths):
        category = calibrate.STATISTICAL_CATEGORIES[0]
        groups = {
            'human_aozora': [calibrate.CorpusDoc('human_aozora', Path('human.md'), '文' * n)
                            for n in human_lengths],
            'human_web': [],
            'ai': [calibrate.CorpusDoc('ai', Path('ai.md'), '文' * n) for n in ai_lengths],
        }
        def prepared(mod, doc):
            findings = [Finding(1, category, '例', 'warn')] if doc.corpus_type == 'ai' else []
            return SimpleNamespace(doc=doc, findings=findings)
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(calibrate, 'load_corpus', return_value=groups), \
             patch.object(calibrate, 'prepare_doc', side_effect=prepared), \
             patch.object(calibrate, 'run_full_lint'), \
             patch.object(calibrate, 'REPORTS_DIR', Path(directory)), \
             contextlib.redirect_stdout(io.StringIO()):
            calibrate.cmd_length_analysis(None)
            result = json.loads((Path(directory) / 'length_analysis.json').read_text())
            return result['min_effective_length_bin'][category]

    def test_sample_floor_boundaries(self):
        for human, ai in ((0, 1), (1, 1), (2, 1), (3, 0), (3, 1)):
            with self.subTest(human=human, ai=ai):
                expected = calibrate.LENGTH_BINS[0][0] if human >= 3 and ai >= 1 else None
                self.assertEqual(self.estimate([100] * human, [100] * ai), expected)

    def test_sparse_short_bin_does_not_override_supported_longer_bin(self):
        self.assertEqual(self.estimate([100, 1500, 1500, 1500], [100, 1500]),
                         calibrate.LENGTH_BINS[1][0])


if __name__ == "__main__":
    unittest.main()
