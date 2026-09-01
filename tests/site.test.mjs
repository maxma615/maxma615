import test from 'node:test';
import assert from 'node:assert/strict';
import { access, readFile } from 'node:fs/promises';

test('editable portfolio content source exists', async () => {
  await assert.doesNotReject(access(new URL('../data.js', import.meta.url)));
});

test('content source defines the required showcase groups', async () => {
  const source = await readFile(new URL('../data.js', import.meta.url), 'utf8').catch(() => '');
  for (const field of ['profile', 'achievements', 'projects', 'skills']) {
    assert.match(source, new RegExp(`${field}:`));
  }
});
