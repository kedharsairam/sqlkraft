/**
 * Preview effect of repair on specific files.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Dynamically load the repair module
import("./repair-fragmentation.mjs").then(({ repairFile }) => {
  const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");
  
  const filesToPreview = [
    "abs.md",
    "odbc-reserved-keywords.md",
    "future-keywords.md",
    "arithmetic-operators.md",
    "date-and-time-functions.md",
    "stgeometryn-geometry-data-type.md",
    "uniqueidentifier.md",
    "loginproperty.md",
    "encryptbypassphrase.md",
  ];

  for (const file of filesToPreview) {
    const filePath = path.join(contentDir, file);
    const content = fs.readFileSync(filePath, "utf-8");
    
    // Find body start (after second ---)
    const firstSep = content.indexOf("---");
    const secondSep = content.indexOf("---", firstSep + 1);
    const bodyStart = secondSep + 3;
    
    console.log("=".repeat(80));
    console.log(`FILE: ${file}`);
    console.log("=".repeat(80));
    
    const repaired = repairFile(content);
    
    const origBody = content.slice(bodyStart).trim().split("\n");
    const repairedBody = repaired.slice(repaired.indexOf("---", repaired.indexOf("---") + 1) + 3).trim().split("\n");
    
    console.log(`\n--- ORIGINAL (${origBody.length} body lines) ---`);
    console.log(origBody.slice(0, 40).join("\n"));
    if (origBody.length > 40) console.log(`  ... (${origBody.length - 40} more lines)`);
    
    console.log(`\n--- REPAIRED (${repairedBody.length} body lines) ---`);
    console.log(repairedBody.slice(0, 40).join("\n"));
    if (repairedBody.length > 40) console.log(`  ... (${repairedBody.length - 40} more lines)`);
    
    console.log("\n");
  }
  
  console.log("Preview complete.");
}).catch(e => {
  console.error("Error:", e);
  process.exit(1);
});
