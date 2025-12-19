const fs = require('fs');
const path = require('path');

const sidebars = require('../sidebars');

const docsDir = path.join(__dirname, '..', 'docs');

function ensureDocPath(id) {
  const candidates = ['.md', '.mdx'].map((ext) => path.join(docsDir, `${id}${ext}`));
  const existing = candidates.find((candidate) => fs.existsSync(candidate));
  if (!existing) {
    throw new Error(`Document not found for id: ${id}`);
  }
  return existing;
}

function collectDocs(items, order, visited = new Set()) {
  for (const item of items) {
    if (typeof item === 'string') {
      if (!visited.has(item)) {
        order.push(item);
        visited.add(item);
      }
      continue;
    }

    if (item.type === 'doc' && item.id) {
      if (!visited.has(item.id)) {
        order.push(item.id);
        visited.add(item.id);
      }
      continue;
    }

    if (item.type === 'category' && Array.isArray(item.items)) {
      if (item.link?.type === 'doc' && item.link.id && !visited.has(item.link.id)) {
        order.push(item.link.id);
        visited.add(item.link.id);
      }
      collectDocs(item.items, order, visited);
    }
  }

  return { order, visited };
}

function listAllDocs(dir, accumulator = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      listAllDocs(fullPath, accumulator);
      continue;
    }

    if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();
      if (ext === '.md' || ext === '.mdx') {
        const relativePath = path.relative(docsDir, fullPath);
        const docId = relativePath.slice(0, -ext.length).split(path.sep).join('/');
        accumulator.push(docId);
      }
    }
  }

  return accumulator;
}

function buildTree(items, prefix = '') {
  return items.flatMap((item, index) => {
    const isLast = index === items.length - 1;
    const connector = isLast ? '└─ ' : '├─ ';
    const childPrefix = prefix + (isLast ? '   ' : '│  ');

    if (typeof item === 'string') {
      return `${prefix}${connector}${item}`;
    }

    if (item.type === 'doc' && item.id) {
      return `${prefix}${connector}${item.id}`;
    }

    if (item.type === 'category') {
      const headline = `${prefix}${connector}${item.label}`;
      const nestedItems = [];
      if (item.link?.type === 'doc' && item.link.id) {
        nestedItems.push({ type: 'doc', id: item.link.id });
      }
      if (Array.isArray(item.items)) {
        nestedItems.push(...item.items);
      }
      const children = buildTree(nestedItems, childPrefix);
      return [headline, ...children];
    }

    return `${prefix}${connector}${item.id ?? 'unknown'}`;
  });
}

function printSidebarTree() {
  const sidebarItems = sidebars.docsSidebar ?? [];
  const lines = buildTree(sidebarItems);
  console.log('=== Sidebar tree ===');
  console.log(lines.join('\n'));
}

function printDocsContent() {
  const sidebarItems = sidebars.docsSidebar ?? [];
  const { order: sidebarDocs, visited } = collectDocs(sidebarItems, []);
  const allDocs = listAllDocs(docsDir).sort();
  const missingDocs = allDocs.filter((id) => !visited.has(id));
  const docOrder = [...sidebarDocs, ...missingDocs];

  console.log('\n=== Docs content ===');
  for (const id of docOrder) {
    const docPath = ensureDocPath(id);
    const content = fs.readFileSync(docPath, 'utf8');
    console.log(`\n--- ${id} (${path.relative(process.cwd(), docPath)}) ---`);
    console.log(content);
  }
}

printSidebarTree();
printDocsContent();
