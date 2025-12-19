/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'intro',
    {
      type: 'category',
      label: '弦',
      link: { type: 'doc', id: 'strings' },
      items: ['strings-manufacturers'],
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
  ],
};

module.exports = sidebars;
