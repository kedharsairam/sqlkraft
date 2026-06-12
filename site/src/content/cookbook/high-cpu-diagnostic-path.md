---
name: "High CPU Diagnostic Path"
title: "High CPU Diagnostic Path"
category: "performance"
severity: "critical"
description: "Systematic approach to diagnosing high CPU usage on SQL Server using DMVs, wait statistics, and diagnostic scripts."
tags: ["cpu","performance","scheduling","diagnostic"]
pubDate: 2026-05-30
---

When SQL Server consumes excessive CPU, the root cause typically falls into one of three categories: expensive query compilation/recompilation, inefficient execution plans with scans or excessive row operations, or signal waits from OS-level scheduling pressure.

## Overview

High CPU utilization in SQL Server is most often caused by:

- **Plan cache churn** — Frequent ad-hoc queries triggering repeated compilation
- **Inefficient queries** — Missing index scans, key lookups, or sort spills
- **Parallelism issues** — CX_PACKET waits indicating skewed parallel distribution
- **Signal waits** — Threads ready to run but waiting for scheduler time (SOS_SCHEDULER_YIELD)

## Diagnostic Steps

### 1. Identify top CPU-consuming queries

Query [sys.dm_exec_query_stats](/sqlkraft/dmvs/sys-dm-exec-query-stats/) to find queries with the highest total CPU time aggregated over cached plans. Filter by `total_worker_time` descending, and cross-reference with [sys.dm_exec_requests](/sqlkraft/dmvs/sys-dm-exec-requests/) for currently running queries.

### 2. Check scheduler pressure

Query [sys.dm_os_schedulers](/sqlkraft/dmvs/sys-dm-os-schedulers/) to view runnable task counts and scheduler load. A consistently high `runnable_tasks_count` with associated `SOS_SCHEDULER_YIELD` waits indicates CPU pressure.

### 3. Examine wait statistics

Review [SOS_SCHEDULER_YIELD](/sqlkraft/wait-statistics/sos_scheduler_yield/) waits — normal at moderate levels but concerning when consistently in top wait types. Check [CXPACKET](/sqlkraft/wait-statistics/cxpacket/) for parallel query skew and [CMEMTHREAD](/sqlkraft/wait-statistics/cmemthread/) for memory object contention.

### 4. Review execution plan cache

Use [sys.dm_exec_query_stats](/sqlkraft/dmvs/sys-dm-exec-query-stats/) to find plans with high `plan_generation_num` indicating frequent recompilations. Cross-reference with `total_worker_time` and `execution_count` to calculate average CPU per execution.

## Key Scripts

- [View top 10 high CPU utilization queries](/sqlkraft/scripts/to-view-list-of-top-10-high-cpu-utilization-queries/) — Quick-hit diagnostic for finding current CPU-heavy queries
- [View CPU utilization history](/sqlkraft/scripts/to-view-cpu-utilization-history/) — Historical trend analysis using DMV snapshots
- [View tasks, threads, and schedulers](/sqlkraft/scripts/to-view-list-of-tasks-threads-and-schedulers/) — Deep dive into scheduler-level activity

## See Also

- [Memory Pressure Triage](/sqlkraft/cookbook/memory-pressure-triage/) — Often correlated with CPU issues
- [Locking & Blocking Outages](/sqlkraft/cookbook/locking-blocking-outages/) — Blocking chains can manifest as CPU pressure
- Architecture: [Thread and Task Architecture](/sqlkraft/architecture/thread-task-architecture/)
