#!/usr/bin/env node
// Comprehensive content quality audit
// Checks every markdown file for formatting, structure, and consistency issues

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTENT_DIR = path.resolve(__dirname, "../src/content");
const EXT = ".md";

// ── Stats ──
let total = 0;
let issues = [];
let stats = {
  filesWithIssues: 0,
  totalIssues: 0,
  byCategory: {},
};

function report(file, category, message, detail = "") {
  issues.push({ file, category, message, detail });
  stats.totalIssues++;
  stats.byCategory[category] = (stats.byCategory[category] || 0) + 1;
}

// ── Scan helpers ──
function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      // Skip trash, config.ts
      if (entry.name === "trash") continue;
      files.push(...walk(full));
    } else if (entry.name.endsWith(EXT)) {
      files.push(full);
    }
  }
  return files;
}

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) return null;
  const fm = {};
  const lines = match[1].split("\n");
  let currentKey = null;
  let currentValue = [];
  let inLiteralBlock = false;

  for (const line of lines) {
    const kv = line.match(/^(\w+):\s*(.*)/);
    if (kv) {
      // Save previous key if any
      if (currentKey) {
        fm[currentKey] = currentValue.join("\n").replace(/^"|"$/g, "");
      }
      currentKey = kv[1];
      const val = kv[2];
      if (val === "|") {
        inLiteralBlock = true;
        currentValue = [];
      } else {
        inLiteralBlock = false;
        currentValue = [val];
      }
    } else if (inLiteralBlock) {
      currentValue.push(line);
    } else if (currentKey && line.startsWith("  ")) {
      // Folded or wrapped value (for array items like tags)
      currentValue.push(line.trim());
    }
  }
  if (currentKey) {
    fm[currentKey] = currentValue.join("\n").replace(/^"|"$/g, "");
  }
  return fm;
}

// ── Check functions ──

function checkFrontmatter(file, relPath, content) {
  const fm = parseFrontmatter(content);
  if (!fm) {
    report(relPath, "frontmatter", "Missing or invalid frontmatter");
    return;
  }

  // Required fields
  const required = ["name", "title", "description"];
  for (const field of required) {
    if (!fm[field]) {
      report(relPath, "frontmatter", `Missing required frontmatter field: "${field}"`);
    }
  }

  // Description quality
  if (fm.description) {
    const desc = fm.description;
    if (desc.length < 10) {
      report(relPath, "description", `Description too short (${desc.length} chars): "${desc}"`);
    }
    if (desc.endsWith(".") && desc.length > 30 && !desc.endsWith(". ")) {
      // Single sentence without trailing space is fine
    }
    // Check for boilerplate remnants
    const boilerplateSigns = [
      "Azure SQL Database Azure SQL Managed Instance",
      "Transact-SQL syntax conventions",
      "Applies to:",
      "Last updated on",
      "Related content",
    ];
    for (const sign of boilerplateSigns) {
      if (desc.includes(sign)) {
        report(relPath, "boilerplate", `Description contains boilerplate: "${sign.slice(0, 40)}..."`);
      }
    }

    // Check for column metadata markers at start
    const colMarkers = /^(ID of|Name of|Identifier of|Object identification|The name of|The class of|The ID of|Path of|Handle of)/i;
    if (colMarkers.test(desc)) {
      report(relPath, "boilerplate", `Description starts with column metadata marker: "${desc.slice(0, 50)}..."`);
    }
  }

  // Check pubDate
  if (fm.pubDate) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(fm.pubDate)) {
      report(relPath, "frontmatter", `Invalid pubDate format: "${fm.pubDate}" (expected YYYY-MM-DD)`);
    }
  } else {
    report(relPath, "frontmatter", "Missing pubDate");
  }

  // Check tags
  if (fm.tags) {
    try {
      const tags = JSON.parse(fm.tags);
      if (!Array.isArray(tags)) {
        report(relPath, "frontmatter", "tags is not an array");
      }
    } catch {
      report(relPath, "frontmatter", `Invalid tags JSON: "${fm.tags.slice(0, 50)}..."`);
    }
  }
}

function checkHeadings(file, relPath, content) {
  // Remove frontmatter
  const body = content.replace(/^---\n[\s\S]*?\n---\n/, "");

  // Check heading order (no skipping levels)
  const headings = body.match(/^#{1,6}\s/gm);
  if (headings) {
    let prevLevel = 1;
    for (const h of headings) {
      const level = h.trim().length;
      if (level > prevLevel + 1) {
        report(relPath, "headings", `Heading level skipped: ${h.trim()} -> previous was ${prevLevel}`);
      }
      prevLevel = level;
    }
  }

  // Check for duplicate headings (same level, same text)
  const headingTexts = body.match(/^#{1,6}\s.+$/gm);
  if (headingTexts) {
    const seen = new Set();
    for (const ht of headingTexts) {
      if (seen.has(ht.toLowerCase())) {
        report(relPath, "headings", `Duplicate heading: "${ht}"`);
      }
      seen.add(ht.toLowerCase());
    }
  }
}

function checkCodeFences(file, relPath, content) {
  const body = content.replace(/^---\n[\s\S]*?\n---\n/, "");
  const openFences = body.match(/```/g);
  if (openFences && openFences.length % 2 !== 0) {
    report(relPath, "code-fences", `Unbalanced code fences (${openFences.length} backtick-triplets)`);
  }

  // Check for empty code fences
  const emptyFences = body.match(/```\w*\n```/g);
  if (emptyFences) {
    report(relPath, "code-fences", `${emptyFences.length} empty code fence(s)`);
  }

  // Check for code fences without language specifier
  // Count only opening fences (odd occurrences of ``` in the sequence)
  const allFences = [...body.matchAll(/^```/gm)];
  let openingUnlabeled = 0;
  for (let i = 0; i < allFences.length; i++) {
    // Opening fences are at even indices (0, 2, 4...) in a balanced file
    if (i % 2 === 0) {
      const pos = allFences[i].index;
      const lineStart = body.lastIndexOf("\n", pos) + 1;
      const lineEnd = body.indexOf("\n", pos);
      const line = body.slice(lineStart, lineEnd === -1 ? undefined : lineEnd);
      // Opening fence should have a language specifier after ```
      const rest = line.slice(3).trim();
      if (!rest) {
        openingUnlabeled++;
      }
    }
  }
  if (openingUnlabeled > 0) {
    report(relPath, "code-fences", `${openingUnlabeled} opening code fence(s) without language specification`);
  }
}

function checkBoilerplate(file, relPath, content) {
  const body = content.replace(/^---\n[\s\S]*?\n---\n/, "");

  // Check for common Microsoft documentation artifacts
  const artifacts = [
    { pattern: /Transact-SQL syntax conventions/gi, label: "Transact-SQL syntax conventions" },
    { pattern: /Applies to:/gi, label: "Applies to:" },
    { pattern: /Last updated on \d{1,2}\/\d{1,2}\/\d{4}/gi, label: "Last updated on date" },
    { pattern: /Related content/gi, label: "Related content section" },
    { pattern: /Azure SQL Database Azure SQL Managed Instance/gi, label: "Platform name list" },
    { pattern: /SQL Server \(all supported versions\)/gi, label: "All supported versions boilerplate" },
  ];

  for (const { pattern, label } of artifacts) {
    const matches = body.match(pattern);
    if (matches) {
      report(relPath, "boilerplate", `${matches.length} occurrence(s) of "${label}"`);
    }
  }
}

function checkFormatting(file, relPath, content) {
  const body = content.replace(/^---\n[\s\S]*?\n---\n/, "");

  // Check for trailing whitespace
  const lines = body.split("\n");
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].length > 0 && lines[i] !== lines[i].trimEnd()) {
      report(relPath, "whitespace", `Trailing whitespace on line ${i + 1}`);
      break; // One report per file is enough
    }
  }

  // Check for extremely long lines (> 500 chars)
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].length > 500 && !lines[i].startsWith("|")) {
      report(relPath, "long-lines", `Line ${i + 1} is ${lines[i].length} characters (max 500)`);
      break;
    }
  }

  // Check for hard tabs
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes("\t")) {
      report(relPath, "formatting", `Hard tab on line ${i + 1}`);
      break;
    }
  }

  // Check for consecutive blank lines (more than 2)
  let blankCount = 0;
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].trim() === "") {
      blankCount++;
      if (blankCount > 2) {
        report(relPath, "formatting", `More than 2 consecutive blank lines around line ${i + 1}`);
        break;
      }
    } else {
      blankCount = 0;
    }
  }
}

function checkSyntaxSection(file, relPath, content) {
  const body = content.replace(/^---\n[\s\S]*?\n---\n/, "");

  // Check if Description section exists and has content
  const descMatch = body.match(/^## Description\s*\n([\s\S]*?)(?=\n## |\n$|$)/);
  if (descMatch) {
    const descContent = descMatch[1].trim();
    if (!descContent) {
      report(relPath, "content", "Description section is empty");
    }
  } else {
    // Some files might not have a Description section — that's OK for some collections
  }

  // Check if Syntax section exists
  const syntaxMatch = body.match(/^## Syntax/);
  if (!syntaxMatch) {
    // Only flag for collections that should have syntax
    const collectionsWithSyntax = ["dmvs", "stored-procedures", "functions", "tsql-reference", "catalog-views"];
    const inDir = collectionsWithSyntax.some((c) => relPath.startsWith(c));
    if (inDir) {
      report(relPath, "content", "Missing Syntax section");
    }
  }
}

// ── Main ──
console.log("🔍 Starting comprehensive content audit...\n");

const files = walk(CONTENT_DIR);
total = files.length;

for (const file of files) {
  const relPath = path.relative(CONTENT_DIR, file);
  const content = fs.readFileSync(file, "utf-8");

  checkFrontmatter(file, relPath, content);
  checkHeadings(file, relPath, content);
  checkCodeFences(file, relPath, content);
  checkBoilerplate(file, relPath, content);
  checkFormatting(file, relPath, content);
  checkSyntaxSection(file, relPath, content);
}

// ── Summary ──
console.log(`\n📊 Audit Results:`);
console.log(`   Total files scanned: ${total}`);
console.log(`   Files with issues:    ${new Set(issues.map((i) => i.file)).size}`);
console.log(`   Total issues found:  ${stats.totalIssues}`);
console.log(`\n   By category:`);

const sortedCategories = Object.entries(stats.byCategory).sort((a, b) => b[1] - a[1]);
for (const [cat, count] of sortedCategories) {
  console.log(`     ${cat.padEnd(20)} ${count}`);
}

// ── Detailed report ──
if (issues.length > 0) {
  console.log(`\n📋 Detailed Issue Report:\n`);
  // Group by category
  const byCat = {};
  for (const issue of issues) {
    if (!byCat[issue.category]) byCat[issue.category] = [];
    byCat[issue.category].push(issue);
  }

  for (const [cat, catIssues] of Object.entries(byCat).sort((a, b) => b[1].length - a[1].length)) {
    console.log(`  ── ${cat.toUpperCase()} (${catIssues.length} issues) ──`);
    // Show first 10 per category
    const shown = catIssues.slice(0, 10);
    for (const issue of shown) {
      console.log(`     ${issue.file}`);
      console.log(`       ${issue.message}`);
      if (issue.detail) console.log(`       ${issue.detail}`);
    }
    if (catIssues.length > 10) {
      console.log(`       ... and ${catIssues.length - 10} more`);
    }
    console.log();
  }
}

// ── Exit code ──
const SEVERE_CATEGORIES = ["frontmatter", "code-fences", "content"];
const severeIssues = issues.filter((i) => SEVERE_CATEGORIES.includes(i.category));
if (severeIssues.length > 0) {
  console.log(`\n⚠️  ${severeIssues.length} severe issue(s) found (frontmatter, code-fences, content).`);
}

console.log(`\n✅ Audit complete.`);
