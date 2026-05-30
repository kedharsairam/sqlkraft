/**
 * add-cookbook-to-search-index.cjs
 *
 * Appends the new "Diagnosing Deadlocks in Production" cookbook entry
 * to search-index.json so it appears in the Spotlight command palette.
 */
const fs = require("fs");
const path = require("path");

const INDEX_PATH = path.join(__dirname, "..", "src", "data", "search-index.json");
const data = JSON.parse(fs.readFileSync(INDEX_PATH, "utf-8"));

const newEntries = [
  {
    slug: "diagnosing-deadlocks-production",
    name: "Diagnosing Deadlocks in Production",
    title: "Diagnosing Deadlocks in Production",
    category: "blocking",
    tags: ["deadlock", "blocking", "xevents", "xml_deadlock_report", "system-health", "victim"],
    description:
      "Step-by-step guide to detect, capture, and analyze SQL Server deadlocks with zero downtime — using system_health, XEvent sessions, trace flags, and deadlock graph XML parsing.",
    collection: "cookbook",
  },
];

data.push(...newEntries);
fs.writeFileSync(INDEX_PATH, JSON.stringify(data, null, 2));
console.log(
  `[cookbook-index] Added ${newEntries.length} entry. Total: ${data.length} entries.`,
);
