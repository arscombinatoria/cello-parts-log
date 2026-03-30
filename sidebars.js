/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  homeSidebar: ['intro'],
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
            'strings/strings-manufacturer-daddario',
            'strings/strings-manufacturer-jargar',
            'strings/strings-manufacturer-larsen',
            'strings/strings-manufacturer-pirastro',
            'strings/strings-manufacturer-savarez-corelli',
            'strings/strings-manufacturer-thomastik-infeld',
            'strings/strings-manufacturer-warchal',
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
