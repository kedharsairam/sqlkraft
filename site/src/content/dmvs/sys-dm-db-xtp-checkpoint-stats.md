---
name: 'sys.dm_db_xtp_checkpoint_stats'
title: 'sys.dm_db_xtp_checkpoint_stats'
category: 'in-memory'
description: 'Returns statistics about the In-Memory OLTP checkpoint operations in the current database. If the database has no In-Memory OLTP objects, In-Memory OLTP (In-Memory Optimization) SQL Server 2014 (12.x) is substantially different from more recent versions, and is discussed The following table describes the columns in Server 2016 (13.x) and later versions. Last LSN seen by the controller. Log bytes u'
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_db_xtp_checkpoint_stats'
---

## Description

Returns statistics about the In-Memory OLTP checkpoint operations in the current database. If the database has no In-Memory OLTP objects, In-Memory OLTP (In-Memory Optimization) SQL Server 2014 (12.x) is substantially different from more recent versions, and is discussed The following table describes the columns in Server 2016 (13.x) and later versions. Last LSN seen by the controller. Log bytes unprocessed by the controller,

## Syntax

```sql
sys.dm_db_xtp_checkpoint_stats
```
