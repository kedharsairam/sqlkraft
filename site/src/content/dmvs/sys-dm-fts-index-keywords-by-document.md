---
name: "sys.dm_fts_index_keywords_by_document"
title: "sys.dm_fts_index_keywords_by_document"
category: "full-text"
description: "Returns information about the document-level content of a full-text index associated with the sys.dm_fts_index_keywords_by_document is a dynamic management function. sys.dm_fts_index_keywords (Transact-SQL) sys.dm_fts_index_keywords_by_property (Transact-SQL) function."
tags: ["full-text", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_fts_index_keywords_by_document
  (
  DB_ID('database_name'),     OBJECT_ID('table_name')
  )
---

## Description

Returns information about the document-level content of a full-text index associated with the sys.dm_fts_index_keywords_by_document is a dynamic management function. sys.dm_fts_index_keywords (Transact-SQL) sys.dm_fts_index_keywords_by_property (Transact-SQL) function. This function accepts a database name and returns the database ID, which sys.dm_fts_index_keywords_by_document uses to find the specified database. If

## Syntax

```sql
sys.dm_fts_index_keywords_by_document (
DB_ID('database_name'), OBJECT_ID('table_name')
)
```
