/**
 * Test full pipeline step by step to find where joining fails.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

import("./repair-fragmentation.mjs").then((mod) => {
  const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");
  const content = fs.readFileSync(path.join(contentDir, "date-and-time-functions.md"), "utf-8");

  const lines = content.split("\n");
  
  // Find lines around the SYSDATETIME section in the ORIGINAL
  console.log("=== Original: lines around SYSDATETIME ===");
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes("SYSDATETIME")) {
      for (let j = Math.max(0, i - 2); j <= Math.min(lines.length - 1, i + 25); j++) {
        console.log(`${j}: ${JSON.stringify(lines[j])}`);
      }
      break;
    }
  }
}).catch(e => console.error("Error:", e));
