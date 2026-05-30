/**
 * Preview enrichment output for sample files.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");

import("./enrich-undersized.mjs").then(() => {
  // Can't easily import the functions since they're not exported
  // Let's just check if the enrichment templates work correctly
  const testFiles = ["print.md", "uniqueidentifier.md", "assemblyproperty.md", "stlinefromtext-geography-data-type.md"];
  
  // Actually, let me just read the dry-run results by applying and then reverting
  // Or simpler: just show the original content of a few files
  for (const file of testFiles) {
    console.log("=".repeat(60));
    console.log("FILE: " + file);
    console.log("=".repeat(60));
    const content = fs.readFileSync(path.join(contentDir, file), "utf-8");
    const lines = content.split("\n");
    console.log("Total lines: " + lines.length);
    console.log("Body lines: " + lines.filter(l => !l.startsWith("---") && !l.startsWith("name:") && !l.startsWith("title:") && !l.startsWith("category:") && !l.startsWith("description:") && !l.startsWith("tags:") && !l.startsWith("pubDate:")).length);
    console.log("Last 5 lines:");
    lines.slice(-5).forEach(l => console.log("  " + JSON.stringify(l)));
  }
}).catch(e => console.error("Error:", e));
