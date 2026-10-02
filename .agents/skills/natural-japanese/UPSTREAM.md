# 取り込み元と更新方法

このディレクトリは [coji/natural-japanese](https://github.com/coji/natural-japanese) の `skills/natural-japanese/` をコピーしたものです。ローカル・クラウドのどちらでも、リポジトリ内のファイルを参照して利用します。スキルの配置に Node.js や npx は不要です。

- 取り込み元コミット: `9a78a42964096da509b8f3e011f0085a5f080151`
- ソース: https://github.com/coji/natural-japanese/tree/9a78a42964096da509b8f3e011f0085a5f080151/skills/natural-japanese
- ライセンス: MIT（上流の著作権表示を含む `LICENSE` を同梱）
- 上流ファイルへの変更: `SKILL.md`、スクリプトとfixture内の実行例をリポジトリルートから使えるパスに統一。`scripts/calibrate.py` のコーパス基準ディレクトリをリポジトリルートに修正し、最低有効文書長の推定は人間3件以上・AI1件以上のビンに限定。
- `scripts/textcore.py` はメタデータ・コード・URL・HTMLコメントを共通の処理で区別。インラインコードの改行にも対応し、コメント記号のリテラルで後続の本文が消える問題を修正。`scripts/outline.py` と `scripts/terms.py` もこの処理を使用。
- 用語抽出は、見出しを含み、除外箇所の文字オフセットを保持するテキストから行う。回数と初出文脈にも同じテキストを使い、コード・URL・メタデータ内の用語を集計しない。
- GFM表はヘッダーと区切り行の列数からブロックを認識し、外側のパイプがない行も共通処理で除外。リンク先は括弧の対応、エスケープ、山括弧、タイトルを読み取り、URL途中のコメント記号で後続本文が消えないようにする。
- 追加ファイル: `LICENSE`、本ファイル、`scripts/test_vendored.py`（配置とコメント処理の回帰テスト）。

更新時は上流の変更を確認し、上記のローカル修正と回帰テストを保持しながら、`skills/natural-japanese/` の変更・削除を反映します。上流で同じ問題が修正されていれば、該当するローカル修正の記録を更新します。上流ルートの `LICENSE` と、この文書のコミット情報も更新してください。

回帰テストはリポジトリルートから `uv run .agents/skills/natural-japanese/scripts/test_vendored.py` で実行できます。用語抽出も実行するため、検査スクリプトと同じ形態素解析の依存関係を使用します。

検査スクリプトには `uv` が必要です。依存関係は各スクリプトに記載されており、初回実行時に取得されます。実行できない環境では `references/manual-checklist.md` を使います。

校正スクリプトが生成するリポジトリルートの `corpus/reports/` はGitの除外対象です。入力となるコーパスのファイルはこの除外対象に含めません。
