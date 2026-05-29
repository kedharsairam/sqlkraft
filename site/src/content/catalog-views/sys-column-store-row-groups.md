---
name: 'sys.column_store_row_groups'
title: 'sys.column_store_row_groups'
category: 'compatibility'
description: 'SQL database in Microsoft Fabric Provides columnstore index information on a per-segment basis. For clustered columnstore indexes, number of rows physically stored (including those marked as deleted) and a column for the number of rows marked as deleted. Use groups have a high percentage of deleted rows and should be rebuilt. The ID of the table on which this index is defined. The ID of the column'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: 'sys.column_store_row_groups'
---

## Description

SQL database in Microsoft Fabric Provides columnstore index information on a per-segment basis. For clustered columnstore indexes, number of rows physically stored (including those marked as deleted) and a column for the number of rows marked as deleted. Use groups have a high percentage of deleted rows and should be rebuilt. The ID of the table on which this index is defined. The ID of the columnstore index.

## Syntax

```sql
sys.column_store_row_groups
```
