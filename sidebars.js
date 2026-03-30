/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  homeSidebar: ['intro'],
  stringsSidebar: [
    {
      type: 'category',
      label: '弦',
      link: {type: 'doc', id: 'strings'},
      items: [
        'strings-materials',
        {
          type: 'category',
          label: 'メーカー横断比較表',
          link: {type: 'doc', id: 'strings-manufacturers'},
          items: [
            'strings-manufacturer-daddario',
            'strings-manufacturer-jargar',
            'strings-manufacturer-larsen',
            'strings-manufacturer-pirastro',
            'strings-manufacturer-savarez-corelli',
            'strings-manufacturer-thomastik-infeld',
            'strings-manufacturer-warchal',
          ],
        },
        'strings-selection-guide',
      ],
    },
  ],
  bridgesSidebar: ['bridges'],
  pegsSidebar: ['pegs'],
  fingerboardsSidebar: ['fingerboards'],
  endpinsSidebar: ['endpins'],
  tailpiecesSidebar: ['tailpieces'],
  nutsSidebar: ['nuts'],
  saddlesSidebar: ['saddles'],
  soundpostsSidebar: ['soundposts'],
  tailgutsSidebar: ['tailguts'],
  bowsSidebar: ['bows'],
  rosinSidebar: ['rosin'],
  casesSidebar: ['cases'],
};

module.exports = sidebars;
