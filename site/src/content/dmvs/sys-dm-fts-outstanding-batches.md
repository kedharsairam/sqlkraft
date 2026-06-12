---
name: "sys.dm_fts_outstanding_batches"
title: "sys.dm_fts_outstanding_batches"
category: "full-text"
description: "Returns information about each full-text indexing batch."
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT database_id, table_id, COUNT(*) AS batch_count FROM
  sys.dm_fts_outstanding_batches GROUP BY database_id, table_id ;
  GO
---

## Description

Returns information about each full-text indexing batch.

## Syntax

```sql
SELECT database_id, table_id, COUNT(*) AS batch_count FROM sys.dm_fts_outstanding_batches GROUP BY database_id, table_id ;
GO
```
