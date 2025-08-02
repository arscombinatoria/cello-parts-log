import { test } from 'node:test';
import assert from 'node:assert/strict';
import { getAllPageSlugs, getPage } from './content.js';

test('getAllPageSlugs includes bridges', () => {
  const slugs = getAllPageSlugs().map((p) => p.params.slug.join('/'));
  assert(slugs.includes('bridges'));
});

test('getPage returns bridges content', async () => {
  const page = await getPage(['bridges']);
  assert.equal(page.title, 'bridges');
  assert.ok(page.contentHtml.includes('チェロ駒'));
});
