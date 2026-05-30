/**
 * audit-content.js — Data integrity audit and pruning for empty/ghost content files.
 *
 * Walks all `src/content/**\/*.md` files, extracts body content (excluding frontmatter),
 * and moves files with < 100 meaningful body characters to `src/content/trash/`.
 *
 * "Meaningful" = non-whitespace characters (HTML/markdown/comments still count as content).
 *
 * Usage: node scripts/audit-content.js
 *        (runs automatically as `prebuild` in package.json)
 *
 * Exit codes: 0 = success (pruned ok), 1 = error
 * On success, prints summary to stdout.
 * On error, prints error to stderr and exits non-zero (which blocks the build).
 */

const fs = require("fs");
const path = require("path");

// ── Config ──────────────────────────────────────────────────────────────────
const SRC_DIR = path.resolve(__dirname, "..", "site", "src", "content");
const TRASH_DIR = path.join(SRC_DIR, "trash");
const MIN_BODY_CHARS = 100; // files with fewer meaningful body chars are flagged
const MEANINGFUL_RE = /\S/g; // any non-whitespace character

// ── Helpers ─────────────────────────────────────────────────────────────────

/**
 * Split raw markdown into frontmatter (string) and body (string).
 * If no frontmatter found, body is the entire content.
 * @param {string} raw
 * @returns {{ frontmatter: string|null, body: string }}
 */
function splitFrontmatter(raw) {
  // Frontmatter must start with --- on the very first line
  if (raw.startsWith("---")) {
    // Find the closing ---
    const endIdx = raw.indexOf("---", 3); // search past opening ---
    if (endIdx !== -1) {
      return {
        frontmatter: raw.slice(0, endIdx + 3),
        body: raw.slice(endIdx + 3),
      };
    }
  }
  return { frontmatter: null, body: raw };
}

/**
 * Count meaningful (non-whitespace) characters in a string.
 * @param {string} str
 * @returns {number}
 */
function countMeaningfulChars(str) {
  const matches = str.match(MEANINGFUL_RE);
  return matches ? matches.length : 0;
}

/**
 * Check if a file is a ghost (body is effectively empty).
 * @param {string} filePath — absolute path to .md file
 * @returns {{ isGhost: boolean, bodyChars: number, totalBytes: number }}
 */
function checkFile(filePath) {
  const stat = fs.statSync(filePath);
  const raw = fs.readFileSync(filePath, "utf-8");
  const { body } = splitFrontmatter(raw);
  const bodyChars = countMeaningfulChars(body);
  return {
    isGhost: bodyChars < MIN_BODY_CHARS,
    bodyChars,
    totalBytes: stat.size,
  };
}

/**
 * Move a file from its original location to trash/, preserving relative path components.
 * E.g., src/content/tsql-reference/sum.md → src/content/trash/tsql-reference/sum.md
 * @param {string} filePath — absolute path to file
 * @param {string} relativePath — path relative to src/content/
 */
function moveToTrash(filePath, relativePath) {
  const dest = path.join(TRASH_DIR, relativePath);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.renameSync(filePath, dest);
  return dest;
}

// ── Main ────────────────────────────────────────────────────────────────────

function main() {
  const startTime = Date.now();

  if (!fs.existsSync(SRC_DIR)) {
    console.error(`[audit-content] ERROR: source directory not found: ${SRC_DIR}`);
    process.exit(1);
  }

  // Ensure trash directory exists
  fs.mkdirSync(TRASH_DIR, { recursive: true });

  // Walk all .md files recursively
  const entries = [];
  walkDir(SRC_DIR, entries);

  // Filter out files already in trash/
  const files = entries.filter((f) => !f.startsWith("trash"));

  console.log(`[audit-content] Scanning ${files.length} files in src/content/ ...`);

  // Check each file
  const ghosts = [];
  const errors = [];

  for (const relativePath of files) {
    const fullPath = path.join(SRC_DIR, relativePath);
    try {
      const result = checkFile(fullPath);
      if (result.isGhost) {
        ghosts.push({ relativePath, ...result });
      }
    } catch (err) {
      errors.push({ relativePath, error: err.message });
    }
  }

  // Move flagged files to trash/
  let movedCount = 0;
  for (const ghost of ghosts) {
    const fullPath = path.join(SRC_DIR, ghost.relativePath);
    try {
      const dest = moveToTrash(fullPath, ghost.relativePath);
      movedCount++;
      console.log(
        `  [prune] ${ghost.relativePath} (${ghost.bodyChars} chars, ${ghost.totalBytes} bytes) → trash/`
      );
    } catch (err) {
      errors.push({ relativePath: ghost.relativePath, error: `move failed: ${err.message}` });
    }
  }

  // ── Summary ──────────────────────────────────────────────────────────────
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);

  if (errors.length > 0) {
    console.error(`\n[audit-content] ERROR: ${errors.length} file(s) had errors:`);
    for (const e of errors) {
      console.error(`  - ${e.relativePath}: ${e.error}`);
    }
    process.exit(1);
  }

  if (ghosts.length > 0) {
    console.log(
      `\n[audit-content] Found ${ghosts.length} empty files, moved ${movedCount} to trash/ (${elapsed}s)`
    );
  } else {
    console.log(`\n[audit-content] No empty files found. All ${files.length} files pass audit. (${elapsed}s)`);
  }

  process.exit(0);
}

/**
 * Walk a directory recursively, collecting relative paths of all .md files.
 * @param {string} dir — absolute directory path
 * @param {string[]} out — array to push relative paths into
 * @param {string} [prefix] — internal use for recursion
 */
function walkDir(dir, out, prefix) {
  prefix = prefix || "";
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch {
    return; // skip unreadable directories
  }
  for (const entry of entries) {
    const rel = prefix ? `${prefix}/${entry.name}` : entry.name;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkDir(full, out, rel);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      out.push(rel);
    }
  }
}

main();
