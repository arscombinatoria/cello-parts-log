/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'intro',
    {
      type: 'category',
      label: '弦',
      link: { type: 'doc', id: 'strings' },
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
    'bridges',
    'pegs',
    'fingerboards',
    'endpins',
    'tailpieces',
    'nuts',
    'saddles',
    'soundposts',
    'tailguts',
    'bows',
    'rosin',
    'cases',
  ],
};

module.exports = sidebars;
