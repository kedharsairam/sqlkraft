/**
 * Fix title capitalization issues in tsql-reference frontmatter.
 * Capitalizes the first letter of every title that starts with lowercase.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dir = path.resolve(__dirname, "../src/content/tsql-reference");

const files = fs.readdirSync(dir).filter(f => f.endsWith(".md"));
let fixed = 0;

for (const file of files) {
  const fp = path.join(dir, file);
  let content = fs.readFileSync(fp, "utf-8");
  const titleMatch = content.match(/^title: "([^"]+)"/m);
  if (titleMatch) {
    const title = titleMatch[1];
    if (title.length > 0 && title[0] === title[0].toLowerCase() && title[0] !== title[0].toUpperCase()) {
      const newTitle = title[0].toUpperCase() + title.slice(1);
      const oldLine = `title: "${title}"`;
      const newLine = `title: "${newTitle}"`;
      content = content.replace(oldLine, newLine);
      fs.writeFileSync(fp, content, "utf-8");
      console.log(`Fixed: ${file} → "${newTitle}"`);
      fixed++;
    }
  }
}

console.log(`\nFixed ${fixed} title capitalizations.`);
