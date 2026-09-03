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

test('site profile identifies Max', async () => {
  const source = await readFile(new URL('../data.js', import.meta.url), 'utf8');
  assert.match(source, /name: 'Max\.Ma'/);
});

test('page contains planned section anchors and dynamic content containers', async () => {
  const page = await readFile(new URL('../index.html', import.meta.url), 'utf8').catch(() => '');
  for (const id of ['about', 'achievements', 'projects', 'skills', 'contact']) {
    assert.match(page, new RegExp(`id="${id}"`));
  }
  for (const id of ['achievements-list', 'projects-list', 'skills-list']) {
    assert.match(page, new RegExp(`id="${id}"`));
  }
  assert.match(page, /Max\.Ma/);
});

test('stylesheet defines the portfolio theme and mobile layout', async () => {
  const css = await readFile(new URL('../styles.css', import.meta.url), 'utf8').catch(() => '');
  for (const token of ['--ink:', '--paper:', '--accent:']) assert.match(css, new RegExp(token));
  assert.match(css, /@media \(max-width: 680px\)/);
  assert.match(css, /prefers-reduced-motion/);
});

test('deployment workflow uploads and deploys the portfolio root', async () => {
  const workflow = await readFile(new URL('../.github/workflows/deploy-pages.yml', import.meta.url), 'utf8').catch(() => '');
  assert.match(workflow, /actions\/upload-pages-artifact@v4/);
  assert.match(workflow, /path: '\.'/);
  assert.match(workflow, /actions\/deploy-pages@v4/);
});

test('documentation states the profile repository GitHub Pages address', async () => {
  const readme = await readFile(new URL('../README.md', import.meta.url), 'utf8');
  assert.match(readme, /https:\/\/maxma615\.github\.io\/maxma615\//);
});

test('profile README introduces Max and links featured work', async () => {
  const readme = await readFile(new URL('../README.md', import.meta.url), 'utf8');
  for (const text of ['Max.Ma', 'Intelligent Science and Technology', 'racing_vision_ai', 'rdk_LeRobot_tools', 'skills']) {
    assert.match(readme, new RegExp(text));
  }
});
