/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  homeSidebar: ['index'],
  stringsSidebar: [
    {
      type: 'category',
      label: '弦',
      link: {type: 'doc', id: 'strings/strings'},
      items: [
        'strings/strings-materials',
        {
          type: 'category',
          label: 'メーカー横断比較表',
          link: {type: 'doc', id: 'strings/strings-manufacturers'},
          items: [
            'strings/manufacturers/strings-manufacturer-daddario',
            'strings/manufacturers/strings-manufacturer-jargar',
            'strings/manufacturers/strings-manufacturer-larsen',
            'strings/manufacturers/strings-manufacturer-pirastro',
            'strings/manufacturers/strings-manufacturer-savarez-corelli',
            'strings/manufacturers/strings-manufacturer-thomastik-infeld',
            'strings/manufacturers/strings-manufacturer-warchal',
          ],
        },
        'strings/strings-selection-guide',
      ],
    },
  ],
  bridgesSidebar: [
    {
      type: 'category',
      label: '駒',
      link: {type: 'doc', id: 'bridges/bridges'},
      items: ['bridges/bridges-material-trends', 'bridges/bridges-blank-manufacturers'],
    },
  ],
  pegsSidebar: [
    {
      type: 'category',
      label: 'ペグ',
      link: {type: 'doc', id: 'pegs/pegs'},
      items: ['pegs/pegs-materials', 'pegs/pegs-friction-vs-geared'],
    },
  ],
  fingerboardsSidebar: [
    {
      type: 'category',
      label: '指板',
      link: {type: 'doc', id: 'fingerboards/fingerboards'},
      items: ['fingerboards/fingerboards-materials'],
    },
  ],
  endpinsSidebar: [
    {
      type: 'category',
      label: 'エンドピン',
      link: {type: 'doc', id: 'endpins/endpins'},
      items: ['endpins/endpins-materials'],
    },
  ],
  tailpiecesSidebar: [
    {
      type: 'category',
      label: 'テールピース',
      link: {type: 'doc', id: 'tailpieces/tailpieces'},
      items: ['tailpieces/tailpieces-materials', 'tailpieces/tailpieces-mass-adjustment', 'tailpieces/tailpieces-adjusters'],
    },
  ],
  nutsSidebar: [
    {
      type: 'category',
      label: 'ナット',
      link: {type: 'doc', id: 'nuts/nuts'},
      items: ['nuts/nuts-material-trends'],
    },
  ],
  saddlesSidebar: [
    {
      type: 'category',
      label: 'サドル',
      link: {type: 'doc', id: 'saddles/saddles'},
      items: ['saddles/saddles-material-trends'],
    },
  ],
  soundpostsSidebar: [
    {
      type: 'category',
      label: '魂柱',
      link: {type: 'doc', id: 'soundposts/soundposts'},
      items: ['soundposts/soundposts-materials'],
    },
  ],
  tailgutsSidebar: [
    {
      type: 'category',
      label: 'テールコード',
      link: {type: 'doc', id: 'tailguts/tailguts'},
      items: ['tailguts/tailguts-materials'],
    },
  ],
  bowsSidebar: ['bows/bows'],
  rosinSidebar: ['rosin/rosin'],
  casesSidebar: ['cases/cases'],
};

module.exports = sidebars;
