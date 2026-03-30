# Cello Parts Log

チェロの各パーツ（弦・駒・ペグ・指板・エンドピンなど）の交換や調整に関する情報を整理するための Docusaurus ベースのドキュメントサイトです。主観的な所感と客観的な仕様を分けて記録し、後から検証・更新しやすい形を目指しています。

## サイト構成

- `/docs` 配下に各パーツのメモを配置しています。トップは `docs/intro.md` で、サイドバーから各カテゴリに移動できます。
- 各カテゴリは `docs/<category>/` ディレクトリで管理し、カテゴリトップは
  `docs/<category>/index.md` に統一します（例: `docs/bridges/index.md`,
  `docs/pegs/index.md`）。
- カテゴリ配下の詳細ページは、同じカテゴリディレクトリ内に配置します（例: `docs/bridges/bridges-material-trends.md`）。

## 必要な環境

- Node.js LTS（22 〜 24 系を想定）
- npm

## 開発用コマンド

- `npm ci` — 依存関係のインストール
- `npm start` — 開発サーバーを起動（`http://localhost:3000`）
- `npm run build` — 本番ビルドを生成（`build/`）
- `npm run serve` — ビルド済みサイトをローカルで確認
- `npm run lint` — ESLint による静的解析
- `npm run typecheck` — TypeScript の型チェック
- `npm test` — `npm run typecheck` を実行

Node.js は CI で 22 / 24 系の matrix で動作確認しています。Pages デプロイは Node.js 24 系で実行しています。

## GitHub Pages へのデプロイ

- `deploy-pages.yml` により、`main` ブランチへの push で自動ビルドと Pages デプロイが行われます。
- Pages の公開 URL: `https://arscombinatoria.github.io/cello-parts-log/`

## コントリビュート方法

1. Issue で提案やバグ報告を共有してください。
2. 作業ブランチで変更し、`npm run lint`, `npm test`, `npm run build` を通したうえで PR を作成します。
3. 1 PR 1 トピックを基本とし、変更内容の背景や安全面への配慮があれば概要を併記してください。

## 参考

- [Docusaurus](https://docusaurus.io/)
