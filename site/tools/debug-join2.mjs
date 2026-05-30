/**
 * Deep debug: check function outputs for specific lines.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

import("./repair-fragmentation.mjs").then((mod) => {
  const { isContinuationLine, isStandaloneItem, hasContinuationMarker, repairFile } = mod;
  
  // Test specific lines
  const testLines = [
    "The returned value doesn't include the time",
    "zone offset.",
    "datetime2(7)",
    "The",
    "function returns a",
    "SYSDATETIME",
  ];
  
  console.log("=== Function Tests ===");
  for (const line of testLines) {
    console.log(`Line: "${line}"`);
    console.log(`  isContinuationLine: ${isContinuationLine(line)}`);
    console.log(`  isStandaloneItem: ${isStandaloneItem(line)}`);
    console.log(`  hasContinuationMarker: ${hasContinuationMarker(line)}`);
    console.log(`  noEndingPunct: ${!/[.!?]$/.test(line)}`);
    console.log();
  }
  
  // Check the file directly
  const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");
  const content = fs.readFileSync(path.join(contentDir, "date-and-time-functions.md"), "utf-8");
  
  // Find lines with "include the time" and "zone offset" in original
  const origLines = content.split("\n");
  console.log("=== Lines containing 'include the time' in ORIGINAL ===");
  origLines.forEach((l, i) => {
    if (l.includes("include the time")) console.log(`  ${i}: ${JSON.stringify(l)}`);
  });
  console.log("=== Lines containing 'zone offset' in ORIGINAL ===");
  origLines.forEach((l, i) => {
    if (l.includes("zone offset")) console.log(`  ${i}: ${JSON.stringify(l)}`);
  });
  
  // Check final output
  const repaired = repairFile(content);
  const repairedLines = repaired.split("\n");
  console.log(`\n=== Lines containing 'zone offset' in REPAIRED ===`);
  repairedLines.forEach((l, i) => {
    if (l.includes("zone offset")) console.log(`  ${i}: ${JSON.stringify(l)}`);
  });
  
  // Also check the last few lines and first few lines
  console.log(`\n=== First 10 repaired lines ===`);
  repairedLines.slice(0, 10).forEach((l, i) => console.log(`  ${i}: ${JSON.stringify(l)}`));
  
  console.log(`\n=== Last 10 repaired lines ===`);
  repairedLines.slice(-10).forEach((l, i) => console.log(`  ${repairedLines.length - 10 + i}: ${JSON.stringify(l)}`));
}).catch(e => { console.error("Error:", e); process.exit(1); });
