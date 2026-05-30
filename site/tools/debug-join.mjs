/**
 * Debug the joining behavior on a specific section.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");

import("./repair-fragmentation.mjs").then(({ repairFile, joinFragmentedProse, cleanupBlankLines }) => {
  const file = "date-and-time-functions.md";
  const content = fs.readFileSync(path.join(contentDir, file), "utf-8");

  const repaired = repairFile(content);

  // Find the section around "doesn't include the time"
  const lines = repaired.split("\n");
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes("doesn't include the time")) {
      console.log(`=== Section at line ${i} ===`);
      for (let j = Math.max(0, i-2); j <= Math.min(lines.length-1, i+5); j++) {
        console.log(`${j}: ${JSON.stringify(lines[j])}`);
      }
      break;
    }
  }

  // Check for "zone offset"
  const zoneLines = lines.filter(l => l.includes("zone offset"));
  console.log(`\nLines containing "zone offset": ${zoneLines.length}`);
  zoneLines.forEach(l => console.log(`  ${JSON.stringify(l)}`));

  // Count lines
  console.log(`\nOriginal total lines: ${content.split("\n").length}`);
  console.log(`Repaired total lines: ${lines.length}`);

  // Sample of the SYSDATETIME section
  const sysIdx = lines.findIndex(l => l.includes("SYSDATETIME"));
  if (sysIdx >= 0) {
    console.log(`\n=== SYSDATETIME section (5 lines after) ===`);
    for (let j = sysIdx; j <= Math.min(lines.length-1, sysIdx+5); j++) {
      console.log(`${j}: ${JSON.stringify(lines[j])}`);
    }
  }
}).catch(e => { console.error("Error:", e); process.exit(1); });
