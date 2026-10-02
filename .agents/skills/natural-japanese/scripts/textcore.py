"""textcore.py — 検査層3スクリプト（lint.py / outline.py / terms.py）の共有基盤。

エントリポイントではない（単体実行を想定しない）ため PEP 723 インラインメタデータは
持たない。依存（sudachipy / sudachidict-core）は各エントリスクリプト側で宣言する。
`uv run .agents/skills/natural-japanese/scripts/lint.py` 等の実行時は sys.path[0] が scripts/ ディレクトリになるため、
同ディレクトリの `import textcore` がそのまま解決できる。

提供するもの:
    - sudachipy Tokenizer の遅延初期化（get_tokenizer）
    - 文分割（split_sentences_with_lines 等）
    - Markdown構造のマスク処理（mask_markdown_structure / mask_html_comments）
    - 行番号付き反復・段落分割ユーティリティ
    - 入力ファイルの読み込みと入力エラー処理（read_source_file）
    - 共有データ構造（Finding）
"""

from __future__ import annotations

import dataclasses
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# 共有データ構造
# ---------------------------------------------------------------------------

@dataclasses.dataclass
class Finding:
    line: int
    category: str
    excerpt: str
    severity: str  # "info" | "warn" | "critical"
    detail: str = ""
    # 文書全体集計型の検出器（antithesis_repetition, repeated_sentence_lead,
    # repeated_syntax_template, paragraph_lead_conjunction, nominal_ending 等）で、
    # 同じ集計に基づく他の該当行番号を列挙するための任意フィールド。
    # 単発検出（forbidden_phrase 等）では None のまま。
    related_lines: list[int] | None = None
    # --baseline 比較を行ったときだけ "new" | "persisting" にセットされる
    # （比較しない通常実行では None のまま。to_dict() で省く）。
    status: str | None = None

    def __post_init__(self) -> None:
        # JSON 出力でも detail 表記と同じく重複除去・昇順に正規化する
        if self.related_lines is not None:
            self.related_lines = sorted(set(self.related_lines))

    def to_dict(self) -> dict:
        d = dataclasses.asdict(self)
        # --baseline を使わない通常実行では status は常に None なので、
        # JSON 出力のフィールド構成を従来どおりに保つためキー自体を省く
        # （--baseline なしの挙動は完全に不変、という要件のため）。
        if d.get("status") is None:
            d.pop("status", None)
        return d


# ---------------------------------------------------------------------------
# sudachipy Tokenizer は生成コスト（辞書ロード）が高いので遅延・使い回し。
# ---------------------------------------------------------------------------
_tokenizer_obj = None


def get_tokenizer():
    global _tokenizer_obj
    if _tokenizer_obj is None:
        from sudachipy import Dictionary

        _tokenizer_obj = Dictionary().create()
    return _tokenizer_obj


# ---------------------------------------------------------------------------
# 体言止め判定（lint.py の nominal_ending 検出器と outline.py の見出し統計で共用）。
#
# TRAILING_SYMBOL_POS / NOUN_ENDING_POS / strip_trailing_symbols() は元々
# lint.py 側だけに定義されていたが、outline.py の見出し統計（体言止め率）でも
# 同じ判定ロジックが必要になったため、共有基盤である textcore.py に移設した。
# lint.py は本モジュールから import して使う（値は移設前と完全に同一）。
# ---------------------------------------------------------------------------
NOUN_ENDING_POS = {"名詞"}
TRAILING_SYMBOL_POS = {"補助記号", "空白"}


def strip_trailing_symbols(morphemes: list) -> list:
    """文末（または見出し末尾）の記号（」など）を除いた実質的な最終形態素列を返す。"""
    i = len(morphemes)
    while i > 0 and morphemes[i - 1].part_of_speech()[0] in TRAILING_SYMBOL_POS:
        i -= 1
    return morphemes[:i]


# ---------------------------------------------------------------------------
# テンプレ見出し語彙カタログ（outline.py の見出し統計「テンプレ見出し検出」で使用）。
#
# lint.py の BOILERPLATE_HEADING_WORDS（「まとめ」「おわりに」等、締めの定型句のみ）
# より対象を広げ、書き出し側の定型（「はじめに」「背景」）も含む。outline.py は
# severity 付きの検出器ではなく統計提示なので、ここでのヒットは「AI臭い」の
# 断定ではなく判断材料の一つに過ぎない。拡張前提のカタログとして、見出しの
# 前方一致で判定する（例:「まとめと今後の課題」は「まとめ」にも「今後」にも
# 一部一致しうるが、判定は startswith のみで十分。カタログはリスト順に評価し、
# 最初に一致した語を採用する）。
# ---------------------------------------------------------------------------
TEMPLATE_HEADING_WORDS: list[str] = [
    "はじめに",
    "背景",
    "概要",
    "本記事について",
    "この記事について",
    "まとめと今後",
    "今後の展望",
    "今後の課題",
    "今後について",
    "まとめ",
    "おわりに",
    "終わりに",
    "さいごに",
    "最後に",
    "結論",
    "総括",
    "conclusion",
    "introduction",
    "summary",
]


# ---------------------------------------------------------------------------
# Markdown構造行のマスク処理
# 見出し・リスト項目・コードブロック内・引用ブロックは「文章」ではないため、
# 体言止め判定や翻訳調検出などの対象から外す。行を削除すると後続行の行番号が
# ズレてレポートの L<n> が狂うので、該当行は「内容を空文字に置き換える」ことで
# 行番号を保ったまま解析対象外にする（マスク方式）。
# ---------------------------------------------------------------------------
_HEADING_RE = re.compile(r"^\s*#{1,6}(\s|$)")
_LIST_ITEM_RE = re.compile(r"^\s*([-*+]|\d+[.)])(\s|$)")
_BLOCKQUOTE_RE = re.compile(r"^\s*>")
# フェンス行の検出。開始/終了の判定では「同じ文字種（`` ` `` か `~`）かつ
# 長さが開始フェンス以上」であることを別途チェックする（``` と ~~~ の混同や、
# フェンス内に出てくる別種・より短いフェンス様の行での誤クローズを防ぐため）。
_CODE_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
# YAML フロントマター（ファイル先頭の `---` ... `---`）。先頭行が単独の `---` の
# ときだけフロントマターとみなし、次の単独 `---` までをまとめてマスクする。
_FRONT_MATTER_DELIM_RE = re.compile(r"^---\s*$")
# 行内のインラインコードスパン。同じ長さのバッククォート列で囲まれた範囲を
# 認識し、内容に含まれる別の長さのバッククォート列は終端とみなさない。
# 文解析前に該当部分だけ同じ文字数の空白に置換する（行番号・オフセットを保つため）。
_INLINE_CODE_SPAN_RE = re.compile(
    r"(?<!`)(`+)(?!`)(?:(?!\n(?:[ \t]*\n|[ \t]*(?:`{3,}|~{3,}|#{1,6}[ \t])))[\s\S])*?(?<!`)\1(?!`)"
)
# インデントコードブロック（4スペース以上のインデント）はマスク対象に含めない。
# 通常の文中でも字下げされた引用・リストの続きなど紛らわしいケースが多く、
# 誤マスクのリスクの方が高いと判断して見送る（要検討事項として明示しておく）。
# Markdown 内のリンク・画像 `[text](url)` / `![alt](url)` の url 部分。
# alt/text 側は自然文の一部として残し、URL のみ空白化する。
_AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:)[^>\n]*>")


def _markdown_link_end(text: str, start: int) -> int | None:
    """リンク先の括弧・エスケープ・山括弧と任意のタイトルを読む。"""
    if not text.startswith("](", start):
        return None

    def whitespace(pos: int) -> int:
        while pos < len(text) and text[pos].isspace():
            pos += 1
        return pos

    pos = whitespace(start + 2)
    if pos >= len(text):
        return None
    if text[pos] == "<":
        pos += 1
        while pos < len(text) and text[pos] not in ">\n":
            pos += 2 if text[pos] == "\\" and pos + 1 < len(text) else 1
        if pos >= len(text) or text[pos] != ">":
            return None
        pos += 1
    else:
        depth = 0
        while pos < len(text) and not text[pos].isspace():
            char = text[pos]
            if char == "\\" and pos + 1 < len(text) and text[pos + 1] != "\n":
                pos += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            pos += 1
        if depth:
            return None
    destination_end = pos
    pos = whitespace(pos)
    if pos < len(text) and text[pos] != ")":
        if pos == destination_end or text[pos] not in "\"'(":
            return None
        closing = ")" if text[pos] == "(" else text[pos]
        pos += 1
        while pos < len(text) and text[pos] != closing:
            pos += 2 if text[pos] == "\\" and pos + 1 < len(text) else 1
        if pos >= len(text):
            return None
        pos = whitespace(pos + 1)
    if pos >= len(text) or text[pos] != ")":
        return None
    # リンク構文は空行を越えない。単一改行で分かれたタイトルは許容する。
    if re.search(r"\n[ \t]*\n", text[start:pos + 1]):
        return None
    return pos + 1


def _table_cells(line: str) -> list[str] | None:
    """エスケープされていないパイプで分割し、任意の外側パイプを除く。"""
    cells = []
    start = 0
    pos = 0
    while pos < len(line):
        if line[pos] == "\\" and pos + 1 < len(line):
            pos += 2
            continue
        if line[pos] == "|":
            cells.append(line[start:pos].strip())
            start = pos + 1
        pos += 1
    if not cells:
        return None
    cells.append(line[start:].strip())
    if not cells[0]:
        cells.pop(0)
    if cells and not cells[-1]:
        cells.pop()
    return cells


def mask_gfm_tables(text: str) -> str:
    """ヘッダーと同じ列数の区切り行から表ブロックを認識し、オフセットを保つ。

    呼び出し元でコード・コメント・フロントマターを先に除外する。
    パイプだけを含む通常の文は表として扱わない。
    """
    lines = text.split("\n")
    def interrupts(line: str) -> bool:
        return not line.strip() or bool(
            _HEADING_RE.match(line) or _LIST_ITEM_RE.match(line)
            or _BLOCKQUOTE_RE.match(line) or _CODE_FENCE_RE.match(line)
            or re.fullmatch(r"[ \t]*(?:[-*_][ \t]*){3,}", line)
        )
    i = 0
    while i + 1 < len(lines):
        header = _table_cells(lines[i])
        delimiter = _table_cells(lines[i + 1])
        if (interrupts(lines[i]) or not header or not delimiter
                or len(header) != len(delimiter)
                or not all(re.fullmatch(r":?-+:?", cell) for cell in delimiter)):
            i += 1
            continue
        end = i + 2
        while end < len(lines) and not interrupts(lines[end]):
            end += 1
        for row in range(i, end):
            lines[row] = " " * len(lines[row])
        i = end
    return "\n".join(lines)


def _blank_preserving_offsets(text: str) -> str:
    return "".join("\n" if char == "\n" else " " for char in text)


def mask_html_comments(
    text: str, *, mask_fenced_code: bool = False, mask_inline_code: bool = False
) -> str:
    """コメント・フロントマターを、改行と文字オフセットを保って空白化する。

    共通の読み取り順序はメタデータ、フェンス、行内コード・URL、コメント。
    コードとURLのコメント記号はリテラルとして扱い、実際のコメント内では
    Markdown記法を解釈しない。行内コードは同じ長さのバッククォートで閉じる
    範囲を認識し、空行・新しいブロックを越えない改行も扱う。
    コード自体の空白化は各フラグで指定する。
    """
    out: list[str] = []
    pos = 0
    in_front_matter = False
    open_fence: tuple[str, int] | None = None
    while pos < len(text):
        if pos == 0 or text[pos - 1] == "\n":
            end = text.find("\n", pos)
            end = len(text) if end == -1 else end + 1
            line = text[pos:end]
            if pos == 0 and _FRONT_MATTER_DELIM_RE.match(line):
                in_front_matter = True
                out.append(_blank_preserving_offsets(line))
                pos = end
                continue
            if in_front_matter:
                if _FRONT_MATTER_DELIM_RE.match(line):
                    in_front_matter = False
                out.append(_blank_preserving_offsets(line))
                pos = end
                continue
            fence = _CODE_FENCE_RE.match(line)
            was_in_fence = open_fence is not None
            if fence:
                run = fence.group(1)
                if open_fence is None:
                    open_fence = (run[0], len(run))
                elif (run[0] == open_fence[0] and len(run) >= open_fence[1]
                      and not line[fence.end():].strip()):
                    open_fence = None
            if was_in_fence or open_fence is not None:
                out.append(_blank_preserving_offsets(line) if mask_fenced_code else line)
                pos = end
                continue

        # エスケープされた記号もHTMLコメントの開始として解釈しない。
        if text[pos] == "\\" and pos + 1 < len(text) and text[pos + 1] in r"\`*_{}[]()#+-.!<>~":
            out.append(text[pos:pos + 2])
            pos += 2
            continue
        code = _INLINE_CODE_SPAN_RE.match(text, pos)
        if code:
            out.append(_blank_preserving_offsets(code.group()) if mask_inline_code else code.group())
            pos = code.end()
            continue
        link_end = _markdown_link_end(text, pos)
        if link_end is not None:
            out.append("](" + _blank_preserving_offsets(text[pos + 2:link_end - 1]) + ")"
                       if mask_inline_code else text[pos:link_end])
            pos = link_end
            continue
        autolink = _AUTOLINK_RE.match(text, pos)
        if autolink:
            out.append(_blank_preserving_offsets(autolink.group()) if mask_inline_code else autolink.group())
            pos = autolink.end()
            continue
        if text.startswith("<!--", pos):
            end = text.find("-->", pos + 4)
            end = len(text) if end == -1 else end + 3
            out.append(_blank_preserving_offsets(text[pos:end]))
            pos = end
            continue
        out.append(text[pos])
        pos += 1
    return "".join(out)


def mask_markdown_structure(
    text: str, *, preserve_offsets: bool = False, include_headings: bool = False
) -> str:
    """検査対象外の構造をマスクし、行数を保つ。

    preserve_offsets=True は除外行も同じ長さの空白にし、文字オフセットも保つ。
    include_headings=True は見出しの本文を含める（用語抽出用）。
    """
    text = mask_gfm_tables(mask_html_comments(text, mask_fenced_code=True))
    text = mask_html_comments(text, mask_inline_code=True)
    masked_lines = []
    for line in text.split("\n"):
        heading = _HEADING_RE.match(line)
        if heading and include_headings:
            masked_lines.append(" " * heading.end() + line[heading.end():])
        elif heading or _LIST_ITEM_RE.match(line) or _BLOCKQUOTE_RE.match(line):
            masked_lines.append(" " * len(line) if preserve_offsets else "")
        else:
            masked_lines.append(line)
    return "\n".join(masked_lines)


def iter_lines_with_no(text: str) -> list[tuple[int, str]]:
    """1-indexed 行番号付きで行を返す。"""
    return list(enumerate(text.splitlines(), start=1))


def find_line_no(lines: list[tuple[int, str]], needle: str, start_hint: int = 0) -> int:
    """needle を含む行番号を探す。

    start_hint（探索を始めたい行番号、例: 対象段落の開始行）以降を優先的に走査する。
    同一内容の段落が文書中に複数回登場する場合、常に先頭から検索すると
    最初に出現した行に誤帰属してしまうため、start_hint 以降の一致を優先し、
    見つからない場合のみ文書全体（start_hint より前）にフォールバックする。
    """
    for no, line in lines:
        if no >= start_hint and needle in line:
            return no
    for no, line in lines:
        if needle in line:
            return no
    return start_hint or 1


def iter_paragraphs_with_lines(
    lines: list[tuple[int, str]],
) -> list[list[tuple[int, str]]]:
    """行番号付きの行リストを、空行区切りの段落（行のグループ）に分ける。

    段落の開始行が呼び出し側に正確に分かるため、re.split(r"\\n\\s*\\n", text) と
    テキスト検索（find_line_no）による近似の line_cursor 計算に頼らずに済む。
    同一内容の段落が複数回登場しても、行番号を直接持っているので誤帰属しない。
    """
    paragraphs: list[list[tuple[int, str]]] = []
    current: list[tuple[int, str]] = []
    for no, line in lines:
        if line.strip():
            current.append((no, line))
        else:
            if current:
                paragraphs.append(current)
                current = []
    if current:
        paragraphs.append(current)
    return paragraphs


# ---------------------------------------------------------------------------
# 文分割
# ---------------------------------------------------------------------------
SENTENCE_SPLIT_RE = re.compile(r"[。！？\n]")


def split_sentences_with_lines(
    lines: list[tuple[int, str]], raw_lines_by_no: dict[int, str] | None = None
) -> list[tuple[int, str, str]]:
    """行番号付きで文を分割する（。！？で分割、行内に複数文があれば同じ行番号を割り当てる）。

    マスク済みテキスト（見出し・表マスクやインラインコードスパンの空白置換済み）と
    原文（raw_lines_by_no）を同じオフセットで同時に切り出し、
    (行番号, マスク済み文, 原文の文) の3要素タプルを返す。
    マスク処理は「行の全置換（同じ長さの空文字ではなく行そのものを""にする）」か
    「インラインコードスパンを同じ文字数の空白に置換」のいずれかで、
    どちらも文字位置を保つため、マスク済みテキストで見つけた区切り位置をそのまま
    原文の同じオフセットに適用できる。
    見出し・表・コードブロックなどマスクで丸ごと空文字になった行は、マスク済み側が
    空になり文が生成されないため、原文にレポートに出したくない構造行の内容が
    紛れ込むことはない。
    """
    sentences = []
    for no, line in lines:
        raw_line = raw_lines_by_no.get(no, line) if raw_lines_by_no else line
        bounds = []
        prev = 0
        for m in SENTENCE_SPLIT_RE.finditer(line):
            bounds.append((prev, m.start()))
            prev = m.end()
        bounds.append((prev, len(line)))
        for s, e in bounds:
            piece = line[s:e]
            if piece.strip():
                raw_piece = raw_line[s:e] if len(raw_line) >= e else piece
                sentences.append((no, piece.strip(), raw_piece.strip()))
    return sentences


# ---------------------------------------------------------------------------
# 見出し行パーサ（outline.py / terms.py で共用）
# ---------------------------------------------------------------------------


def _heading_level_and_text(line: str) -> tuple[int, str]:
    """見出し行から (レベル, 見出しテキスト) を取り出す。

    ATX見出しの closing sequence（末尾の `#` 列）は、CommonMark と同様に
    「直前に空白がある場合のみ」除去する。空白なしで見出しテキストに直接続く
    `#`（例: 「# C#」「# F#入門」）は closing sequence ではなくテキストの一部
    なので、除去してはいけない（`(?:\\s+#+)?` で closing sequence の手前に
    最低1文字の空白を要求することで区別する）。
    """
    m = re.match(r"^\s*(#{1,6})\s*(.*?)(?:\s+#+)?\s*$", line)
    if not m:
        return 0, line.strip()
    return len(m.group(1)), m.group(2).strip()


# ---------------------------------------------------------------------------
# ファイル読み込みと入力エラー処理
#
# 「文章の中身に関する判断」と「そもそも実行できない入力エラー」は区別する
# （lint.py/outline.py/terms.py 共通の方針）。前者は exit 0（判断は人間/AIに委ねる）、
# 後者（ファイル不在・ディレクトリ指定・読み取り不可・非UTF-8等）は exit 1。
# 3つのエントリスクリプトがまったく同じエラーメッセージ・判定順序で読み込めるよう、
# ここに一本化する。
# ---------------------------------------------------------------------------


def read_source_file(path: Path) -> tuple[str | None, str | None]:
    """path を UTF-8 テキストとして読み込む。

    成功時は (text, None)、失敗時は (None, error_message) を返す。
    呼び出し側は error_message を stderr に出力し、exit code 1 で終了する
    （このモジュールは exit しない。呼び出し側の CLI が判断する）。
    """
    if not path.exists():
        return None, f"エラー: ファイルが見つかりません: {path}"
    if path.is_dir():
        return None, f"エラー: ディレクトリが指定されました（ファイルを指定してください）: {path}"
    try:
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeDecodeError) as exc:
        return None, f"エラー: ファイルを読み込めません: {path} ({exc})"
