/**
 * add-xevents-to-search-index.cjs
 *
 * Appends xevents content entries to the search-index.json so they
 * appear in the Spotlight command palette via generate-palette-index.js.
 */
const fs = require("fs");
const path = require("path");

const INDEX_PATH = path.join(__dirname, "..", "src", "data", "search-index.json");
const data = JSON.parse(fs.readFileSync(INDEX_PATH, "utf-8"));

const newEntries = [
  {
    slug: "system-health-session",
    name: "system_health",
    title: "The Default System Health Session (system_health)",
    category: "system-health",
    tags: ["extended-events", "system-health", "diagnostics", "ring-buffer", "default-session"],
    description:
      "Comprehensive reference on SQL Server's built-in system_health Extended Events session — how to query, interpret, and export session data for root-cause analysis of critical server events.",
    collection: "xevents",
  },
  {
    slug: "deadlock-graph-capture",
    name: "xml_deadlock_report",
    title: "Deadlock Graph Capture with xml_deadlock_report",
    category: "deadlock",
    tags: ["extended-events", "deadlock", "xml_deadlock_report", "blocking", "deadlock-graph"],
    description:
      "Production-grade techniques for capturing, querying, and analyzing SQL Server deadlock graphs using the xml_deadlock_report Extended Event, including system_health extraction and dedicated event session setup.",
    collection: "xevents",
  },
  {
    slug: "sp-statement-completed",
    name: "sp_statement_completed",
    title: "Query Performance Tracking with sp_statement_completed",
    category: "query-performance",
    tags: ["extended-events", "query-performance", "sp_statement_completed", "duration", "cpu", "logical-reads"],
    description:
      "Capture real-time query execution performance metrics using the sp_statement_completed Extended Event — duration, CPU, reads, writes, and row counts for every completed statement within a stored procedure or batch.",
    collection: "xevents",
  },
  {
    slug: "xevent-wait-statistics",
    name: "xevent_wait_statistics",
    title: "Wait Statistics Capture with Extended Events",
    category: "wait-statistics",
    tags: ["extended-events", "wait-statistics", "wait_info", "performance-monitoring", "sql_os"],
    description:
      "Architect a high-precision wait statistics monitoring pipeline using Extended Events — capture wait_type, wait_time, and blocking_session_id at per-wait granularity without the overhead of sys.dm_os_wait_stats polling.",
    collection: "xevents",
  },
];

data.push(...newEntries);
fs.writeFileSync(INDEX_PATH, JSON.stringify(data, null, 2));
console.log(
  `[xevents-index] Added ${newEntries.length} entries. Total: ${data.length} entries.`,
);
