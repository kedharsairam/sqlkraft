/**
 * Extract file lists from audit report.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const reportPath = path.resolve(__dirname, "../audit-tsql-reference-report.md");
const content = fs.readFileSync(reportPath, "utf-8");

// Extract undersized files
const undersizedMatch = content.match(/## Undersized Content[\s\S]*?(?=## )/);
if (undersizedMatch) {
  console.log("=== UNDERSIZED FILES (" + (undersizedMatch[0].match(/\| `([^`]+)`/g) || []).length + ") ===");
  const lines = undersizedMatch[0].split("\n");
  for (const line of lines) {
    const m = line.match(/`([^`]+)`/);
    if (m) console.log(m[1]);
  }
}

// Extract fragmented files
const fragmentedMatch = content.match(/## Fragmented[\s\S]*?(?=## )/);
if (fragmentedMatch) {
  console.log("\n=== FRAGMENTED FILES (" + (fragmentedMatch[0].match(/\| `([^`]+)`/g) || []).length + ") ===");
  const lines = fragmentedMatch[0].split("\n");
  for (const line of lines) {
    const m = line.match(/`([^`]+)`/);
    if (m) console.log(m[1]);
  }
}
