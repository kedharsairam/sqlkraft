// Generates a compact palette-index.json from the full search-index.json
// for the Spotlight-style command palette. Uses single-char field names
// to minimize transfer size.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dataDir = path.resolve(__dirname, "../src/data");

const raw = fs.readFileSync(path.join(dataDir, "search-index.json"), "utf-8");
const fullIndex = JSON.parse(raw);

const paletteIndex = fullIndex.map((item) => {
  // Fix URL slug for errors collection: the [id].astro route prepends
  // `error-` to entry.data.name, so filenames like "severity-10.md"
  // produce URLs like /errors/error-severity-10/.
  var slug = item.slug;
  if (item.collection === "errors" && !slug.startsWith("error-")) {
    slug = "error-" + slug;
  }
  return {
    t: (item.title || item.name || "").slice(0, 100),
    u: `/${item.collection}/${slug}/`,
    c: item.collection,
    d: (item.description || "").slice(0, 120),
  };
});

const outPath = path.join(dataDir, "palette-index.json");
fs.writeFileSync(outPath, JSON.stringify(paletteIndex));

console.log(
  `[palette-index] Generated ${paletteIndex.length} entries (${(Buffer.byteLength(JSON.stringify(paletteIndex), "utf-8") / 1024).toFixed(0)} KB)`,
);
