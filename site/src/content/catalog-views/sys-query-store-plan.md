---
name: "sys.query_store_plan"
title: "sys.query_store_plan"
category: "query-store"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about each execution plan associated with a query."
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: "<major>.<minor>.<build>.<revision>"
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about each execution plan associated with a query. ID of the plan group. Cursor queries typically require multiple (populate and fetch) plans. Populate and fetch plans that are compiled together are in the same group. Version of the engine used to compile the plan Database compatibility level of the database

## Syntax

```sql
<major>.<minor>.<build>.<revision>
```

## Examples

### Example 1

`sp_query_store_reset_exec_stats`

### Example 2

```sql
SELECT txt.query_text_id,
txt.query_sql_text,
pl.plan_id,
qry.*
FROM sys.query_store_plan
AS pl
INNER
JOIN sys.query_store_query
AS qry
ON pl.query_id = qry.query_id
INNER
JOIN sys.query_store_query_text
AS txt
ON qry.query_text_id = txt.query_text_id;
EXECUTE sp_query_store_reset_exec_stats 3;
```
