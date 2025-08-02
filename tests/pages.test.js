import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { getAllPageSlugs } from '../lib/content.js';

const port = 3000;
let server;

before(async () => {
  server = spawn('npx', ['next', 'dev', '-p', String(port)], {
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  await new Promise((resolve, reject) => {
    function onData(data) {
      if (data.toString().toLowerCase().includes('ready')) {
        server.stdout.off('data', onData);
        server.stderr.off('data', onData);
        resolve();
      }
    }
    server.stdout.on('data', onData);
    server.stderr.on('data', onData);
    server.on('error', reject);
  });
});

after(() => {
  server.kill();
});

test('index page returns 200', async () => {
  const res = await fetch(`http://localhost:${port}/`);
  assert.equal(res.status, 200);
});

test('all content pages return 200', async () => {
  const paths = getAllPageSlugs();
  for (const { params } of paths) {
    const route = params.slug.join('/');
    const res = await fetch(`http://localhost:${port}/${route}`);
    assert.equal(res.status, 200, `expected 200 for /${route}`);
  }
});
