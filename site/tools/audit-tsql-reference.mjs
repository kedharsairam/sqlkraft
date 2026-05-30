/**
 * SqlKraft — T-SQL Reference Deep Content Validation Script
 *
 * Scans all 542 files in src/content/tsql-reference/ for:
 *   - Empty or placeholder descriptions
 *   - Garbled / PDF extraction artifacts
 *   - Fragmented body content (extraction damage)
 *   - Undersized content blocks
 *   - Title capitalization inconsistencies
 *
 * Performs automatic fixes for simple recurring issues.
 * Outputs a detailed markdown audit report.
 *
 * Usage:  node tools/audit-tsql-reference.mjs
 *         node tools/audit-tsql-reference.mjs --fix   (apply auto-fixes)
 *         node tools/audit-tsql-reference.mjs --report-only  (no fixes, just report)
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

// ──────────────────────────────────────────
// Configuration
// ──────────────────────────────────────────

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTENT_DIR = path.resolve(__dirname, "../src/content/tsql-reference");
const REPORT_FILE = path.resolve(__dirname, "../audit-tsql-reference-report.md");
const TRASH_DIR = path.resolve(__dirname, "../src/content/trash/tsql-reference");

const MIN_SENTENCE_LENGTH = 30; // characters — minimum for a meaningful sentence
const MIN_BODY_WORDS = 20; // words — minimum body content for a non-trivial page
const FRAGMENT_THRESHOLD = 0.7; // 70%+ lines being single-line fragments = extraction damage

const VALID_CATEGORIES = [
  "statements", "queries", "language-elements", "data-types",
  "operators", "functions", "hints", "predicates", "transactions",
  "variables", "xquery",
];

// ──────────────────────────────────────────
// Helpers
// ──────────────────────────────────────────

function parseFrontmatter(text) {
  const match = text.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!match) return { frontmatter: {}, body: text, rawFrontmatter: "" };
  const rawFm = match[1];
  const body = text.slice(match[0].length);
  const fm = {};
  for (const line of rawFm.split("\n")) {
    const kv = line.match(/^(\w+):\s*(.*)/);
    if (kv) {
      let val = kv[2].trim();
      // Remove surrounding quotes
      if ((val.startsWith('"') && val.endsWith('"')) ||
          (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      // Parse arrays: ["a", "b"]
      if (val.startsWith("[") && val.endsWith("]")) {
        try {
          val = JSON.parse(val.replace(/'/g, '"'));
        } catch {
          val = val.slice(1, -1).split(",").map(s => s.trim().replace(/["']/g, ""));
        }
      }
      // Parse dates
      if (kv[1] === "pubDate" || kv[1] === "updatedDate") {
        try { val = new Date(val); } catch { /* keep string */ }
      }
      fm[kv[1]] = val;
    }
  }
  return { frontmatter: fm, body, rawFrontmatter: rawFm };
}

function sentenceCount(text) {
  // Count sentences by terminal punctuation followed by space/end/line
  const matches = text.match(/[.!?][\s\n\r]|\.$/g);
  return matches ? matches.length : 0;
}

function wordCount(text) {
  return text.split(/\s+/).filter(w => w.length > 0).length;
}

function isGarbledChar(ch) {
  const code = ch.codePointAt(0);
  // U+FF89 HALFWIDTH KATAKANA LETTER NO (PDF artifact), replacement char, control chars
  // Exclude legitimate punctuation: U+2022 bullet, U+2013 en dash, U+2014 em dash
  return code === 0xFF89 || code === 0xFFFD || code === 0xFFFE || code === 0xFFFF ||
         (code >= 0x2000 && code <= 0x206F && code !== 0x2013 && code !== 0x2014 && code !== 0x2022) ||
         (code >= 0xFE00 && code <= 0xFE0F) || // variation selectors
         (code >= 0xE0000 && code <= 0xE007F); // tags block
}

function findGarbledChars(text) {
  const result = [];
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (isGarbledChar(ch)) {
      result.push({ char: ch, codePoint: ch.codePointAt(0).toString(16), position: i });
    }
  }
  return result;
}

function getContentQuality(body) {
  const lines = body.split("\n").filter(l => l.trim().length > 0);
  const totalLines = lines.length;
  if (totalLines === 0) return { totalLines: 0, singleWordLines: 0, fragmented: false, fractionSingleWord: 0 };

  // Count lines that are single words or short fragments (PDF extraction artifact)
  let singleWordLines = 0;
  let codeBlockLines = 0;
  let inCodeBlock = false;
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith("```")) { inCodeBlock = !inCodeBlock; codeBlockLines++; continue; }
    if (inCodeBlock) { codeBlockLines++; continue; }
    // Non-code lines: count words
    const words = trimmed.split(/\s+/).filter(w => w.length > 0);
    if (words.length <= 3 && trimmed.length < 60) {
      singleWordLines++;
    }
  }

  const nonCodeLines = totalLines - codeBlockLines;
  const fractionSingleWord = nonCodeLines > 0 ? singleWordLines / nonCodeLines : 0;
  const fragmented = fractionSingleWord >= FRAGMENT_THRESHOLD && nonCodeLines >= 10;

  return { totalLines, singleWordLines, nonCodeLines, fractionSingleWord, fragmented };
}

function isSuspiciousDescription(desc) {
  if (!desc || desc.length === 0) return { suspicious: true, reason: "empty" };
  const lower = desc.toLowerCase();
  const patterns = [
    { regex: /summarize this article/i, reason: "copilot prompt artifact" },
    { regex: /insert description here/i, reason: "placeholder text" },
    { regex: /^#{1,3}\s+\w+/, reason: "markdown heading used as description" },
    { regex: /^(tbd|todo|fixme|lorem ipsum)/i, reason: "placeholder" },
    { regex: /^https?:\/\//, reason: "URL-only description" },
  ];
  for (const p of patterns) {
    if (p.regex.test(lower)) return { suspicious: true, reason: p.reason };
  }
  // Description should be at least 10 chars
  if (desc.trim().length < 10 && desc.trim().length > 0) return { suspicious: true, reason: `too short (${desc.trim().length} chars)` };
  return { suspicious: false, reason: null };
}

function checkTitleCapitalization(title, filename) {
  // Check for leading letter-case issues in T-SQL keywords
  // Should be properly capitalized for T-SQL reference
  const issues = [];

  // Check if title looks like a sentence fragment starting lowercase
  if (title.length > 2 && title[0] === title[0].toLowerCase() && title[0] !== title[0].toUpperCase()) {
    issues.push("title starts with lowercase letter");
  }

  return issues;
}

function getSuggestedTitle(filename) {
  // Derive a proper display title from the filename slug
  let name = filename.replace(/\.md$/, "");
  // Capitalize first letter
  name = name.charAt(0).toUpperCase() + name.slice(1);
  // Handle common T-SQL keyword casing
  const keywordMap = {
    "Alter": "ALTER",
    "Create": "CREATE",
    "Drop": "DROP",
    "Select": "SELECT",
    "Insert": "INSERT",
    "Update": "UPDATE",
    "Delete": "DELETE",
    "Exec": "EXEC",
    "Execute": "EXECUTE",
    "Set": "SET",
    "Use": "USE",
    "With": "WITH",
    "Grant": "GRANT",
    "Revoke": "REVOKE",
    "Deny": "DENY",
    "Begin": "BEGIN",
    "Commit": "COMMIT",
    "Rollback": "ROLLBACK",
    "Save": "SAVE",
    "Truncate": "TRUNCATE",
    "Merge": "MERGE",
    "Open": "OPEN",
    "Close": "CLOSE",
    "Fetch": "FETCH",
    "Declare": "DECLARE",
    "Return": "RETURN",
    "Signal": "SIGNAL",
    "Call": "CALL",
    "Cursor": "CURSOR",
    "While": "WHILE",
    "If": "IF",
    "Else": "ELSE",
    "Case": "CASE",
    "When": "WHEN",
    "Then": "THEN",
    "End": "END",
    "Go": "GO",
    "As": "AS",
    "Is": "IS",
    "Not": "NOT",
    "Null": "NULL",
    "And": "AND",
    "Or": "OR",
    "In": "IN",
    "Exists": "EXISTS",
    "Between": "BETWEEN",
    "Like": "LIKE",
    "Order": "ORDER",
    "By": "BY",
    "Group": "GROUP",
    "Having": "HAVING",
    "Where": "WHERE",
    "From": "FROM",
    "Into": "INTO",
    "Values": "VALUES",
    "Join": "JOIN",
    "Left": "LEFT",
    "Right": "RIGHT",
    "Inner": "INNER",
    "Outer": "OUTER",
    "Cross": "CROSS",
    "Apply": "APPLY",
    "On": "ON",
    "Top": "TOP",
    "Distinct": "DISTINCT",
    "All": "ALL",
    "Union": "UNION",
    "Intersect": "INTERSECT",
    "Except": "EXCEPT",
    "For": "FOR",
    "Option": "OPTION",
    "Check": "CHECK",
    "Constraint": "CONSTRAINT",
    "Default": "DEFAULT",
    "Primary": "PRIMARY",
    "Foreign": "FOREIGN",
    "Key": "KEY",
    "References": "REFERENCES",
    "Unique": "UNIQUE",
    "Index": "INDEX",
    "View": "VIEW",
    "Procedure": "PROCEDURE",
    "Function": "FUNCTION",
    "Trigger": "TRIGGER",
    "Table": "TABLE",
    "Column": "COLUMN",
    "Schema": "SCHEMA",
    "Database": "DATABASE",
    "Server": "SERVER",
    "Role": "ROLE",
    "Login": "LOGIN",
    "User": "USER",
    "Type": "TYPE",
    "Assembly": "ASSEMBLY",
    "Message": "MESSAGE",
    "Contract": "CONTRACT",
    "Service": "SERVICE",
    "Route": "ROUTE",
    "Queue": "QUEUE",
    "Xml": "XML",
    "Json": "JSON",
    "Xquery": "XQUERY",
    "Sql": "SQL",
    "Tsql": "TSQL",
    "Dmv": "DMV",
    "Ssl": "SSL",
    "Tls": "TLS",
    "Ip": "IP",
    "Url": "URL",
    "Api": "API",
    "Cdc": "CDC",
    "Clr": "CLR",
    "Cte": "CTE",
    "Ddl": "DDL",
    "Dml": "DML",
    "Dcl": "DCL",
    "Tcl": "TCL",
    "Etl": "ETL",
    "Odbc": "ODBC",
    "Oledb": "OLEDB",
    "Pdw": "PDW",
    "Ssis": "SSIS",
    "Ssms": "SSMS",
    "Ssd": "SSD",
    "Ram": "RAM",
    "Cpu": "CPU",
    "Io": "IO",
    "Guid": "GUID",
    "Uuid": "UUID",
    "Hindex": "HINDEX",
    "Hekaton": "HEKATON",
  };

  const words = name.split(/[-_ ]/);
  const cased = words.map(w => keywordMap[w] || w);
  return cased.join(" ");
}

// ──────────────────────────────────────────
// Main Audit
// ──────────────────────────────────────────

async function audit() {
  const args = process.argv.slice(2);
  const applyFixes = args.includes("--fix");
  const reportOnly = args.includes("--report-only");

  if (!fs.existsSync(CONTENT_DIR)) {
    console.error(`Content directory not found: ${CONTENT_DIR}`);
    process.exit(1);
  }

  const files = fs.readdirSync(CONTENT_DIR).filter(f => f.endsWith(".md"));
  console.log(`Scanning ${files.length} files in ${CONTENT_DIR}...\n`);

  // Ensure trash directory exists
  if (applyFixes && !fs.existsSync(TRASH_DIR)) {
    fs.mkdirSync(TRASH_DIR, { recursive: true });
  }

  const results = {
    total: files.length,
    emptyDescriptions: [],
    suspiciousDescriptions: [],
    garbledContent: [],
    fragmentedContent: [],
    undersizedContent: [],
    titleIssues: [],
    categoryErrors: [],
    autoFixed: [],
    quarantined: [],
    invalidCategories: [],
  };

  let fixedCount = 0;

  for (const file of files) {
    const filePath = path.join(CONTENT_DIR, file);
    const content = fs.readFileSync(filePath, "utf-8");
    const { frontmatter, body, rawFrontmatter } = parseFrontmatter(content);
    const problems = [];

    // ── 1. Description checks ──
    const desc = frontmatter.description;
    if (typeof desc === "string" && desc.length === 0) {
      results.emptyDescriptions.push(file);
      problems.push("empty description");
    }

    const descCheck = isSuspiciousDescription(desc);
    if (descCheck.suspicious) {
      results.suspiciousDescriptions.push({ file, desc, reason: descCheck.reason });
      problems.push(`suspicious description: ${descCheck.reason}`);
    }

    // ── 2. Category validation ──
    const cat = frontmatter.category;
    if (cat && !VALID_CATEGORIES.includes(cat)) {
      results.invalidCategories.push({ file, category: cat });
      problems.push(`invalid category: "${cat}"`);
    }

    // ── 3. Garbled characters ──
    const garbled = findGarbledChars(content);
    if (garbled.length > 0) {
      results.garbledContent.push({ file, chars: garbled.map(g => `U+${g.codePoint.toUpperCase()} '${g.char}'`) });
      problems.push(`${garbled.length} garbled character(s) found`);
    }

    // ── 4. Body fragmentation / extraction damage ──
    const quality = getContentQuality(body);
    if (quality.fragmented) {
      results.fragmentedContent.push({
        file,
        fractionSingleWord: quality.fractionSingleWord.toFixed(2),
        totalNonCodeLines: quality.nonCodeLines,
      });
      problems.push(`fragmented content (${(quality.fractionSingleWord * 100).toFixed(0)}% single-fragment lines)`);
    }

    // ── 5. Undersized content ──
    const bodyWords = wordCount(body);
    if (bodyWords < MIN_BODY_WORDS && bodyWords > 0) {
      results.undersizedContent.push({ file, wordCount: bodyWords });
      problems.push(`undersized body (${bodyWords} words, min ${MIN_BODY_WORDS})`);
    }

    // ── 6. Title issues ──
    const title = frontmatter.title || "";
    const titleIssues = checkTitleCapitalization(title, file);
    if (titleIssues.length > 0) {
      results.titleIssues.push({ file, title, issues: titleIssues });
      problems.push(`title issue: ${titleIssues.join("; ")}`);
    }

    // ── 7. Auto-fix: descriptions ──
    if (applyFixes) {
      let needsDescFix = false;
      let newDesc = "";

      if (typeof desc === "string" && desc.length === 0) {
        // Empty description — derive from body or title
        needsDescFix = true;
        const bodyWords = body.split(/\s+/).filter(w => w.length > 0);
        if (bodyWords.length >= 5) {
          const raw = bodyWords.slice(0, 20).join(" ");
          const firstSentence = raw.match(/^[^.!?]*[.!?]/);
          newDesc = firstSentence ? firstSentence[0].trim() : raw.slice(0, 120).trim() + ".";
        }
        if (!newDesc || newDesc.length < 10) {
          newDesc = `T-SQL reference for ${title || file.replace(".md", "")} syntax and usage.`;
        }
      } else if (typeof desc === "string" && /^(###?\s+|#{1,3}\s)/.test(desc)) {
        // Description is a markdown heading — replace with meaningful text
        needsDescFix = true;
        const headingText = desc.replace(/^#{1,3}\s+/, "").trim();
        newDesc = `T-SQL reference covering ${headingText}.`;
      } else if (typeof desc === "string" && /^summarize this article/i.test(desc)) {
        // Copilot prompt artifact
        needsDescFix = true;
        newDesc = `T-SQL reference for ${title || file.replace(".md", "")} syntax and usage.`;
      }

      if (needsDescFix) {
        const escapedDesc = newDesc.replace(/"/g, '\\"');
        if (desc && desc.length > 0) {
          // Replace non-empty description
          const descLine = rawFrontmatter.split("\n").find(l => l.startsWith("description:"));
          if (descLine) {
            const newContent = content.replace(descLine, `description: "${escapedDesc}"`);
            fs.writeFileSync(filePath, newContent, "utf-8");
          }
        } else {
          // Replace empty description
          const newContent = content.replace(
            /^description:\s*""$/m,
            `description: "${escapedDesc}"`
          );
          if (newContent !== content) {
            fs.writeFileSync(filePath, newContent, "utf-8");
          }
        }
        results.autoFixed.push({ file, field: "description", old: desc || "", new: newDesc });
        fixedCount++;
        problems.push(`AUTO-FIXED: description → "${newDesc.substring(0, 60)}..."`);
      }
    }

    // ── 8. Auto-fix: garbled character removal ──
    if (applyFixes && garbled.length > 0) {
      let cleaned = content;
      let removed = 0;
      for (const g of garbled) {
        const before = cleaned.length;
        cleaned = cleaned.replace(g.char, "");
        if (cleaned.length < before) removed++;
      }
      if (removed > 0) {
        fs.writeFileSync(filePath, cleaned, "utf-8");
        if (!results.autoFixed.find(f => f.file === file)) {
          results.autoFixed.push({ file, field: "content", old: `${garbled.length} garbled chars`, new: "removed" });
        }
        fixedCount++;
      }
    }

    // Log per-file problems
    if (problems.length > 0 && !reportOnly) {
      console.log(`  ${file}: ${problems.join("; ")}`);
    }
  }

  // ──────────────────────────────────────────
  // Generate Report
  // ──────────────────────────────────────────

  const totalDefects =
    results.emptyDescriptions.length +
    results.suspiciousDescriptions.length +
    results.garbledContent.length +
    results.fragmentedContent.length +
    results.undersizedContent.length +
    results.titleIssues.length +
    results.invalidCategories.length;

  const reportLines = [];
  reportLines.push(`# T-SQL Reference Content Audit Report`);
  reportLines.push(``);
  reportLines.push(`**Date:** ${new Date().toISOString().split("T")[0]}`);
  reportLines.push(`**Files scanned:** ${results.total}`);
  reportLines.push(`**Total defects found:** ${totalDefects}`);
  if (applyFixes) reportLines.push(`**Auto-fixes applied:** ${fixedCount}`);
  reportLines.push(``);
  reportLines.push(`## Summary`);
  reportLines.push(``);
  reportLines.push(`| Defect Category | Count |`);
  reportLines.push(`|-----------------|-------:|`);
  reportLines.push(`| Empty descriptions | ${results.emptyDescriptions.length} |`);
  reportLines.push(`| Suspicious descriptions | ${results.suspiciousDescriptions.length} |`);
  reportLines.push(`| Garbled/extraction artifacts | ${results.garbledContent.length} |`);
  reportLines.push(`| Fragmented body content | ${results.fragmentedContent.length} |`);
  reportLines.push(`| Undersized content (< ${MIN_BODY_WORDS} words) | ${results.undersizedContent.length} |`);
  reportLines.push(`| Title/capitalization issues | ${results.titleIssues.length} |`);
  reportLines.push(`| Invalid categories | ${results.invalidCategories.length} |`);
  reportLines.push(``);

  // ── Empty Descriptions ──
  if (results.emptyDescriptions.length > 0) {
    reportLines.push(`## Empty Descriptions (${results.emptyDescriptions.length})`);
    reportLines.push(``);
    reportLines.push(`Files with \`description: ""\` in frontmatter:`);
    reportLines.push(``);
    for (const f of results.emptyDescriptions) {
      reportLines.push(`- \`${f}\``);
    }
    reportLines.push(``);
  }

  // ── Suspicious Descriptions ──
  if (results.suspiciousDescriptions.length > 0) {
    reportLines.push(`## Suspicious Descriptions (${results.suspiciousDescriptions.length})`);
    reportLines.push(``);
    reportLines.push(`| File | Description | Issue |`);
    reportLines.push(`|------|-------------|-------|`);
    for (const s of results.suspiciousDescriptions) {
      reportLines.push(`| \`${s.file}\` | "${s.desc}" | ${s.reason} |`);
    }
    reportLines.push(``);
  }

  // ── Garbled Content ──
  if (results.garbledContent.length > 0) {
    reportLines.push(`## Garbled / Extraction Artifacts (${results.garbledContent.length})`);
    reportLines.push(``);
    reportLines.push(`Files containing garbled Unicode characters (PDF extraction artifacts):`);
    reportLines.push(``);
    reportLines.push(`| File | Characters Found |`);
    reportLines.push(`|------|-----------------|`);
    for (const g of results.garbledContent) {
      reportLines.push(`| \`${g.file}\` | ${g.chars.join(", ")} |`);
    }
    reportLines.push(``);
  }

  // ── Fragmented Content ──
  if (results.fragmentedContent.length > 0) {
    reportLines.push(`## Fragmented / Extraction-Damaged Content (${results.fragmentedContent.length})`);
    reportLines.push(``);
    reportLines.push(`Files where >${Math.round(FRAGMENT_THRESHOLD * 100)}% of non-code lines are single words/fragments (likely PDF extraction damage):`);
    reportLines.push(``);
    reportLines.push(`| File | Fragment % | Non-Code Lines |`);
    reportLines.push(`|------|-----------:|:--------------:|`);
    for (const f of results.fragmentedContent) {
      reportLines.push(`| \`${f.file}\` | ${(parseFloat(f.fractionSingleWord) * 100).toFixed(0)}% | ${f.totalNonCodeLines} |`);
    }
    reportLines.push(``);
  }

  // ── Undersized Content ──
  if (results.undersizedContent.length > 0) {
    reportLines.push(`## Undersized Content (${results.undersizedContent.length})`);
    reportLines.push(``);
    reportLines.push(`Files with fewer than ${MIN_BODY_WORDS} words of body content (excluding frontmatter):`);
    reportLines.push(``);
    reportLines.push(`| File | Word Count |`);
    reportLines.push(`|------|-----------:|`);
    for (const u of results.undersizedContent) {
      reportLines.push(`| \`${u.file}\` | ${u.wordCount} |`);
    }
    reportLines.push(``);
  }

  // ── Title Issues ──
  if (results.titleIssues.length > 0) {
    reportLines.push(`## Title / Capitalization Issues (${results.titleIssues.length})`);
    reportLines.push(``);
    reportLines.push(`| File | Current Title | Issues |`);
    reportLines.push(`|------|---------------|--------|`);
    for (const t of results.titleIssues) {
      reportLines.push(`| \`${t.file}\` | "${t.title}" | ${t.issues.join("; ")} |`);
    }
    reportLines.push(``);
  }

  // ── Invalid Categories ──
  if (results.invalidCategories.length > 0) {
    reportLines.push(`## Invalid Categories (${results.invalidCategories.length})`);
    reportLines.push(``);
    reportLines.push(`| File | Category |`);
    reportLines.push(`|------|----------|`);
    for (const c of results.invalidCategories) {
      reportLines.push(`| \`${c.file}\` | "${c.category}" |`);
    }
    reportLines.push(``);
  }

  // ── Auto-Fixes Applied ──
  if (results.autoFixed.length > 0) {
    reportLines.push(`## Auto-Fixes Applied (${results.autoFixed.length})`);
    reportLines.push(``);
    reportLines.push(`| File | Field | Change |`);
    reportLines.push(`|------|-------|--------|`);
    for (const a of results.autoFixed) {
      reportLines.push(`| \`${a.file}\` | ${a.field} | "${a.old}" → "${a.new.substring(0, 60)}${a.new.length > 60 ? '...' : ''}" |`);
    }
    reportLines.push(``);
  }

  // ── Conclusion ──
  reportLines.push(`## Recommendations`);
  reportLines.push(``);
  if (results.fragmentedContent.length > 50) {
    reportLines.push(`- **Critical**: ${results.fragmentedContent.length} files show severe PDF extraction fragmentation. These files need manual content restoration or replacement with properly sourced content.`);
  }
  if (results.emptyDescriptions.length > 0) {
    reportLines.push(`- ${results.emptyDescriptions.length} files had empty descriptions ${applyFixes ? '(auto-fixed)' : '(auto-fix available with --fix)'}.`);
  }
  if (results.garbledContent.length > 0) {
    reportLines.push(`- ${results.garbledContent.length} files contain garbled Unicode artifacts from PDF extraction ${applyFixes ? '(auto-fixed)' : '(auto-fix available with --fix)'}.`);
  }
  if (results.undersizedContent.length > 0) {
    reportLines.push(`- ${results.undersizedContent.length} files have very little body content and may need manual authoring.`);
  }
  reportLines.push(``);
  reportLines.push(`---`);
  reportLines.push(`*Report generated by tools/audit-tsql-reference.mjs*`);

  const reportContent = reportLines.join("\n");
  fs.writeFileSync(REPORT_FILE, reportContent, "utf-8");
  console.log(`\nReport written to: ${REPORT_FILE}`);

  // Print summary to console
  console.log(`\n═══ AUDIT SUMMARY ═══`);
  console.log(`  Total files:        ${results.total}`);
  console.log(`  Empty descriptions: ${results.emptyDescriptions.length}`);
  console.log(`  Suspicious desc:    ${results.suspiciousDescriptions.length}`);
  console.log(`  Garbled artifacts:  ${results.garbledContent.length}`);
  console.log(`  Fragmented content: ${results.fragmentedContent.length}`);
  console.log(`  Undersized content: ${results.undersizedContent.length}`);
  console.log(`  Title issues:       ${results.titleIssues.length}`);
  console.log(`  Invalid categories: ${results.invalidCategories.length}`);
  console.log(`  Total defects:      ${totalDefects}`);
  if (applyFixes) console.log(`  Auto-fixes applied: ${fixedCount}`);
  console.log(`  Report:             ${REPORT_FILE}`);
  console.log(`═══════════════════════\n`);
}

audit().catch(console.error);
