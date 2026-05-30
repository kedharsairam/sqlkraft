import { defineCollection, z } from "astro:content";

/**
 * SqlKraft — Astro Content Collection Schemas
 *
 * All collections use strict Zod validation. Each content type has a
 * dedicated collection directory under src/content/.
 */

// ──────────────────────────────────────────
// DMVs (Dynamic Management Views)
// ──────────────────────────────────────────
const dmvsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "execution",
      "index",
      "os",
      "io",
      "memory",
      "transactions",
      "in-memory",
      "availability",
      "security",
      "service-broker",
      "full-text",
      "resource-governor",
      "change-tracking",
      "clr",
      "columnstore",
      "log",
      "statistics",
      "database",
      "file",
      "partition",
      "query-performance",
      "security-audit",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    permissions: z.string().optional(),
    introducedVersion: z.string().optional(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
  }),
});

// ──────────────────────────────────────────
// Wait Statistics
// ──────────────────────────────────────────
const waitStatisticsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(), // e.g., "CXPACKET"
    title: z.string(),
    category: z.enum([
      "baseline",
      "triage",
      "top-consumer",
      "latency",
      "blocking",
      "memory",
      "scheduling",
      "io",
    ]),
    severity: z.enum(["critical", "high", "medium", "low", "info"]),
    description: z.preprocess((v) => v ?? "", z.string().max(300)),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    relatedScripts: z.array(z.string()).optional(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
  }),
});

// ──────────────────────────────────────────
// System Catalog Views
// ──────────────────────────────────────────
const catalogViewsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "databases-files",
      "objects",
      "security",
      "indexes",
      "partitions",
      "query-store",
      "service-broker",
      "full-text",
      "configuration",
      "xml",
      "spatial",
      "external",
      "compatibility",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// System Functions
// ──────────────────────────────────────────
const functionsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "aggregate",
      "analytic",
      "conversion",
      "cryptographic",
      "date-time",
      "mathematical",
      "metadata",
      "ranking",
      "security",
      "string",
      "system",
      "system-statistical",
      "text-image",
      "trigger",
      "json",
      "ai",
      "availability-group",
      "backup-restore",
      "change-data-capture",
    ]),
    returnType: z.string().optional(),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Stored Procedures (System)
// ──────────────────────────────────────────
const storedProceduresCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "general",
      "catalog",
      "configuration",
      "cursor",
      "database-mail",
      "full-text",
      "maintenance",
      "replication",
      "security",
      "spatial",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// T-SQL Reference
// ──────────────────────────────────────────
const tsqlReferenceCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "statements",
      "queries",
      "language-elements",
      "data-types",
      "operators",
      "functions",
      "hints",
      "predicates",
      "transactions",
      "variables",
      "xquery",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    syntax: z.string().optional(),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Error Codes
// ──────────────────────────────────────────
const errorsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    errorNumber: z.number(),
    severity: z.enum(["critical", "high", "medium", "low", "info"]),
    category: z.enum([
      "connection",
      "deadlock",
      "corruption",
      "io",
      "query-execution",
      "authentication",
      "replication",
      "system",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    messageText: z.string().optional(),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Architecture / Narrative
// ──────────────────────────────────────────
const architectureCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    topic: z.enum([
      "query-processing",
      "index-architecture",
      "memory-management",
      "locking",
      "deadlocks",
      "thread-task",
      "io-fundamentals",
      "transaction-log",
      "latch-contention",
      "spinlock-contention",
      "collation",
      "tables",
      "change-data-capture",
      "clr-integration",
      "xml-data",
      "json-data",
      "spatial-data",
      "sql-graph",
      "filestream",
      "service-broker",
      "hierarchical-data",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// T-SQL Scripts (curated library)
// ──────────────────────────────────────────
const scriptsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    description: z.preprocess((v) => v ?? "", z.string()),
    category: z.enum([
      "high-availability",
      "architecture",
      "automation",
      "backup-restore",
      "configuration",
      "database",
      "general",
      "index-maintenance",
      "installation",
      "migration",
      "performance",
      "replication",
      "security-audit",
      "monitoring",
      "maintenance",
      "troubleshooting",
    ]),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Operations (admin / operational procedures)
// ──────────────────────────────────────────
const operationsCollection = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    topic: z.enum([
      "ssms",
      "profiler",
      "sqlpackage",
      "linux-operations",
      "azure-synapse",
      "azure-arc",
      "event-classes",
      "ssb-diagnose",
      "data-tools",
      "upgrade",
      "migration",
      "monitor",
      "high-availability",
      "configuration",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Cookbook / Common Tasks (cross-collection scenarios)
// ──────────────────────────────────────────
const cookbookCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum(["performance", "blocking", "memory", "io", "availability", "general"]),
    severity: z.enum(["critical", "high", "medium", "low", "info"]).optional(),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    relatedContent: z
      .object({
        dmvs: z.array(z.string()).optional(),
        waits: z.array(z.string()).optional(),
        scripts: z.array(z.string()).optional(),
        errors: z.array(z.string()).optional(),
      })
      .optional(),
    related: z.array(z.string()).optional(),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Extended Events (XEvents)
// ──────────────────────────────────────────
const xeventsCollection = defineCollection({
  type: "content",
  schema: z.object({
    name: z.string(),
    title: z.string(),
    category: z.enum([
      "system-health",
      "deadlock",
      "query-performance",
      "wait-statistics",
      "general",
    ]),
    description: z.preprocess((v) => v ?? "", z.string()),
    tags: z.preprocess((v) => v ?? [], z.array(z.string())),
    targetVersion: z.string().optional(),
    pubDate: z.date(),
  }),
});

// ──────────────────────────────────────────
// Registry
// ──────────────────────────────────────────
export const collections = {
  dmvs: dmvsCollection,
  "wait-statistics": waitStatisticsCollection,
  "catalog-views": catalogViewsCollection,
  functions: functionsCollection,
  "stored-procedures": storedProceduresCollection,
  "tsql-reference": tsqlReferenceCollection,
  errors: errorsCollection,
  architecture: architectureCollection,
  scripts: scriptsCollection,
  operations: operationsCollection,
  cookbook: cookbookCollection,
  xevents: xeventsCollection,
};
