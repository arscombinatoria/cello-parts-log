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

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
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
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Docs',
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
