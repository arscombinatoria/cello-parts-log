# 取り込み元と更新方法

このディレクトリは [coji/natural-japanese](https://github.com/coji/natural-japanese) の `skills/natural-japanese/` をコピーしたものです。ローカル・クラウドのどちらでも、リポジトリ内のファイルを参照して利用します。スキルの配置に Node.js や npx は不要です。

- 取り込み元コミット: `9a78a42964096da509b8f3e011f0085a5f080151`
- ソース: https://github.com/coji/natural-japanese/tree/9a78a42964096da509b8f3e011f0085a5f080151/skills/natural-japanese
- ライセンス: MIT（上流の著作権表示を含む `LICENSE` を同梱）
- 上流ファイルへの変更: `SKILL.md` の読解負荷チェックのパスを配置先に合わせ、`scripts/calibrate.py` のコーパス基準ディレクトリをリポジトリルートに修正。`scripts/textcore.py` はHTMLコメント内のフェンスで本文が検査対象から外れないよう修正。
- 追加ファイル: `LICENSE`、本ファイル、`scripts/test_vendored.py`（配置とコメント処理の回帰テスト）。

更新時は上流の変更を確認し、上記のローカル修正と回帰テストを保持しながら、`skills/natural-japanese/` の変更・削除を反映します。上流で同じ問題が修正されていれば、該当するローカル修正の記録を更新します。上流ルートの `LICENSE` と、この文書のコミット情報も更新してください。

回帰テストはリポジトリルートから `python -m unittest discover -s .agents/skills/natural-japanese/scripts -p 'test_*.py'` で実行できます。テストには外部依存関係は不要です。

検査スクリプトには `uv` が必要です。依存関係は各スクリプトに記載されており、初回実行時に取得されます。実行できない環境では `references/manual-checklist.md` を使います。
