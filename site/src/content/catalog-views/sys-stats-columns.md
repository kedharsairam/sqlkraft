---
name: "sys.stats_columns"
title: "sys.stats_columns"
category: "objects"
description: "Contains a row for each column that is part of ID of the object of which this column is part."
tags: ["objects","catalog-view"]
pubDate: "2026-05-29"
syntax: "HumanResources.Employee"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column that is part of ID of the object of which this column is part.

## Syntax

`HumanResources.Employee`

## Permissions

## Examples

### Example 1

`HumanResources.Employee`

### Example 2

```sql
USE
AdventureWorks2022;
GO
SELECT s.name
AS statistics_name,
c.name
AS column_name,
sc.stats_column_id
FROM sys.stats
AS s
INNER
JOIN sys.stats_columns
AS sc
ON s.object_id = sc.object_id
AND s.stats_id = sc.stats_id
INNER
JOIN sys.columns
AS c
ON sc.object_id = c.object_id
AND c.column_id = sc.column_id
WHERE s.object_id = OBJECT_ID(
'HumanResources.Employee'
);
```
