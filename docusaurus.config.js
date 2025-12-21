// @ts-check

const {themes} = require('prism-react-renderer');

const config = {
  title: 'Cello Parts Log',
  tagline: 'チェロのパーツ交換と調整の記録',
  favicon: 'img/favicon.ico',

  url: 'https://arscombinatoria.github.io',
  baseUrl: '/cello-parts-log/',
  organizationName: 'arscombinatoria',
  projectName: 'cello-parts-log',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  future: {
    experimental_faster: {
      rspackBundler: true,
    },
  },

  i18n: {
    defaultLocale: 'ja',
    locales: ['ja'],
  },

  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        docsRouteBasePath: '/',
        language: ['ja'],
        highlightSearchTermsOnTargetPage: true,
      },
    ],
  ],

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: false,
        },
        blog: false,
        pages: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Cello Parts Log',
      logo: {
        alt: 'Cello Parts Log ロゴ',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'ホーム',
        },
        {
          type: 'doc',
          docId: 'strings',
          position: 'left',
          label: '弦',
        },
        {type: 'doc', docId: 'bridges', position: 'left', label: '駒'},
        {type: 'doc', docId: 'pegs', position: 'left', label: 'ペグ'},
        {type: 'doc', docId: 'fingerboards', position: 'left', label: '指板'},
        {type: 'doc', docId: 'endpins', position: 'left', label: 'エンドピン'},
        {type: 'doc', docId: 'tailpieces', position: 'left', label: 'テールピース'},
        {type: 'doc', docId: 'nuts', position: 'left', label: 'ナット'},
        {type: 'doc', docId: 'saddles', position: 'left', label: 'サドル'},
        {type: 'doc', docId: 'soundposts', position: 'left', label: '魂柱'},
        {type: 'doc', docId: 'tailguts', position: 'left', label: 'テールコード'},
        {
          href: 'https://github.com/arscombinatoria/cello-parts-log',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'リソース',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/arscombinatoria/cello-parts-log',
            },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Cello Parts Log`,
    },
    prism: {
      theme: themes.github,
      darkTheme: themes.dracula,
    },
  },
};

module.exports = config;
