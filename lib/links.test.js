import { test } from 'node:test';
import assert from 'node:assert/strict';
import { getAllPageSlugs, getPage } from './content.js';

// Verify that all links found in page content resolve to a valid target.
test('all page links are alive', async () => {
  const pages = getAllPageSlugs();
  for (const { params: { slug } } of pages) {
    const page = await getPage(slug);
    const linkRegex = /<a\s+[^>]*href="([^"]+)"/g;
    let match;
    while ((match = linkRegex.exec(page.contentHtml)) !== null) {
      const href = match[1];
      if (href.startsWith('http://') || href.startsWith('https://')) {
        const res = await fetch(href);
        assert.ok(res.ok, `External link ${href} on page ${slug.join('/')} returned ${res.status}`);
      } else if (href.startsWith('/')) {
        const targetSlug = href.split('/').filter(Boolean);
        try {
          await getPage(targetSlug);
        } catch {
          assert.fail(`Internal link ${href} on page ${slug.join('/')} not found`);
        }
      }
    }
  }
});
