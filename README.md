# Cello Parts Log

チェロの各パーツ（弦・駒・ペグ・指板・エンドピンなど）の交換や調整に関する情報を整理するドキュメントサイトです。Docusaurus で構築しています。所感と客観的な仕様を分け、後から検証・更新しやすい形で記録することを目指しています。

## サイト構成

- `/docs` 配下に各パーツのメモを配置しています。トップページは `docs/index.md` で、サイドバーから各カテゴリに移動できます。
- 各カテゴリは `docs/<category>/` ディレクトリで管理し、カテゴリのトップページは
  `docs/<category>/index.md` に統一しています（例: `docs/bridges/index.md`,
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

CI では Node.js 22 系と 24 系で動作を確認しています。GitHub Pages へのデプロイには Node.js 24 系を使っています。

## GitHub Pages へのデプロイ

- `main` ブランチに push すると、`deploy-pages.yml` がサイトを自動でビルドし、GitHub Pages にデプロイします。
- Pages の公開 URL: `https://arscombinatoria.github.io/cello-parts-log/`

## 変更の提案方法

1. Issue で提案やバグ報告を共有してください。
2. 作業ブランチで変更を加え、`npm run lint`、`npm test`、`npm run build` が成功することを確認してから PR を作成してください。
3. 1 つの PR では 1 つのテーマを扱ってください。変更の背景や安全面で配慮した点があれば、PR の説明に概要を記載してください。

## 参考

- [Docusaurus](https://docusaurus.io/)
