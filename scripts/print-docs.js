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

  return order;
}

function listAllDocs(dir, basePath = '') {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const docs = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      const nestedBase = path.join(basePath, entry.name);
      docs.push(...listAllDocs(fullPath, nestedBase));
      continue;
    }

    if (entry.isFile()) {
      const ext = path.extname(entry.name);
      if (ext === '.md' || ext === '.mdx') {
        const id = path.join(basePath, path.basename(entry.name, ext));
        docs.push({ id, path: fullPath });
      }
    }
  }

  return docs;
}

function printDoc(id, docPath) {
  const content = fs.readFileSync(docPath, 'utf8');
  console.log(`\n--- ${id} (${path.relative(process.cwd(), docPath)}) ---`);
  console.log(content);
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
  const docOrder = collectDocs(sidebarItems, []);
  const allDocs = listAllDocs(docsDir);
  const printedDocs = new Set();

  console.log('\n=== Docs content ===');
  for (const id of docOrder) {
    const docPath = ensureDocPath(id);
    printDoc(id, docPath);
    printedDocs.add(id);
  }

  const remainingDocs = allDocs
    .filter(({ id }) => !printedDocs.has(id))
    .sort((a, b) => a.id.localeCompare(b.id));

  for (const { id, path: docPath } of remainingDocs) {
    printDoc(id, docPath);
  }
}

printSidebarTree();
printDocsContent();
