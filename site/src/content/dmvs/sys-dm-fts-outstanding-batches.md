---
name: "sys.dm_fts_outstanding_batches"
title: "sys.dm_fts_outstanding_batches"
category: "full-text"
description: "SQL database in Microsoft Fabric Returns information about each full-text indexing batch."
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT database_id, table_id, COUNT(*) AS batch_count FROM
  sys.dm_fts_outstanding_batches GROUP BY database_id, table_id ;
  GO
---

## Description

SQL database in Microsoft Fabric Returns information about each full-text indexing batch. ID of the table ID that contains the full-text index The batch object memory address Crawl object memory address (parent object) Memory region memory address of the outbound share memory of the filter daemon host (fdhost.exe) Most recent error code for the batch Indicates whether this is a retry batch: Type of retry needed for the batch:

## Syntax

```sql
SELECT database_id, table_id, COUNT(*) AS batch_count FROM sys.dm_fts_outstanding_batches GROUP BY database_id, table_id ;
GO
```
