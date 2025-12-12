# Cello Parts Log

チェロの各パーツ（弦・駒・ペグ・指板・エンドピンなど）の交換や調整に関する情報を整理するための Docusaurus ベースのドキュメントサイトです。主観的な所感と客観的な仕様を分けて記録し、後から検証・更新しやすい形を目指しています。

## サイト構成
- `/docs` 配下に各パーツのメモを配置しています。トップは `docs/intro.md` で、サイドバーから各カテゴリに移動できます。
- 既存の Jekyll 版は `legacy-jekyll/` に退避してあり、必要に応じて参照できます（公開は Docusaurus のみ）。

## 必要な環境
- Node.js LTS（20 〜 22 系を想定）
- npm

## 開発用コマンド
- `npm ci` — 依存関係のインストール
- `npm start` — 開発サーバーを起動（`http://localhost:3000`）
- `npm run build` — 本番ビルドを生成（`build/`）
- `npm run serve` — ビルド済みサイトをローカルで確認
- `npm run lint` — ESLint による静的解析
- `npm test` — 現状はプレースホルダー（失敗しません）

## GitHub Pages へのデプロイ
- `deploy-pages.yml` により、`main` ブランチへの push で自動ビルドと Pages デプロイが行われます。
- Pages の公開 URL: `https://arscombinatoria.github.io/cello-parts-log/`

## コントリビュート方法
1. Issue で提案やバグ報告を共有してください。
2. 作業ブランチで変更し、`npm run lint`, `npm test`, `npm run build` を通したうえで PR を作成します。
3. 1 PR 1 トピックを基本とし、変更内容の背景や安全面への配慮があれば概要を併記してください。

## 参考
- Docusaurus: https://docusaurus.io/
