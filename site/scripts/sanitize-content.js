/**
 * sanitize-content.js — Automated Markdown Sanitization Engine
 *
 * Scans all content collections for common ingestion corruption artifacts
 * and repairs them programmatically:
 *
 *   1. Strip dangling metadata headings (#### syntaxsql, ### nvarchar, etc.)
 *   2. Convert single-word code blocks to inline code
 *   3. Join fragmented sentences (broken across lines)
 *   4. Collapse excessive blank lines
 *   5. Delete completely empty stub files (headings only, no real content)
 *
 * Usage:  node scripts/sanitize-content.js [--dry-run] [--collections=tsql-reference,architecture]
 *
 * Default: runs on ALL content collections, writes changes in-place.
 * --dry-run:  report only, no writes.
 * --collections: comma-separated list of collection dirs to process.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

/* ── Config ── */
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTENT_ROOT = path.resolve(__dirname, "..", "src", "content");

const args = process.argv.slice(2);
const DRY_RUN = args.includes("--dry-run");
const COLLECTIONS_FILTER = args
  .find((a) => a.startsWith("--collections="))
  ?.split("=")[1]
  ?.split(",")
  .map((s) => s.trim())
  .filter(Boolean);

/* ── Datatype names to strip as standalone headings ── */
const DATATYPE_NAMES = new Set([
  "int",
  "bigint",
  "smallint",
  "tinyint",
  "bit",
  "decimal",
  "numeric",
  "money",
  "smallmoney",
  "float",
  "real",
  "datetime",
  "datetime2",
  "datetimeoffset",
  "date",
  "time",
  "char",
  "varchar",
  "nchar",
  "nvarchar",
  "text",
  "ntext",
  "binary",
  "varbinary",
  "image",
  "xml",
  "json",
  "sql_variant",
  "sql-variant",
  "hierarchyid",
  "geography",
  "geometry",
  "uniqueidentifier",
  "rowversion",
  "timestamp",
  "cursor",
  "table",
  "sysname",
  "xml",
]);

/* ── Heading levels to strip as standalone ingestion artifact headings ── */
const METADATA_HEADING_RE = /^#{3,4}\s+(syntaxsql|syntax|nvarchar|int|bigint|smallint|tinyint|varchar|char|nchar|decimal|numeric|float|real|datetime|datetime2|date|time|datetimeoffset|money|smallmoney|bit|binary|varbinary|image|text|ntext|xml|sql_variant|hierarchyid|geography|geometry|uniqueidentifier|rowversion|timestamp|cursor|table|sysname)\s*$/i;

/* ── Lines that are just the word "sql" or "SQL" ── */
const SQL_BLOCK_WORD_RE = /^sql$/i;

/* ── Lines that are just a single word/punctuation fragment inside a code block ── */
const STRAY_CODE_BLOCK_WORD_RE = /^[A-Za-z][A-Za-z0-9_.#()[\]]{0,30}$/;

/* ── Stats tracking ── */
const stats = {
  files_scanned: 0,
  dangling_headings_removed: 0,
  stray_code_blocks_fixed: 0,
  fragmented_sentences_joined: 0,
  blank_lines_collapsed: 0,
  empty_stubs_deleted: 0,
  files_modified: 0,
  errors: [],
};

/* ════════════════════════════════════════════════════════════════
   FRONTMATTER HELPERS
   ════════════════════════════════════════════════════════════════ */

/**
 * Parse frontmatter into key-value pairs, handling both
 * `key: "value"` and `key: |` (YAML literal block) formats.
 */
function parseFrontmatterMap(frontmatterText) {
  const lines = frontmatterText.split("\n");
  const map = {};
  let currentKey = null;
  let inLiteralBlock = false;

  // Remove the --- markers
  const bodyLines = lines.filter((l) => !/^---/.test(l.trim()));

  for (const line of bodyLines) {
    const kv = line.match(/^(\w[\w-]*):\s*(.*)/);
    if (kv) {
      currentKey = kv[1];
      const val = kv[2].trim();
      if (val === "|") {
        inLiteralBlock = true;
        map[currentKey] = ""; // placeholder
        continue;
      }
      inLiteralBlock = false;
      map[currentKey] = val.replace(/^"|"$/g, "");
    } else if (inLiteralBlock && currentKey) {
      // Accumulate literal block content
      const prev = map[currentKey] || "";
      map[currentKey] = prev + (prev ? "\n" : "") + line;
    } else if (/^\s+-\s/.test(line) && currentKey) {
      // YAML list item:   - "value" or   - value
      // Reinitialize as array if the current value is empty string (e.g., "tags:" with no inline value)
      const existing = map[currentKey];
      if (!Array.isArray(existing)) {
        map[currentKey] = [];
      }
      const itemMatch = line.match(/^\s+-\s+"([^"]*)"\s*$/);
      if (itemMatch) {
        map[currentKey].push(itemMatch[1]);
      } else {
        const bareItem = line.replace(/^\s+-\s+/, "").trim().replace(/^"|"$/g, "");
        if (bareItem) map[currentKey].push(bareItem);
      }
    }
  }

  // Convert arrays back to JSON strings for consistency
  for (const key of Object.keys(map)) {
    if (Array.isArray(map[key])) {
      map[key] = JSON.stringify(map[key]);
    } else if (typeof map[key] === "string") {
      map[key] = map[key].trim();
    }
  }

  return map;
}

/**
 * Rebuild frontmatter text from a key-value map, converting all
 * values to quoted strings (simpler, more consistent format).
 */
function rebuildFrontmatter(frontmatterText, overrides) {
  // Parse current frontmatter
  const fm = parseFrontmatterMap(frontmatterText);

  // Apply overrides
  for (const [key, value] of Object.entries(overrides)) {
    if (value === undefined) continue;
    fm[key] = value;
  }

  // Rebuild
  const lines = [];
  for (const [key, value] of Object.entries(fm)) {
    if (value === null || value === undefined) continue;
    const strVal = String(value);

    // JSON array — output inline even if it contains quotes
    if (/^\[[\s\S]*\]$/.test(strVal.trim())) {
      lines.push(`${key}: ${strVal}`);
    } else if (strVal === "true" || strVal === "false") {
      // Boolean values — unquoted for YAML boolean parsing
      lines.push(`${key}: ${strVal}`);
    } else if (/^\d{4}-\d{2}-\d{2}$/.test(strVal)) {
      // Date value (e.g., 2025-12-01) — output unquoted for YAML date parsing
      lines.push(`${key}: ${strVal}`);
    } else if (strVal.includes('"') || strVal.includes("\n")) {
      // Multi-line or contains quotes — use YAML literal block
      lines.push(`${key}: |`);
      for (const subLine of strVal.split("\n")) {
        lines.push(`  ${subLine}`);
      }
    } else {
      lines.push(`${key}: "${strVal}"`);
    }
  }

  return lines.join("\n");
}

/* ════════════════════════════════════════════════════════════════
   SANITIZATION PASSES
   ════════════════════════════════════════════════════════════════ */

/**
 * Pass 1 — Strip dangling metadata headings.
 * Removes lines like `#### syntaxsql`, `### nvarchar`, `### int`
 * when they appear as standalone headings.
 * Also strips `#### Property`, `#### Value`, `#### Usage` if they
 * appear as isolated stubs (no content after them).
 */
function stripDanglingHeadings(lines) {
  const result = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Strip #### syntaxsql / ### datatype headings
    if (METADATA_HEADING_RE.test(line.trim())) {
      stats.dangling_headings_removed++;
      continue; // skip this line
    }

    // Strip headings that match common ingestion property labels
    // when they have no content after them (empty stub headings)
    const stubHeadingRe = /^#{3,4}\s+(Property|Value|Usage|Date range|Time range|Time zone offset range|Element ranges|Character length|Storage size|Accuracy|Default value|Calendar|User-defined fractional second precision|Time zone offset aware and preservation|Daylight saving aware|Default string literal formats|Default string literal formats \(used|for down-level client\))\s*$/i;
    if (stubHeadingRe.test(line.trim())) {
      // Check if next line is also a heading or blank
      const nextLine = i + 1 < lines.length ? lines[i + 1].trim() : "";
      const nextNextLine = i + 2 < lines.length ? lines[i + 2].trim() : "";
      if (
        nextLine === "" ||
        nextLine.startsWith("#") ||
        nextLine.startsWith("```") ||
        nextNextLine === "" ||
        nextNextLine.startsWith("#")
      ) {
        stats.dangling_headings_removed++;
        continue;
      }
    }

    result.push(line);
  }
  return result;
}

/**
 * Pass 2 — Fix stray single-word code blocks.
 * Converts ```sql\nWORD\n``` to inline `WORD` where WORD is a
 * single identifier, token, or short phrase.
 */
function fixStrayCodeBlocks(content) {
  // Match ```sql ... ``` blocks that contain only a single short line
  return content.replace(
    /```sql\s*\n\s*([A-Za-z][A-Za-z0-9_.#()[\]]{1,60})\s*\n\s*```/g,
    (match, word) => {
      stats.stray_code_blocks_fixed++;
      return "`" + word.trim() + "`";
    }
  );
}

/**
 * Pass 3 — Remove trailing "SQL" lines that are just remnants.
 * Some files have "SQL" on its own line after a paragraph.
 */
function stripStraySqlWords(content) {
  return content.replace(/^\s*SQL\s*$/gm, (match) => {
    stats.stray_code_blocks_fixed++;
    return "";
  });
}

/**
 * Pass 4 — Join fragmented sentences.
 * Heuristic: if a line ends without terminal punctuation and the
 * next line starts with a lowercase letter or open paren, they
 * are part of the same sentence.
 */
function joinFragmentedSentences(lines) {
  const result = [];
  let i = 0;

  while (i < lines.length) {
    let current = lines[i];

    // Skip joining inside code blocks or frontmatter
    if (
      current.trimStart().startsWith("```") ||
      current.trimStart().startsWith("---")
    ) {
      result.push(current);
      i++;
      continue;
    }

    // Look ahead: if this line doesn't end with sentence-ending
    // punctuation and the next line continues the sentence...
    while (i + 1 < lines.length) {
      const next = lines[i + 1];

      // Don't join into code blocks or headings
      if (
        next.trimStart().startsWith("```") ||
        next.trimStart().startsWith("#") ||
        next.trimStart().startsWith("---") ||
        next.trimStart().startsWith(">") ||
        next.trimStart().startsWith("- ") ||
        next.trimStart().startsWith("* ") ||
        next.trimStart().match(/^\d+\.\s/) ||
        next.trimStart().startsWith("|")
      ) {
        break;
      }

      const trimmed = current.trimEnd();
      const nextTrimmed = next.trimStart();

      // If current line ends with terminal punctuation, stop
      if (/[.!?:;]\s*$/.test(trimmed)) break;

      // If next line is blank, stop
      if (nextTrimmed === "") break;

      // If next line starts uppercase in a way that suggests a new sentence
      if (/^[A-Z][a-z]+\s/.test(nextTrimmed) && trimmed.length > 40) break;

      // Join: strip trailing spaces from current, add space, append next
      // But first: if the current line ends with a word and next starts
      // with a word, remove the line break
      if (
        /[a-zA-Z0-9)]$/.test(trimmed) &&
        /^[a-z(]/.test(nextTrimmed)
      ) {
        current = trimmed + " " + nextTrimmed;
        stats.fragmented_sentences_joined++;
        i++;
        continue;
      }

      break;
    }

    result.push(current);
    i++;
  }

  return result;
}

/**
 * Pass 5 — Collapse excessive blank lines.
 */
function collapseBlankLines(lines) {
  const result = [];
  let prevBlank = false;

  for (const line of lines) {
    const isBlank = line.trim() === "";
    if (isBlank && prevBlank) {
      stats.blank_lines_collapsed++;
      continue;
    }
    result.push(line);
    prevBlank = isBlank;
  }

  return result;
}

/**
 * Pass 6 — Fix concatenated column-description salad in frontmatter descriptions.
 *
 * DMVs and catalog views extracted from Microsoft docs often have descriptions
 * that start with a real sentence then dump column metadata:
 *   "Returns a row for each broker connection. ID of the connection. Name of the endpoint. Current state of the connection."
 *
 * This pass truncates the description to the first 1-2 natural-sentence fragments
 * before the column-metadata begins.
 */
function COL_DESC_MARKERS_RE() {
  // These phrases signal that a sentence is describing a column, not the object itself.
  // These are only checked against text that FOLLOWS a sentence break — NOT against the
  // first sentence of a description (which may start with platform prefixes naturally).
  return /^(ID of|Name of|Identifier of|Object identification|The name of|The class of|Date and time|Current state|Possible values|Possible |Value written|Maps to|Is unique|Can be|Related to the value|This view is visible|The item)/i;
}

function fixConcatenatedDescriptions(frontmatter, body) {
  // Fix frontmatter description
  const descMatch = frontmatter.match(/^description:\s*"(.+)"\s*$/m);
  if (descMatch) {
    let original = descMatch[1];

    // First, strip embedded boilerplate from the description
    const platRe = /^(?:Azure SQL Database|Azure SQL Managed Instance|SQL Server|SQL database in Microsoft Fabric|Analytics Platform System \(PDW\)|Azure Synapse Analytics)(?:\s+(?:Azure SQL Database|Azure SQL Managed Instance|SQL Server|SQL database in Microsoft Fabric|Analytics Platform System \(PDW\)|Azure Synapse Analytics))*\s*/i;
    const stripped = original
      .replace(platRe, "")  // Strip platform list at start
      .replace(/\s*Transact-SQL syntax conventions\s*/gi, " ")
      .replace(/Article\s*•\s*\d{2}\/\d{2}\/\d{4}\s*/gi, "")
      .replace(/\s*Last updated on\s+\d{1,2}\/\d{1,2}\/\d{4}\s*/gi, " ")
      .replace(/\s*Related content[\s\S]*$/gi, "")
      .replace(/\s*For more information about SQL Server Audit\s*/gi, " ")
      .replace(/  +/g, " ")
      .trim();

    // Always write back after boilerplate stripping (even if truncation is a no-op)
    if (stripped !== original) {
      frontmatter = frontmatter.replace(
        /^description:\s*".+"/m,
        `description: "${stripped}"`
      );
    }

    // Then apply column-marker truncation on the stripped version
    const cleaned = truncateAfterFirstSentence(stripped);
    if (cleaned !== stripped) {
      stats.fragmented_sentences_joined++;
      frontmatter = frontmatter.replace(
        /^description:\s*".+"/m,
        `description: "${cleaned}"`
      );
    }
  }

  // Fix body: remove column-description-salad from the Description section.
  // Unlike the line-level check below, this works at the sentence level so it
  // catches column metadata that's all in one paragraph (the common case).
  const bodyLines = body.split("\n");
  const fixedLines = [];
  let inDescription = false;

  for (let i = 0; i < bodyLines.length; i++) {
    const line = bodyLines[i];

    // Track when we're in the ## Description section
    if (/^## Description\s*$/i.test(line.trim())) {
      inDescription = true;
      fixedLines.push(line);
      continue;
    }

    // Stop at next heading
    if (inDescription && /^##\s/.test(line.trim())) {
      inDescription = false;
      fixedLines.push(line);
      continue;
    }

    if (inDescription) {
      const trimmed = line.trim();
      if (trimmed === "") {
        // Keep blank lines
        fixedLines.push(line);
        continue;
      }
      // Apply sentence-level truncation to the entire Description paragraph
      const cleaned = truncateAfterColumnMeta(trimmed);
      fixedLines.push(cleaned);
    } else {
      fixedLines.push(line);
    }
  }

  body = fixedLines.join("\n");
  return { frontmatter, body };
}

function truncateAfterFirstSentence(text) {
  // Split into sentences (rough heuristic: text before . followed by space and capital letter or column marker)
  const sentences = [];
  let current = "";
  let i = 0;

  while (i < text.length) {
    current += text[i];
    if (text[i] === "." && (i + 1 >= text.length || (i + 1 < text.length && text[i + 1] === " "))) {
      // Check if next starts with a column marker
      const remainder = text.slice(i + 1).trim();
      if (remainder === "") {
        current += remainder;
        sentences.push(current.trim());
        current = "";
        break;
      }
      // Check if the next sentence starts with a column-description marker
      if (COL_DESC_MARKERS_RE().test(remainder)) {
        // We've found the first column-description marker after a sentence
        // Keep only up to this point
        if (current.trim()) {
          sentences.push(current.trim());
        }
        current = "";
        break;
      }
      // Otherwise, this is a normal sentence continuation
      if (current.trim()) {
        sentences.push(current.trim());
      }
      current = "";
      i++;
      continue;
    }
    i++;
  }

  // If we have leftover text and it doesn't start with column markers
  if (current.trim() && !COL_DESC_MARKERS_RE().test(current.trim())) {
    sentences.push(current.trim());
  }

  // Keep only up to where the main loop broke on a column marker (already handled above).
  // No arbitrary sentence limit — clean descriptions are kept in full.
  const keep = [];
  for (let s = 0; s < sentences.length; s++) {
    const sentence = sentences[s].replace(/^\.\s*/, "").trim();
    if (!sentence) continue;
    // Skip if it looks like truncated content (ends mid-word mid-sentence)
    if (/ [a-z]{2,5}$/.test(sentence) && !/[.!?:;]$/.test(sentence)) continue;
    keep.push(sentence);
  }

  return keep.join(" ");
}

/**
 * Pass 7 — Check if file is an empty stub (only frontmatter + headings/no content).
 * Returns true if the file should be deleted.
 */
function isEmptyStub(bodyLines) {
  const textLines = bodyLines.filter(
    (l) => l.trim() !== "" && !l.trimStart().startsWith("#")
  );
  const codeLines = bodyLines.filter((l) => l.trimStart().startsWith("```"));
  const headingLines = bodyLines.filter((l) => l.trimStart().startsWith("#"));

  // If no text lines and no code blocks, but has headings — it's a stub
  if (textLines.length === 0 && codeLines.length === 0 && headingLines.length > 0) {
    return true;
  }

  // If only very short text fragments
  if (textLines.join("").trim().length < 30 && codeLines.length === 0) {
    return true;
  }

  return false;
}

function truncateAfterColumnMeta(text) {
  // Like truncateAfterFirstSentence, but keeps ALL clean sentences and only
  // stops at a column marker (no arbitrary sentence limit). Used for body content.
  const sentences = [];
  let current = "";
  let i = 0;

  while (i < text.length) {
    current += text[i];
    if (text[i] === "." && (i + 1 >= text.length || (i + 1 < text.length && text[i + 1] === " "))) {
      const remainder = text.slice(i + 1).trim();
      if (remainder === "") {
        sentences.push((current + remainder).trim());
        current = "";
        break;
      }
      if (COL_DESC_MARKERS_RE().test(remainder)) {
        if (current.trim()) sentences.push(current.trim());
        current = "";
        break;
      }
      if (current.trim()) sentences.push(current.trim());
      current = "";
      i++;
      continue;
    }
    i++;
  }

  if (current.trim() && !COL_DESC_MARKERS_RE().test(current.trim())) {
    sentences.push(current.trim());
  }

  const keep = [];
  for (const s of sentences) {
    const sentence = s.replace(/^\.\s*/, "").trim();
    if (!sentence) continue;
    if (/ [a-z]{2,5}$/.test(sentence) && !/[.!?:;]$/.test(sentence)) continue;
    keep.push(sentence);
  }

  return keep.join(" ");
}

/**
 * Strip Microsoft Docs boilerplate artifacts from body content.
 * Operates on text within each section, removing patterns that appear mid-paragraph.
 */
function stripBoilerplate(body) {
  // First pass: strip standalone lines
  let lines = body.split("\n");
  const result = [];
  let skipUntilHeading = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // Strip standalone "Article" (Microsoft Docs header artifact)
    if (/^Article$/i.test(trimmed)) continue;

    // Strip standalone bullet point "•"
    if (/^•$/.test(trimmed)) continue;

    // Strip standalone date lines (e.g., "02/28/2023")
    if (/^\d{2}\/\d{2}\/\d{4}$/.test(trimmed)) continue;

    // Strip "Summarize this article for me" (AI summary headers)
    if (/^Summarize this article for me/i.test(trimmed)) continue;

    // Strip lines that start with "Applies to:"
    if (/^Applies to:/i.test(trimmed)) {
      while (i < lines.length) {
        const next = lines[i + 1]?.trim() || "";
        if (!next || /^[A-Z]/.test(next) || /^##/.test(next)) break;
        i++;
      }
      continue;
    }

    // Strip "Transact-SQL syntax conventions" standalone lines
    if (/^Transact-SQL syntax conventions/i.test(trimmed)) continue;

    // Strip "syntaxsql" standalone remnants
    if (/^syntaxsql$/i.test(trimmed)) continue;

    // Strip "Last updated on ..." lines
    if (/^Last updated on\s+\d{1,2}\/\d{1,2}\/\d{4}/i.test(trimmed)) continue;

    // Strip "Related content" sections
    if (/^Related content/i.test(trimmed)) {
      skipUntilHeading = true;
      continue;
    }
    if (skipUntilHeading) {
      if (/^##/.test(trimmed)) {
        skipUntilHeading = false;
        result.push(line);
      }
      continue;
    }

    result.push(line);
  }

  body = result.join("\n");

  // Second pass: strip embedded boilerplate within paragraphs (text-level)
  body = body.replace(/(?:\.\s*)?Applies to:[\s\S]*?(?:SQL database in Microsoft Fabric|Azure SQL Managed Instance|Analytics Platform System \(PDW\)|\.)\s*/gi, (match) => {
    // If it starts with ". " keep the period, otherwise remove entirely
    if (match.startsWith(". ")) return ". ";
    if (match.startsWith(".")) return ". ";
    return "";
  });

  body = body.replace(/\s*Transact-SQL syntax conventions\s*/gi, " ");

  body = body.replace(/\s*Last updated on\s+\d{1,2}\/\d{1,2}\/\d{4}\s*/gi, " ");

  body = body.replace(/\s*Related content[\s\S]*?(?=\n##|\n$|$)/gi, "");

  // Strip inline compound platform lists (Microsoft concatenation artifacts)
  body = body.replace(
    /Azure SQL Database\s+Azure SQL Managed Instance\s*/gi,
    ""
  );
  body = body.replace(
    /SQL analytics endpoint in Microsoft Fabric\s+Warehouse in Microsoft Fabric\s*/gi,
    ""
  );
  body = body.replace(
    /Azure Synapse Analytics\s+Analytics Platform System \(PDW\)\s*/gi,
    ""
  );
  body = body.replace(
    /Azure SQL Database\s+Azure SQL Managed Instance\s+SQL database in Microsoft Fabric\s*/gi,
    ""
  );
  body = body.replace(
    /SQL database in Microsoft Fabric\s+Azure SQL Database\s+Azure SQL Managed Instance\s*/gi,
    ""
  );

  // Strip orphaned platform names at line start (no "Applies to:" prefix).
  // Line-by-line to avoid consuming newlines.
  const platformNames = [
    "Azure SQL Database", "Azure SQL Managed Instance",
    "SQL Server", "SQL database in Microsoft Fabric",
    "Analytics Platform System (PDW)", "Azure Synapse Analytics"
  ];
  const platformRe = new RegExp(
    "^(?:" + platformNames.join("|") + ")" +
    "(?:\\s+(?:" + platformNames.join("|") + "))*\\s*",
    "gi"
  );

  const platformFix = body.split("\n").map((line) => {
    // Only apply to lines that start with platform names (not headings)
    if (/^##/.test(line.trim())) return line;
    return line.replace(platformRe, "");
  }).join("\n");

  body = platformFix;

  // Clean up orphaned prefixes mid-sentence
  body = body.replace(/ \. /g, ". ");

  // Clean up double spaces
  body = body.replace(/  +/g, " ");
  // Clean up double periods
  body = body.replace(/\.\.+/g, ".");
  // Clean up space before period
  body = body.replace(/\s+\./g, ".");

  return body;
}

/**
 * Replace a specific frontmatter field value using regex.
 * Works for both `key: "value"` and `key: |` literal block formats.
 * Preserves all other fields exactly as-is.
 */
function replaceFrontmatterField(frontmatter, key, newValue) {
  // Handle description: "..." (quoted string)
  const quotedRe = new RegExp(`^(${key}:\\s*)"([^"]*)"\\s*$`, "m");
  if (quotedRe.test(frontmatter)) {
    return frontmatter.replace(quotedRe, `$1"${newValue}"`);
  }

  // Handle description: | (YAML literal block)
  const literalBlockRe = new RegExp(
    `^(${key}:\\s*\\|)\\s*\\n((?:\\s{2}.*\\n?)*)`,
    "m"
  );
  if (literalBlockRe.test(frontmatter)) {
    // Replace literal block with inline quoted value
    return frontmatter.replace(literalBlockRe, `$1 "${newValue}"`);
  }

  // Handle key: bare value (unquoted)
  const bareRe = new RegExp(`^(${key}:\\s*)(\\S.*)$`, "m");
  if (bareRe.test(frontmatter)) {
    // Check if the current value is already a JSON array
    const match = frontmatter.match(bareRe);
    if (match && /^\[/.test(newValue)) {
      // JSON array — output unquoted
      return frontmatter.replace(bareRe, `$1${newValue}`);
    }
    return frontmatter.replace(bareRe, `$1"${newValue}"`);
  }

  return frontmatter;
}

/**
 * Replace a YAML list-format field (tags:\n  - "item") with inline JSON array.
 */
function replaceYamlListWithJson(frontmatter, key, jsonArray) {
  // Match: key:\n  - "item1"\n  - "item2"
  const listRe = new RegExp(
    `^(${key}:)\\s*\\n((?:\\s+-\\s+"[^"]*"\\n?)*)`,
    "m"
  );
  if (listRe.test(frontmatter)) {
    return frontmatter.replace(listRe, `$1 ${jsonArray}`);
  }
  return frontmatter;
}

/**
 * Pass 8 — Clean frontmatter description field (YAML literal blocks + quoted).
 * Strips boilerplate ("Article", "Applies to:", dates, platform names, etc.)
 * from the description field in the frontmatter, regardless of format.
 */
function cleanFrontmatterDescription(frontmatter) {
  // Extract description value directly from frontmatter text
  let desc = "";

  // Try quoted format: description: "..."
  const quotedMatch = frontmatter.match(/^description:\s*"([^"]*)"\s*$/m);
  if (quotedMatch) {
    desc = quotedMatch[1];
  } else {
    // Try literal block format: description: |\n  ...
    const literalMatch = frontmatter.match(/^description:\s*\|\s*\n((?:\s{2}.*\n?)*)/m);
    if (literalMatch) {
      desc = literalMatch[1]
        .split("\n")
        .map((l) => l.replace(/^\s{2}/, ""))
        .join("\n")
        .trim();
    }
  }

  if (!desc || desc.trim() === "") return frontmatter;

  // Clean the description
  let cleaned = desc;

  // Remove "Article" + bullet + date pattern at the start
  cleaned = cleaned.replace(/^Article\s*\n\s*•?\s*\n?\s*\d{2}\/\d{2}\/\d{4}\s*\n*/i, "");

  // Remove "Applies to:" and any content until the next non-blank, non-list line
  cleaned = cleaned.replace(/Applies to:[\s\S]*?(?=\n\s*[A-Za-z]|\n\n|$)/i, "");

  // Remove standalone platform name lines (with optional leading whitespace)
  const platformNames = [
    "Azure SQL Database", "Azure SQL Managed Instance",
    "SQL Server", "SQL database in Microsoft Fabric",
    "Analytics Platform System (PDW)", "Azure Synapse Analytics",
    "Parallel Data Warehouse"
  ];
  for (const name of platformNames) {
    const escaped = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const reIndented = new RegExp(`^\\s*${escaped}\\s*$`, "gim");
    cleaned = cleaned.replace(reIndented, "");
  }

  // Remove "Summarize this article for me" (Microsoft AI-generated summary header)
  cleaned = cleaned.replace(/^Summarize this article for me\s*/i, "");

  // Remove "syntaxsql" remnants
  cleaned = cleaned.replace(/^syntaxsql\s*$/gim, "");

  // Remove "Transact-SQL syntax conventions"
  cleaned = cleaned.replace(/Transact-SQL syntax conventions/gi, "");

  // Remove "Last updated on ..."
  cleaned = cleaned.replace(/Last updated on\s+\d{1,2}\/\d{1,2}\/\d{4}\s*/gi, "");

  // Remove "Related content" and everything after it
  cleaned = cleaned.replace(/Related content[\s\S]*$/gi, "");

  // Clean up the actual description: flatten newlines, remove excessive whitespace
  cleaned = cleaned.replace(/\n+/g, " ").replace(/\s+/g, " ").trim();

  // If description is now empty, keep original
  if (!cleaned || cleaned.length < 5) {
    return frontmatter;
  }

  // Only update if cleaned version is different
  const originalFlat = desc.replace(/\n+/g, " ").replace(/\s+/g, " ").trim();
  if (cleaned === originalFlat) {
    return frontmatter;
  }

  // Replace the description field using targeted regex
  return replaceFrontmatterField(frontmatter, "description", cleaned);
}

/**
 * Pass 9 — Normalize tags to JSON array format.
 */
function normalizeTags(frontmatter) {
  // Try to extract tags value from frontmatter
  let tags = "";
  let isLiteralBlock = false;
  let isYamlList = false;

  // Check for YAML list format: tags:\n  - "item"
  if (/^tags:\s*\n\s+-/m.test(frontmatter)) {
    isYamlList = true;
    // Extract the list items
    const listMatch = frontmatter.match(/^tags:\s*\n((?:\s+-[^\n]*\n?)*)/m);
    if (listMatch) {
      tags = listMatch[1].trim();
    }
  } else {
    // Check for literal block: tags: |\n  [...]
    const literalMatch = frontmatter.match(/^tags:\s*\|\s*\n\s+(\[.*?\])\s*$/m);
    if (literalMatch) {
      isLiteralBlock = true;
      tags = literalMatch[1];
    } else {
      // Check for inline: tags: [...]
      const inlineMatch = frontmatter.match(/^tags:\s*(\[.*?\])\s*$/m);
      if (inlineMatch) {
        tags = inlineMatch[1];
        // Already inline JSON — nothing to do
        try {
          const parsed = JSON.parse(tags);
          if (Array.isArray(parsed)) return frontmatter;
        } catch {}
      }
    }
  }

  if (!tags) return frontmatter;

  // If it's a YAML list, convert items to JSON array
  if (isYamlList) {
    const items = [];
    for (const match of tags.matchAll(/-\s+"([^"]+)"/g)) {
      items.push(match[1]);
    }
    if (items.length > 0) {
      return replaceYamlListWithJson(frontmatter, "tags", JSON.stringify(items));
    }
  }

  // If it's a literal block with JSON, replace inline
  if (isLiteralBlock) {
    try {
      const parsed = JSON.parse(tags);
      if (Array.isArray(parsed)) {
        return replaceFrontmatterField(frontmatter, "tags", JSON.stringify(parsed));
      }
    } catch {}
  }

  return frontmatter;
}

/* ════════════════════════════════════════════════════════════════

/* ════════════════════════════════════════════════════════════════
   MAIN PROCESSOR
   ════════════════════════════════════════════════════════════════ */

function processFile(filePath) {
  const relativePath = path.relative(CONTENT_ROOT, filePath);
  let content;

  try {
    content = fs.readFileSync(filePath, "utf-8");
  } catch (err) {
    stats.errors.push(`Cannot read ${relativePath}: ${err.message}`);
    return;
  }

  stats.files_scanned++;

  // Separate frontmatter and body
  const frontmatterMatch = content.match(/^---\n[\s\S]*?\n---\n/);
  if (!frontmatterMatch) {
    // No frontmatter — skip
    return;
  }

  let frontmatter = frontmatterMatch[0];
  let body = content.slice(frontmatter.length);

  // ── Apply passes ──

  // 0. Clean frontmatter description (handles YAML literal blocks & quoted)
  const cleanedFrontmatter1 = cleanFrontmatterDescription(frontmatter);
  if (cleanedFrontmatter1 !== frontmatter) {
    frontmatter = cleanedFrontmatter1;
  }

  // 0a. Normalize tags to JSON array format
  const cleanedFrontmatter2 = normalizeTags(frontmatter);
  if (cleanedFrontmatter2 !== frontmatter) {
    frontmatter = cleanedFrontmatter2;
  }

  // 0b. Strip Microsoft Docs boilerplate (Applies to, syntax conventions, etc.)
  body = stripBoilerplate(body);

  // 0c. Fix concatenated column-description salad (DMVs, catalog-views)
  const descResult = fixConcatenatedDescriptions(frontmatter, body);
  frontmatter = descResult.frontmatter;
  body = descResult.body;

  // 2. Fix stray code blocks
  body = fixStrayCodeBlocks(body);

  // 3. Strip stray "SQL" words
  body = stripStraySqlWords(body);

  // Convert body back to lines for line-based passes
  let bodyLines = body.split("\n");

  // 1. Strip dangling headings
  const linesAfterP1 = stripDanglingHeadings(bodyLines);

  // 4. Join fragmented sentences
  const linesAfterP4 = joinFragmentedSentences(linesAfterP1);

  // 5. Collapse blank lines
  const finalLines = collapseBlankLines(linesAfterP4);

  const newBody = finalLines.join("\n").trimEnd() + "\n";
  const newContent = frontmatter + newBody;

  // 6. Check for empty stub
  if (isEmptyStub(finalLines)) {
    if (DRY_RUN) {
      console.log(`  [STUB]   ${relativePath} — would delete (empty stub)`);
    } else {
      try {
        fs.unlinkSync(filePath);
        stats.empty_stubs_deleted++;
        console.log(`  [DELETE] ${relativePath} — deleted empty stub`);
      } catch (err) {
        stats.errors.push(`Cannot delete ${relativePath}: ${err.message}`);
      }
    }
    return;
  }

  // Write if changed
  if (newContent !== content) {
    if (DRY_RUN) {
      console.log(`  [MODIFY] ${relativePath} — would sanitize`);
    } else {
      try {
        fs.writeFileSync(filePath, newContent, "utf-8");
        stats.files_modified++;
        console.log(`  [OK]     ${relativePath} — sanitized`);
      } catch (err) {
        stats.errors.push(`Cannot write ${relativePath}: ${err.message}`);
      }
    }
  }
}

function processCollection(collectionDir) {
  const dirPath = path.join(CONTENT_ROOT, collectionDir);
  if (!fs.existsSync(dirPath)) {
    console.warn(`  [SKIP]   Collection "${collectionDir}" does not exist`);
    return;
  }

  const files = fs.readdirSync(dirPath).filter((f) => f.endsWith(".md"));
  console.log(`\n📂 ${collectionDir} (${files.length} files)`);

  for (const file of files) {
    processFile(path.join(dirPath, file));
  }
}

/* ════════════════════════════════════════════════════════════════
   ENTRY POINT
   ════════════════════════════════════════════════════════════════ */

function main() {
  console.log("╔══════════════════════════════════════════════╗");
  console.log("║   SQLKRAFT — Content Sanitization Engine    ║");
  console.log(`║   ${DRY_RUN ? "DRY RUN — no changes written" : "LIVE — writing changes"}       ║`);
  console.log("╚══════════════════════════════════════════════╝\n");

  // Get all collection directories
  const allCollections = fs.readdirSync(CONTENT_ROOT).filter((d) => {
    const dirPath = path.join(CONTENT_ROOT, d);
    return fs.statSync(dirPath).isDirectory() && !d.startsWith("trash") && !d.startsWith(".");
  });

  const collections = COLLECTIONS_FILTER
    ? allCollections.filter((c) => COLLECTIONS_FILTER.includes(c))
    : allCollections;

  for (const collection of collections) {
    processCollection(collection);
  }

  // ── Summary ──
  console.log("\n╔══════════════════════════════════════════════╗");
  console.log("║                  SUMMARY                    ║");
  console.log("╚══════════════════════════════════════════════╝");
  console.log(`  Files scanned:              ${stats.files_scanned}`);
  console.log(`  Files modified:             ${stats.files_modified}`);
  console.log(`  Empty stubs deleted:        ${stats.empty_stubs_deleted}`);
  console.log(`  Dangling headings removed:  ${stats.dangling_headings_removed}`);
  console.log(`  Stray code blocks fixed:    ${stats.stray_code_blocks_fixed}`);
  console.log(`  Fragmented sentences joined:${stats.fragmented_sentences_joined}`);
  console.log(`  Blank lines collapsed:      ${stats.blank_lines_collapsed}`);

  if (stats.errors.length > 0) {
    console.log(`\n  ⚠️  Errors: ${stats.errors.length}`);
    for (const err of stats.errors.slice(0, 5)) {
      console.log(`      ${err}`);
    }
  }

  console.log(`\n  ${DRY_RUN ? "Run without --dry-run to apply changes" : "Done."}`);
}

main();
