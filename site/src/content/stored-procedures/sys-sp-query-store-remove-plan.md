---
name: "sys.sp_query_store_remove_plan"
title: "sp_query_store_remove_plan"
category: "general"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Removes a single plan from the Query Store. The ID of the query plan to be removed. Requires the ALTER permission on the database. The following example returns information about the queries in the Query Store."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_query_store_remove_plan [ @plan_id = ] plan_id
  [ ; ]
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Removes a single plan from the Query Store. The ID of the query plan to be removed. Requires the ALTER permission on the database. The following example returns information about the queries in the Query Store. Arguments for extended stored procedures must be entered in the specific order as section.

## Syntax

```sql
sp_query_store_remove_plan [ @plan_id = ] plan_id
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
sp_query_store_remove_plan [ @plan_id = ] plan_id
[ ; ]
```
