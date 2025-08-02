/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  basePath: '/cello-parts-log',
  assetPrefix: '/cello-parts-log/',
  images: { unoptimized: true },
  trailingSlash: true
};
export default nextConfig;
