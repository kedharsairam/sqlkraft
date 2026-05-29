---
name: 'sys.masked_columns'
title: 'sys.masked_columns'
category: 'objects'
description: 'For more information, see'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
For more information, see

Temporal Tables

(Relational databases)

.

This view returns information about tables where the user has some sort of permission on the

table or if the user has the VIEW ANY DEFINITION permission.

The following query joins

to

to return information about all

masked columns.

Dynamic Data Masking

sys.columns (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
SELECT tbl.name as table_name, c.name AS column_name, c.is_masked,
c.masking_function
FROM sys.masked_columns AS c
JOIN sys.tables AS tbl
ON c.object_id = tbl.object_id
WHERE is_masked = 1;
```
