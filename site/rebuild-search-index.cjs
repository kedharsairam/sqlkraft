/**
 * rebuild-search-index.cjs
 * Scans ALL content directories and builds a complete search-index.json.
 * Handles variable frontmatter schemas per collection.
 * 
 * Usage: node rebuild-search-index.cjs
 */

const fs = require("fs");
const path = require("path");

const CONTENT_DIR = path.join(__dirname, "src", "content");
const OUTPUT_PATH = path.join(__dirname, "src", "data", "search-index.json");

// Collection-specific frontmatter field mappings
const COLLECTION_SCHEMAS = {
  "dmvs":            { nameField: "name",  catField: "category" },
  "catalog-views":   { nameField: "name",  catField: "category" },
  "functions":       { nameField: "name",  catField: "category" },
  "stored-procedures": { nameField: "name", catField: "category" },
  "errors":          { nameField: "name",  catField: "category" },
  "tsql-reference":  { nameField: "name",  catField: "category" },
  "wait-statistics": { nameField: "name",  catField: "category" },
  "architecture":    { nameField: "title", catField: "topic" },
  "scripts":         { nameField: "title", catField: "category" },
  "operations":      { nameField: "title", catField: "topic" },
};

function parseFrontmatter(content) {
  const fm = {};
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return fm;
  
  const lines = match[1].split("\n");
  for (const line of lines) {
    const kv = line.match(/^(\w+):\s+(.+)$/);
    if (!kv) continue;
    let key = kv[1];
    let value = kv[2].trim();
    
    // Handle quoted strings
    if (value.startsWith("'") && value.endsWith("'")) {
      value = value.slice(1, -1).replace("''", "'");
    } else if (value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    }
    // Handle lists
    else if (value.startsWith("[") && value.endsWith("]")) {
      try { value = JSON.parse(value); } catch(e) { value = []; }
    }
    // Handle booleans
    else if (value === "true") { value = true; }
    else if (value === "false") { value = false; }
    // Handle numbers
    else if (/^\d+$/.test(value)) { value = parseInt(value, 10); }
    
    fm[key] = value;
  }
  return fm;
}

function main() {
  console.log("[rebuild-search-index] Scanning content directories...");
  
  const records = [];
  let totalFiles = 0;
  let skippedFiles = 0;
  const seen = new Set();
  
  const dirs = fs.readdirSync(CONTENT_DIR, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);
  
  for (const collection of dirs) {
    const collectionDir = path.join(CONTENT_DIR, collection);
    const schema = COLLECTION_SCHEMAS[collection] || { nameField: "name", catField: "category" };
    
    const files = fs.readdirSync(collectionDir).filter(f => f.endsWith(".md"));
    
    for (const file of files) {
      totalFiles++;
      const slug = file.replace(/\.md$/, "");
      if (seen.has(slug)) {
        skippedFiles++;
        continue;
      }
      seen.add(slug);
      
      const content = fs.readFileSync(path.join(collectionDir, file), "utf-8");
      const fm = parseFrontmatter(content);
      
      const nameField = schema.nameField;
      const catField = schema.catField;
      
      const name = fm[nameField] || slug;
      const title = fm.title || (typeof name === "string" ? name : slug);
      const category = fm[catField] || "general";
      const tags = Array.isArray(fm.tags) ? fm.tags : [];
      const description = (fm.description || "").toString().slice(0, 150);
      
      records.push({
        slug,
        name: typeof name === "string" ? name : slug,
        title: typeof title === "string" ? title : slug,
        category: typeof category === "string" ? category : "general",
        tags,
        description,
        collection,
      });
    }
  }
  
  // Sort by collection then slug
  records.sort((a, b) => {
    if (a.collection !== b.collection) return a.collection.localeCompare(b.collection);
    return a.name.localeCompare(b.name);
  });
  
  // Write output
  const outputDir = path.dirname(OUTPUT_PATH);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(records, null, 2), "utf-8");
  
  console.log(`[rebuild-search-index] Complete!`);
  console.log(`  Directories scanned: ${dirs.length}`);
  console.log(`  Total files found:   ${totalFiles}`);
  console.log(`  Duplicates skipped:  ${skippedFiles}`);
  console.log(`  Index records:       ${records.length}`);
  
  // Per-collection breakdown
  const byCollection = {};
  for (const r of records) {
    byCollection[r.collection] = (byCollection[r.collection] || 0) + 1;
  }
  for (const [coll, count] of Object.entries(byCollection).sort()) {
    console.log(`    ${coll}: ${count}`);
  }
}

main();
