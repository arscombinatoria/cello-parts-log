import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';
import remarkGfm from 'remark-gfm';

const contentDir = path.join(process.cwd(), 'content');

export async function getPage(slugArray) {
  const filePath = path.join(contentDir, ...slugArray, 'index.md');
  const fileContents = fs.readFileSync(filePath, 'utf8');
  const { data, content } = matter(fileContents);
  const processedContent = await remark().use(remarkGfm).use(html).process(content);
  return {
    title: data.title || slugArray[slugArray.length - 1],
    contentHtml: processedContent.toString(),
  };
}

export function getAllPageSlugs() {
  function walk(dir, slugs = []) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    let paths = [];
    for (const entry of entries) {
      if (entry.isDirectory()) {
        const newSlugs = [...slugs, entry.name];
        const subdir = path.join(dir, entry.name);
        if (fs.existsSync(path.join(subdir, 'index.md'))) {
          paths.push({ params: { slug: newSlugs } });
        }
        paths = paths.concat(walk(subdir, newSlugs));
      }
    }
    return paths;
  }
  return walk(contentDir);
}
