---
name: "sys.query_store_query"
title: "sys.query_store_query"
category: "query-store"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the query and its associated overall aggregated runtime execution ID of the database object that the query is part of (stored procedure, trigger, CLR UDF/UDAgg, etc.). if the query isn't executed as part of a database object (ad hoc query). See the ID of the statement batch the query is part of. P"
tags: ["query-store", "catalog-view"]
pubDate: 2026-05-29
syntax: "query_parameterization_type"
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Contains information about the query and its associated overall aggregated runtime execution ID of the database object that the query is part of (stored procedure, trigger, CLR UDF/UDAgg, etc.). if the query isn't executed as part of a database object (ad hoc query). See the ID of the statement batch the query is part of. Populated only if query references temporary

## Syntax

`query_parameterization_type`

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
