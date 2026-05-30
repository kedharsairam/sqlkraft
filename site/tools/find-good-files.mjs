/**
 * Find non-fragmented tsql-reference files with good content structure.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");
const reportPath = path.resolve(__dirname, "../audit-tsql-reference-report.md");

const files = fs.readdirSync(contentDir).filter(f => f.endsWith(".md"));

// Parse report for fragmented and undersized lists
const report = fs.readFileSync(reportPath, "utf-8");

function extractFileList(report, sectionHeading) {
  const re = new RegExp(`## ${sectionHeading}[\\s\\S]*?(?=## )`);
  const match = report.match(re);
  if (!match) return new Set();
  const lines = match[0].split("\n");
  const list = new Set();
  for (const line of lines) {
    const m = line.match(/`([^`]+\.md)`/);
    if (m) list.add(m[1]);
  }
  return list;
}

const fragmented = extractFileList(report, "Fragmented");
const undersized = extractFileList(report, "Undersized Content");

const goodFiles = files.filter(f => !fragmented.has(f) && !undersized.has(f) && f !== "index.md");

console.log(`Total good (non-fragmented, non-undersized) files: ${goodFiles.length}`);

// Sample and display some
const samples = goodFiles.sort(() => Math.random() - 0.5).slice(0, 15);
for (const f of samples) {
  const content = fs.readFileSync(path.join(contentDir, f), "utf-8");
  const lines = content.trim().split("\n").filter(
    l => !l.startsWith("---") && !l.includes(": ")
  );
  const wordCount = content.split(/\s+/).length;
  const bodyPreview = lines.slice(0, 5).join(" ").replace(/\s+/g, " ").trim();
  console.log(`${f} | words: ${wordCount} | body: ${bodyPreview.slice(0, 150)}...`);
}
