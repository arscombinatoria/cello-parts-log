/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',               // out/ に静的書き出し
  basePath: '/cello-parts-log',   // プロジェクトサイト用
  assetPrefix: '/cello-parts-log/', // _next 等のアセット参照
  images: { unoptimized: true },  // 画像最適化APIは export 非対応
  trailingSlash: true
};
export default nextConfig;
