---
name: "Memory Pressure Triage"
title: "Memory Pressure Triage"
category: performance
severity: critical
description: "Structured approach to detecting and resolving memory pressure in SQL Server using buffer pool analysis, memory clerks, and wait statistics."
tags: ["memory", "buffer-pool", "page-life-expectancy", "performance"]
relatedContent:
  dmvs: ["sys-dm-os-process-memory", "sys-dm-os-memory-clerks", "sys-dm-exec-query-stats"]
  waits: ["RESOURCE_SEMAPHORE", "RESOURCE_SEMAPHORE_QUERY_COMPILE", "PAGEIOLATCH_SH"]
  scripts: ["to-check-how-much-memory-sql-server-is-consuming", "to-check-memory-usage-of-each-memory-clerk", "to-check-page-life-expectancy-buffer-cache-hit", "to-analyze-buffer-pool-or-manage-buffer-pool"]
pubDate: 2026-05-30
---

Memory pressure degrades SQL Server performance by forcing pages out of the buffer cache, increasing physical I/O, and blocking query compilation. Early detection using DMV-based threshold monitoring is critical.

## Overview

Memory pressure manifests in three tiers:

- **Buffer pool pressure** — Low page life expectancy (PLE), high PAGEIOLATCH waits
- **Memory grant pressure** — Queries waiting for query execution memory grants (RESOURCE_SEMAPHORE)
- **Cache pressure** — Plan cache eviction causing frequent recompilation (RESOURCE_SEMAPHORE_QUERY_COMPILE)

## Triage Steps

### 1. Measure buffer pool health

Query [sys.dm_os_performance_counters](/sqlkraft/dmvs/sys-dm-os-process-memory/) for `Page life expectancy` (target: > 300 seconds per 4 GB of buffer pool). Low PLE combined with high `PAGEIOLATCH_SH` waits indicates insufficient memory for working set.

### 2. Check process memory state

[sys.dm_os_process_memory](/sqlkraft/dmvs/sys-dm-os-process-memory/) reveals physical memory in use, reserved pages, and page faults. A high `page_fault_count` growth rate signals memory pressure.

### 3. Analyze memory clerk usage

[sys.dm_os_memory_clerks](/sqlkraft/dmvs/sys-dm-os-memory-clerks/) breaks down memory usage by component (buffer pool, plan cache, object store). Sort by `pages_kb` descending to identify top consumers. The `MEMORYCLERK_SQLBUFFERPOOL` entry should dominate in a well-tuned system.

### 4. Check memory grants

[RESOURCE_SEMAPHORE](/sqlkraft/wait-statistics/resource_semaphore/) waits indicate queries waiting for query execution memory grants. High waits suggest memory grant sizing issues or insufficient max server memory. RESOURCE_SEMAPHORE_QUERY_COMPILE indicates compile blocking due to concurrent compilation memory pressure.

### 5. Evaluate page I/O

Elevated [PAGEIOLATCH_SH](/sqlkraft/wait-statistics/pageiolatch_sh/) waits combined with low PLE suggest the buffer cache is too small for the working set, forcing physical reads on each access.

## Key Scripts

- [Check how much memory SQL Server is consuming](/sqlkraft/scripts/to-check-how-much-memory-sql-server-is-consuming/) — Start here for baseline memory usage
- [Check memory usage of each memory clerk](/sqlkraft/scripts/to-check-memory-usage-of-each-memory-clerk/) — Identify which component is consuming memory
- [Check page life expectancy](/sqlkraft/scripts/to-check-page-life-expectancy-buffer-cache-hit/) — Buffer pool health metric
- [Analyze buffer pool](/sqlkraft/scripts/to-analyze-buffer-pool-or-manage-buffer-pool/) — Deep-dive buffer pool analysis

## See Also

- [High CPU Diagnostic Path](/sqlkraft/cookbook/high-cpu-diagnostic-path/) — CPU and memory issues often co-occur
- [Locking & Blocking Outages](/sqlkraft/cookbook/locking-blocking-outages/) — Large transactions consume memory grants
- Architecture: [Memory Management Architecture](/sqlkraft/architecture/memory-management-architecture/)
