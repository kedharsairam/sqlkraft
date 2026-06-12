---
name: "sys.syscacheobjects"
title: "sys.syscacheobjects"
category: "objects"
description: "Contains information about how the cache is used. Bucket ID. Value indicates a range from 0 through (directory size - 1). Directory size is the size of the hash table. Ad hoc query (Transact-SQL submitted as language events from the utilities, instead of remote procedure calls) ReplProc (replication procedure) This SQL Server 2000 system table is included as a view for backward compatibility. We r"
tags: ["objects","catalog-view"]
pubDate: 2026-05-29
syntax: "sys.dm_exec_plan_attributes ( plan_handle )"
---

## Description

Contains information about how the cache is used. Bucket ID. Value indicates a range from 0 through (directory size - 1). Directory size is the size of the hash table. Ad hoc query (Transact-SQL submitted as language events from the utilities, instead of remote procedure calls) ReplProc (replication procedure) This SQL Server 2000 system table is included as a view for backward compatibility. We recommend that you use the current SQL Server system views instead.

## Syntax

```sql
sys.dm_exec_plan_attributes ( plan_handle )
```
