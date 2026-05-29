---
name: "sys.sp_query_store_remove_query"
title: "sp_query_store_remove_query"
category: "general"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Removes the query and all associated plans and runtime stats from the Query Store. Transact-SQL syntax conventions The ID of the query to be removed from the Query Store. Requires the ALTER permission on the database. Arguments for extended stored procedures must be entered in the specific order as section. If the parameter"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_query_store_remove_query [ @query_id = ] query_id
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Removes the query and all associated plans and runtime stats from the Query Store. Transact-SQL syntax conventions The ID of the query to be removed from the Query Store. Requires the ALTER permission on the database. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_query_store_remove_query [ @query_id = ] query_id
[ ; ]
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
sp_query_store_remove_query [ @query_id = ] query_id
[ ; ]
```
