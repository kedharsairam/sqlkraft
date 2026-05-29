import fs from 'fs';
import yaml from 'js-yaml';

// Check specific problem file
const paths = [
  'src/content/catalog-views/sys-all-columns.md',
];

for (const p of paths) {
  try {
    const raw = fs.readFileSync(p, 'utf8');
    const match = raw.match(/---\r?\n([\s\S]*?)\r?\n---/);
    if (match) {
      const result = yaml.load(match[1]);
      console.log(p, '-> OK:', result.name, result.category);
    } else {
      console.log(p, '-> no frontmatter');
    }
  } catch(e) {
    console.log(p, '-> ERROR:', e.message);
  }
}

// Scan all catalog-views for bad YAML
console.log('\nScanning all catalog-view files...');
const dir = 'src/content/catalog-views';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.md'));
let errors = 0;
for (const f of files) {
  try {
    const raw = fs.readFileSync(dir + '/' + f, 'utf8');
    const match = raw.match(/---\r?\n([\s\S]*?)\r?\n---/);
    if (match) {
      yaml.load(match[1]);
    } else {
      console.log('  NO FM:', f);
    }
  } catch(e) {
    console.log('  FAIL:', f, '->', e.message.split('\n')[0]);
    errors++;
  }
}
console.log(`\n${files.length} files, ${errors} errors`);
