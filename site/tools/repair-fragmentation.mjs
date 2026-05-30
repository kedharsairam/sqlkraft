/**
 * repair-fragmentation.mjs
 * 
 * Repairs line fragmentation in tsql-reference content files caused by 
 * HTML-to-Markdown scraping that exploded tables and prose into individual 
 * lines with heading markers.
 *
 * Patterns handled:
 *   A. Table detonation — data flattened into #### heading lines
 *   B. Prose atomization — sentences broken across blank-line-separated chunks
 *   C. Type/property lists — flat list of names as heading lines
 *   D. Stray artifacts — "Expand table", "Last updated on...", etc.
 *
 * Usage:
 *   node tools/repair-fragmentation.mjs             # dry-run (report only)
 *   node tools/repair-fragmentation.mjs --fix        # apply fixes
 *   node tools/repair-fragmentation.mjs --file foo.md # single file
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const contentDir = path.resolve(__dirname, "../src/content/tsql-reference");

// ── Configuration ───────────────────────────────────────────────────────────

const STRAY_PATTERNS = [
  /^Expand table\s*$/i,
  /^Last updated on.*$/i,
  /Related content/i,
  /^Summarize this article for me\s*$/i,
  /^##\s+RETURNS\s*$/,               // stray heading inside keyword lists (all-caps = not a real section)
];

// Lines matching these are preserved as-is (structural markdown)
function isStructuralLine(raw, trimmed) {
  if (/^```/.test(trimmed)) return true;          // code fence
  if (/^\|/.test(trimmed)) return true;           // table row
  if (/^(\s*[-*+]|\s*\d+\.)\s/.test(trimmed)) return true; // list item
  if (/^---+$/.test(trimmed) && !raw.startsWith("---")) return true; // HR
  return false;
}

// Lines matching these are stray artifacts to remove
function isStrayLine(trimmed) {
  return STRAY_PATTERNS.some(p => p.test(trimmed));
}

// Lines matching these are "document structure" marks to remove
function isDocStructureMark(trimmed) {
  return /^####\s*syntaxsql\s*$/i.test(trimmed);
}

// Extract heading level from a line
function getHeadingLevel(trimmed) {
  const m = trimmed.match(/^(#{1,6})\s/);
  return m ? m[1].length : 0;
}

// Get heading content (text after ###)
function getHeadingContent(trimmed) {
  return trimmed.replace(/^#{1,6}\s+/, "").trim();
}

// Count words in a string
function wordCount(s) {
  const cleaned = s.replace(/[#*`_\[\]()|]/g, " ").trim();
  return cleaned ? cleaned.split(/\s+/).length : 0;
}

// ── Repair Logic ────────────────────────────────────────────────────────────

function repairFile(content) {
  const rawLines = content.split("\n");
  // Preserve trailing newline behavior
  const endsWithNewline = content.endsWith("\n");

  const pass1 = removeStrayLines(rawLines);
  const pass2 = repairShortHeadings(pass1);
  const pass3 = cleanupBlankLines(pass2);
  const pass4 = joinFragmentedProse(pass3);
  const pass5 = removeExcessBlankLines(pass4);
  const pass6 = fixFrontmatterDescription(pass5);
  const pass7 = removeDocStructureMarks(pass6);

  let result = pass7.join("\n");
  if (endsWithNewline && !result.endsWith("\n")) result += "\n";
  return result;
}

// ── Pass 1: Remove stray/artifact lines ─────────────────────────────────────

function removeStrayLines(lines) {
  return lines.filter((line, i) => {
    const trimmed = line.trim();
    
    // Always keep frontmatter
    if (line.startsWith("---") && i < 15) return true;
    if (trimmed.startsWith("name:") || trimmed.startsWith("title:") || 
        trimmed.startsWith("category:") || trimmed.startsWith("description:") ||
        trimmed.startsWith("tags:") || trimmed.startsWith("pubDate:")) return true;
    
    if (isStrayLine(trimmed)) return false;
    return true;
  });
}

// ── Pass 2: Repair short heading lines ─────────────────────────────────────

function repairShortHeadings(lines) {
  const result = [];
  let inCodeBlock = false;

  for (const raw of lines) {
    const trimmed = raw.trim();

    // Track code blocks
    if (/^```/.test(trimmed)) {
      inCodeBlock = !inCodeBlock;
      result.push(raw);
      continue;
    }

    if (inCodeBlock) {
      result.push(raw);
      continue;
    }

    // Skip empty lines (handled in join pass)
    if (trimmed === "") {
      result.push(raw);
      continue;
    }

    // Skip structural lines
    if (isStructuralLine(raw, trimmed)) {
      result.push(raw);
      continue;
    }

    // Check if this is a heading with short content (likely a fragment)
    const hl = getHeadingLevel(trimmed);
    if (hl > 0) {
      const content = getHeadingContent(trimmed);
      const wc = wordCount(content);

      // Always preserve level-1 and level-2 headings (they're real section headings)
      if (hl <= 2) {
        result.push(raw);
      }
      // For level-3 and above: strip if short content (likely a table fragment)
      else if (wc <= 6 && content.length <= 45) {
        // This is likely a fragment, not a real heading
        // Strip the heading markers and add as plain text
        const indent = raw.match(/^\s*/)[0];
        result.push(indent + content);
      } else {
        // Proper heading — preserve
        result.push(raw);
      }
    } else {
      result.push(raw);
    }
  }

  return result;
}

// ── Pass 3: Clean up blank lines ────────────────────────────────────────────
// Conservative approach: do NOT join short lines into paragraphs.
// Simply remove extraneous blank lines while preserving structural separation.
// The main value from this pass is to collapse multiple blank lines into one.

function cleanupBlankLines(lines) {
  const result = [];
  let inCodeBlock = false;

  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i];
    const trimmed = raw.trim();
    const stripped = raw.replace(/\s+$/, "");

    // Track code blocks
    if (/^```/.test(trimmed)) {
      inCodeBlock = !inCodeBlock;
      result.push(stripped);
      continue;
    }

    if (inCodeBlock) {
      result.push(stripped);
      continue;
    }

    // Skip empty lines that follow other empty lines (collapse multiples)
    if (trimmed === "") {
      if (i > 0 && lines[i - 1].trim() === "") continue;
      result.push("");
      continue;
    }

    result.push(stripped);
  }

  // Remove leading blank lines in body
  while (result.length > 0 && result[0] === "") result.shift();
  // Remove trailing blank line if present
  while (result.length > 0 && result[result.length - 1] === "") result.pop();

  return result;
}

// ── Pass 4: Join clearly fragmented prose ───────────────────────────────────
// This pass is CONSERVATIVE — it only joins lines when it's very clear they
// are sentence fragments that belong together (e.g., line ends with comma
// and next line continues, or lineA ends with a connecting word).
// It does NOT join keyword lists, table data, or standalone items.

/**
 * Check if a line is a "continuation" line (starts lowercase or with connecting word).
 */
function isContinuationLine(line) {
  const t = line.trim();
  if (!t) return false;
  // Starts with lowercase letter (excluding bullet items, numbers)
  if (/^[a-z]/.test(t)) return true;
  return false;
}

/**
 * Check if a line ENDS in a way that expects continuation.
 */
function hasContinuationMarker(line) {
  const t = line.trim();
  if (!t) return false;
  // Ends with comma, semicolon, colon — clearly should continue
  if (/[,;:]$/.test(t)) return true;
  // Ends with a connecting word (like "the", "a", "an", "for", "with", "of", "on", "to", "and")
  if (/\s+(the|a|an|for|with|of|on|to|and|or|but|in|by|as|is|at)$/i.test(t)) return true;
  return false;
}

/**
 * Check if a line looks like a standalone item (keyword, type name, property).
 * These should NOT be joined with neighboring lines.
 * 
 * Rules:
 * - All-caps words (2+ chars) that are not common English → standalone (SQL keywords)
 * - Title-case words that look like property names → standalone
 * - Common sentence-starting words ("The", "This", "For") → NOT standalone
 * - Mixed-case words that could be normal text → NOT standalone
 */
function isStandaloneItem(line) {
  const t = line.trim();
  if (!t) return false;
  const words = t.split(/\s+/);

  // Punctuation-only lines (like `,` or `.`) are NOT standalone
  if (words.every(w => /^[^a-zA-Z0-9]+$/.test(w))) return false;

  // Common English sentence-starting words — these are NOT standalone items
  const sentenceStarters = new Set([
    "the", "this", "that", "these", "those", "for", "with", "from", "into",
    "when", "where", "which", "what", "why", "how", "note", "see", "also",
    "function", "value", "type", "name", "applies", "number", "each", "every",
    "some", "any", "all", "both", "such", "more", "most", "only", "other",
    "same", "than", "after", "before", "between", "under", "over", "through",
    "during", "within", "about", "above", "across", "against", "along", "among",
    "around", "using", "because", "behind", "below", "beneath", "beyond",
    "but", "by", "though", "although", "while", "since", "until", "unless",
    "once", "if", "then", "else", "return", "returns",
  ]);

  // ALL-CAPS words (2+ chars, all uppercase, possibly with digits/underscore)
  // These are SQL keywords → standalone
  const allCapsPattern = /^[A-Z][A-Z0-9_]+$/;
  if (words.length <= 3 && words.every(w => allCapsPattern.test(w.replace(/^[(\[]/, "").replace(/[)\]!?.,;:]$/, "")))) {
    return true;
  }

  // Single common type names like int, varchar, etc. → standalone
  const typeNames = new Set([
    "int", "bigint", "smallint", "tinyint", "bit", "decimal", "numeric",
    "money", "smallmoney", "float", "real",
    "char", "varchar", "nchar", "nvarchar", "text", "ntext",
    "binary", "varbinary", "image", "cursor", "table", "xml",
    "datetime", "smalldatetime", "date", "time", "datetime2", "datetimeoffset",
    "rowversion", "timestamp", "uniqueidentifier", "sql_variant",
    "hierarchyid", "geometry", "geography",
    "varbinary(max)", "varchar(max)", "nvarchar(max)", "varbinary(max)",
  ]);
  if (words.length <= 2 && words.every(w => typeNames.has(w.toLowerCase().replace(/[()]/g, "")))) {
    return true;
  }

  // Title-case property names (like "BadPasswordCount", "DefaultDatabase")
  // These start with uppercase and have mixed case → standalone
  // BUT exclude sentence-starting English words
  if (words.length <= 2) {
    const firstWordClean = words[0].replace(/^[(\[]/, "");
    const isTitleCase = /^[A-Z][a-z]/.test(firstWordClean);
    const startsLikeSentence = sentenceStarters.has(firstWordClean.toLowerCase());
    if (isTitleCase && !startsLikeSentence) return true;
  }

  return false;
}

function joinFragmentedProse(lines) {
  const result = [];
  let inCodeBlock = false;
  let i = 0;

  while (i < lines.length) {
    const raw = lines[i];
    const trimmed = raw.trim();

    // Track code blocks
    if (/^```/.test(trimmed)) {
      inCodeBlock = !inCodeBlock;
      result.push(raw);
      i++;
      continue;
    }

    if (inCodeBlock) {
      result.push(raw);
      i++;
      continue;
    }

    // Empty line — preserve
    if (trimmed === "") {
      result.push("");
      i++;
      continue;
    }

    // YAML frontmatter lines — preserve (word: value pattern)
    if (/^[a-z]+:\s/.test(trimmed) || trimmed === "---") {
      result.push(raw);
      i++;
      continue;
    }

    // Structural elements — preserve
    if (isStructuralLine(raw, trimmed)) {
      result.push(raw);
      i++;
      continue;
    }

    // Headings — preserve
    if (/^#{1,6}\s/.test(trimmed)) {
      result.push(raw);
      i++;
      continue;
    }

    // Check for fragmented prose pattern: a short line followed by continuation
    // Pattern 1: line ends with comma/connector, next non-blank starts lowercase
    // Pattern 2: line is short, next non-blank starts lowercase (sentence broken across lines)

    if (hasContinuationMarker(trimmed)) {
      // This line expects continuation — look ahead for it
      let nextIdx = i + 1;
      let collected = [trimmed];
      
      while (nextIdx < lines.length) {
        const nextLine = lines[nextIdx].trim();
        if (nextLine === "") {
          // Skip blank lines between fragments
          nextIdx++;
          continue;
        }
        // If next line is continuation (starts lowercase) or has its own continuation marker
        if (isContinuationLine(nextLine) || isStandaloneItem(nextLine)) {
          // Check: if next line is a standalone item and current line is also standalone, DON'T join
          if (isStandaloneItem(trimmed) && isStandaloneItem(nextLine)) {
            break;
          }
          collected.push(nextLine);
          nextIdx++;
          // If the collected line ends with a continuation marker, keep going
          if (hasContinuationMarker(nextLine)) {
            continue;
          }
          break;
        }
        break;
      }

      // If we collected more than just the original line, join them
      if (collected.length > 1) {
        const joined = collected.join(" ")
          .replace(/\s{2,}/g, " ")
          .replace(/\s+\./g, ".")
          .replace(/\s+,/g, ",")
          .replace(/\s+;/g, ";")
          .replace(/\s+:/g, ":")
          .replace(/\(\s+/g, "(")
          .replace(/\s+\)/g, ")")
          .trim();
        result.push(joined);
        i = nextIdx;
        continue;
      }
    }

    // Pattern 2: lineA ends mid-sentence (no period), next line starts lowercase
    if (!/[.!?]$/.test(trimmed) && !isStandaloneItem(trimmed)) {
      let nextIdx = i + 1;
      // Skip blank lines
      while (nextIdx < lines.length && lines[nextIdx].trim() === "") nextIdx++;
      if (nextIdx < lines.length) {
        const nextLine = lines[nextIdx].trim();
        if (isContinuationLine(nextLine) && !isStandaloneItem(nextLine)) {
          // Join just these two lines (no cascading)
          result.push((trimmed + " " + nextLine.trim())
            .replace(/\s{2,}/g, " ")
            .replace(/\s+\./g, ".")
            .replace(/\s+,/g, ",")
            .replace(/\s+;/g, ";")
            .replace(/\s+:/g, ":")
            .replace(/\(\s+/g, "(")
            .replace(/\s+\)/g, ")")
            .trim());
          i = nextIdx + 1; // skip past blank lines + joined line
          continue; // continues outer while(i < lines.length) loop
        }
      }
    }

    // Default: preserve the line as-is
    result.push(raw);
    i++;
  }

  return result;
}

// ── Pass 4: Remove excess blank lines ───────────────────────────────────────

function removeExcessBlankLines(lines) {
  const result = [];
  let prevBlank = false;
  for (const line of lines) {
    const isBlank = line === "" || line.trim() === "";
    if (isBlank && prevBlank) continue; // skip consecutive blanks
    result.push(isBlank ? "" : line);   // normalize to empty string
    prevBlank = isBlank;
  }
  return result;
}

// ── Pass 5: Fix frontmatter description ─────────────────────────────────────

function fixFrontmatterDescription(lines) {
  const result = [...lines];
  const descIdx = result.findIndex(l => l.startsWith("description:"));

  if (descIdx === -1) return result;

  const descLine = result[descIdx];
  const currentDesc = descLine.replace(/^description:\s*/, "").replace(/^"|"$/g, "").trim();

  // If description contains ### or #### fragments, generate a clean one
  if (/[#]/.test(currentDesc)) {
    // Find the body start (after second ---)
    const firstSep = result.findIndex(l => l.startsWith("---") && l.trim() === "---");
    const secondSep = result.findIndex((l, i) => i > firstSep && l.startsWith("---") && l.trim() === "---");
    if (secondSep === -1) return result; // no body found

    const bodyLines = result.slice(secondSep + 1);
    // Find first meaningful prose line after frontmatter
    const proseLines = bodyLines.filter(l => {
      const t = l.trim();
      return t && !t.startsWith("#") && !t.startsWith("---") && !t.startsWith("|") && !t.startsWith("```");
    });

    // Use the name field as fallback
    const nameLine = result.find(l => l.startsWith("name:"));
    const name = nameLine ? nameLine.replace(/^name:\s*/, "").replace(/^"|"$/g, "") : "";

    let newDesc;
    if (proseLines.length > 0) {
      // Take first 15 words of the first meaningful prose
      const words = proseLines.join(" ").split(/\s+/).filter(w => w.length > 0);
      newDesc = words.slice(0, 18).join(" ");
      if (words.length > 18) newDesc += "...";
    } else {
      newDesc = name ? `T-SQL reference covering ${name}.` : "T-SQL reference.";
    }

    result[descIdx] = `description: "${newDesc}"`;
  }

  return result;
}

// ── Pass 6: Remove doc structure marks (#### syntaxsql) ─────────────────────

function removeDocStructureMarks(lines) {
  return lines.filter(l => !isDocStructureMark(l.trim()));
}

// ── Report ───────────────────────────────────────────────────────────────────

function generateDiffReport(filePath, original, repaired) {
  const origLines = original.split("\n");
  const newLines = repaired.split("\n");
  const wordRatio = repaired.split(/\s+/).length / Math.max(original.split(/\s+/).length, 1);
  const lineDelta = newLines.length - origLines.length;

  const changes = [];
  // Count heading conversions
  const origHeadings = origLines.filter(l => /^#{1,6}\s/.test(l.trim())).length;
  const newHeadings = newLines.filter(l => /^#{1,6}\s/.test(l.trim())).length;
  const headingChange = origHeadings - newHeadings;

  // Count stray lines removed
  const origStrays = origLines.filter(l => isStrayLine(l.trim())).length;

  // Count blank line reduction
  const origBlanks = origLines.filter(l => l.trim() === "").length;
  const newBlanks = newLines.filter(l => l.trim() === "").length;
  const blankReduction = origBlanks - newBlanks;

  changes.push(`  Lines: ${origLines.length} → ${newLines.length} (${lineDelta >= 0 ? "+" : ""}${lineDelta})`);
  changes.push(`  Words: ${original.split(/\s+/).length} → ${repaired.split(/\s+/).length}`);
  if (headingChange > 0) changes.push(`  Headings → prose: ${headingChange}`);
  if (origStrays > 0) changes.push(`  Stray artifacts removed: ${origStrays}`);
  if (blankReduction > 0) changes.push(`  Blank lines reduced: ${blankReduction}`);

  return changes.join("\n");
}

// ── Exports ──────────────────────────────────────────────────────────────────

export { repairFile, isStrayLine, isDocStructureMark, isStructuralLine, getHeadingLevel, getHeadingContent, wordCount, cleanupBlankLines, joinFragmentedProse, isContinuationLine, isStandaloneItem, hasContinuationMarker };

// ── Main ─────────────────────────────────────────────────────────────────────

function main() {
  const args = process.argv.slice(2);
  const isFix = args.includes("--fix");
  const singleFile = args.includes("--file") ? args[args.indexOf("--file") + 1] : null;

  let filesToRepair;
  if (singleFile) {
    filesToRepair = [singleFile];
  } else {
    // Read the fragmented file list from the audit report
    const reportPath = path.resolve(__dirname, "../audit-tsql-reference-report.md");
    if (!fs.existsSync(reportPath)) {
      console.error("ERROR: audit-tsql-reference-report.md not found. Run audit first.");
      process.exit(1);
    }
    const report = fs.readFileSync(reportPath, "utf-8");
    const fragMatch = report.match(/## Fragmented[\s\S]*?(?=## )/);
    if (!fragMatch) {
      console.error("ERROR: Could not find fragmented section in audit report.");
      process.exit(1);
    }
    filesToRepair = [];
    const lines = fragMatch[0].split("\n");
    for (const line of lines) {
      const m = line.match(/`([^`]+\.md)`/);
      if (m) filesToRepair.push(m[1]);
    }
  }

  console.log(`Fragmentation repair — ${filesToRepair.length} files to process`);
  if (isFix) {
    console.log("Mode: LIVE FIX");
  } else {
    console.log("Mode: DRY RUN (use --fix to apply)");
  }
  console.log("─".repeat(60));

  let changed = 0;
  let skipped = 0;
  const details = [];

  for (const file of filesToRepair) {
    const filePath = path.join(contentDir, file);
    if (!fs.existsSync(filePath)) {
      console.log(`  SKIP: ${file} — not found`);
      skipped++;
      continue;
    }

    const original = fs.readFileSync(filePath, "utf-8");
    const repaired = repairFile(original);

    if (repaired === original) {
      skipped++;
      continue;
    }

    changed++;
    const diff = generateDiffReport(filePath, original, repaired);

    if (isFix) {
      fs.writeFileSync(filePath, repaired, "utf-8");
      console.log(`  ✓ ${file}`);
      console.log(diff);
      console.log("");
    } else {
      console.log(`  ~ ${file} (would change)`);
      console.log(diff);
      console.log("");
    }
  }

  console.log("─".repeat(60));
  console.log(`Summary: ${changed} changed, ${skipped} skipped, ${filesToRepair.length} total`);

  if (isFix) {
    console.log(`\nFixes applied. Next step: run audit to verify.`);
  } else {
    console.log(`\nRun with --fix to apply changes.`);
  }
}

// Only run main when executed directly, not when imported
const isMainModule = process.argv[1] && (
  process.argv[1] === fileURLToPath(import.meta.url) ||
  process.argv[1].endsWith("repair-fragmentation.mjs")
);
if (isMainModule) {
  main();
}
