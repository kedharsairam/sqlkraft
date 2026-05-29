---
title: "Performance considerations"
topic: "tables"
description: |
  Article

  •

  02/04/2025

  Applies to:

  SQL Server 2016 (13.x) and later

  Azure SQL Managed Instance

  This article discusses some specific performance considerations when using system-versioned

  memory-o
tags:
  - "tables"
  - "performance-considerations"
pubDate: 2025-12-01
---

Article

•

02/04/2025

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Managed Instance

This article discusses some specific performance considerations when using system-versioned

memory-optimized temporal tables.

When you add system-versioning to an existing non-temporal table, expect a performance

impact on update and delete operations, because the history table is updated automatically.

Every update and delete is recorded in an internal memory-optimized history table. You might

experience unexpected memory consumption if your workload uses those two operations

massively. Therefore we advise you the following considerations:

Don't perform massive deletes from the current table in one step. Consider deleting data

in multiple batches, with manually invoked data flush in between, with

sp_xtp_flush_temporal_history

, or while

.

Don't perform massive table updates at once, as it can result in memory consumption

that is twice the amount of memory required to update a non-temporal memory-

optimized table. This doubled memory consumption is temporary, because the data flush

task works regularly to keep memory consumption of internal staging tables within

projected boundaries in the steady state. The boundary is 10 percent of memory

consumption of the current temporal table. Consider doing massive updates in multiple

batches, or while

, such as using updates to set the defaults for

newly added columns.

The period of activation for the data flush task isn't configurable, but you can manually execute

sp_xtp_flush_temporal_history

as needed.

Consider using clustered columnstore as a storage option for a disk-based history table,

especially if you plan to run analytics queries on historical data that make use of aggregate or

windowing functions. In that case, a clustered columnstore index is an optimal choice for your

history table. Clustered columnstore indexes provide good data compression, and behave in an

insert-friendly

manner, aligning with how history data is generated.

```sql
SYSTEM_VERSIONING = OFF
SYSTEM_VERSIONING = OFF
```
