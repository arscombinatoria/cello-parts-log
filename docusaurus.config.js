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
      onBrokenMarkdownLinks: 'warn',
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
          editUrl: 'https://github.com/arscombinatoria/cello-parts-log/edit/main/',
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
          label: 'パーツ',
          position: 'left',
          items: [
            {type: 'doc', docId: 'strings', label: '弦'},
            {type: 'doc', docId: 'strings-manufacturers', label: '弦メーカー'},
            {type: 'doc', docId: 'bridges', label: '駒'},
            {type: 'doc', docId: 'pegs', label: '糸巻き'},
            {type: 'doc', docId: 'fingerboards', label: '指板'},
            {type: 'doc', docId: 'endpins', label: 'エンドピン'},
            {type: 'doc', docId: 'tailpieces', label: 'テールピース'},
            {type: 'doc', docId: 'nuts', label: '上ナット'},
            {type: 'doc', docId: 'saddles', label: '下ナット'},
            {type: 'doc', docId: 'soundposts', label: '魂柱'},
            {type: 'doc', docId: 'tailguts', label: 'テールガット'},
          ],
        },
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
