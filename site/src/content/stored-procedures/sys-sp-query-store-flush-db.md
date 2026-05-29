---
name: 'sys.sp_query_store_flush_db'
title: 'sp_query_store_flush_db'
category: 'general'
description: 'SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Flushes the in-memory portion of the Query Store data to disk. Transact-SQL syntax conventions Query Store for readable secondaries executed on a secondary replica, that secondary replica''s cache is forced to flush to the cache on the primary replica. This can accelerate the Query Store cache data being synced to the primar'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sys.sp_query_store_flush_db'
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Flushes the in-memory portion of the Query Store data to disk. Transact-SQL syntax conventions Query Store for readable secondaries executed on a secondary replica, that secondary replica's cache is forced to flush to the cache on the primary replica. This can accelerate the Query Store cache data being synced to the primary replica, if the secondary replica cache flush is otherwise delayed under heavy workload.

## Syntax

```sql
sys.sp_query_store_flush_db
```

## Examples

### Example 1

```sql
0
```

### Example 2

```sql
1
```

### Example 3

```sql
sys.sp_query_store_flush_db
```

### Example 4

```sql
sp_query_store_flush_db
[ ; ]
```

### Example 5

```sql
EXECUTE
sp_query_store_flush_db;
```
