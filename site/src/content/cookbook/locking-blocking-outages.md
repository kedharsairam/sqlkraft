---
name: "Locking & Blocking Outages"
title: "Locking & Blocking Outages"
category: "blocking"
severity: "critical"
description: "Diagnostic workflow for identifying and resolving blocking chains, deadlocks, and lock contention using DMVs, wait types, and troubleshooting scripts."
tags: ["blocking","locking","deadlock","contention","performance"]
pubDate: 2026-05-30
---

Blocking is a natural part of transactional SQL Server — but prolonged blocking chains halt throughput and cause application timeouts. This guide walks through identifying the lead blocker, resolving lock contention, and capturing deadlock graphs.

## Overview

Blocking outages typically follow one of these patterns:

- **Long-running transactions** — Uncommitted transactions holding locks while other sessions wait (LCK_M_* waits)
- **Schema modification blocking** — DDL statements (LCK_M_SCH_M) blocking all subsequent access
- **Deadlock cycles** — Two or more sessions holding resources each other needs, resolved by the deadlock monitor
- **Lock escalation** — Row locks escalated to table locks under memory pressure

## Diagnostic Steps

### 1. Identify active blocking chains

Query [sys.dm_exec_requests](/sqlkraft/dmvs/sys-dm-exec-requests/) filtering by `blocking_session_id != 0`. This returns sessions currently blocked. The session_id that appears most often as a blocker is the lead blocker. Cross-reference with [sys.dm_os_waiting_tasks](/sqlkraft/dmvs/sys-dm-os-waiting-tasks/) for wait type details.

### 2. Inspect lock resources

[sys.dm_tran_locks](/sqlkraft/dmvs/sys-dm-tran-locks/) shows every lock held and waiting. Filter by `request_session_id` of the lead blocker to see what resources they own. Common patterns:
- **LCK_M_S** — Shared lock waiting, typically for SELECT queries blocked by modification
- **LCK_M_U** — Update lock waiting
- **LCK_M_X** — Exclusive lock waiting, blocked by a shared lock holder
- **LCK_M_IX** — Intent exclusive, blocked by schema modification (SCH_M)
- **LCK_M_SCH_M** — Schema modification lock, blocks everything

### 3. Analyze wait type distribution

The LCK_M_* wait types pinpoint the exact lock mode being waited on:
- [LCK_M_S](/sqlkraft/wait-statistics/lck_m_s/) — SELECT blocked by modification
- [LCK_M_X](/sqlkraft/wait-statistics/lck_m_x/) — Modification blocked by another modification or shared lock
- [LCK_M_SCH_M](/sqlkraft/wait-statistics/lck_m_sch_m/) — DDL blocked or blocking — most severe
- [LCK_M_SCH_S](/sqlkraft/wait-statistics/lck_m_sch_s/) — Schema stability wait during DDL

### 4. Capture deadlock graph

Use system_health session or trace flag 1222 to capture deadlock XML. Query the XML deadlock graph to identify involved sessions, resources, and the victim. See [sys.dm_exec_requests](/sqlkraft/dmvs/sys-dm-exec-requests/) for the victim session details.

## Key Scripts

- [Identify blockings](/sqlkraft/scripts/to-identify-blockings/) — Quick query to find currently blocked sessions
- [Identify lead blocker](/sqlkraft/scripts/to-identify-the-lead-blocker-or-blocking-chain/) — Find the root blocker in the chain
- [Identify deadlock](/sqlkraft/scripts/to-identify-deadlock/) — Read captured deadlock graphs
- [View locks](/sqlkraft/scripts/to-view-locks/) — See all locks across the instance

## See Also

- [High CPU Diagnostic Path](/sqlkraft/cookbook/high-cpu-diagnostic-path/) — Blocking chains can appear as CPU pressure
- [Memory Pressure Triage](/sqlkraft/cookbook/memory-pressure-triage/) — Large transactions use memory grants
- Architecture: [Locking Architecture](/sqlkraft/architecture/locking-architecture/)
- Architecture: [Deadlock Architecture](/sqlkraft/architecture/deadlocks-architecture/)
