---
name: 'sys.fulltext_semantic_languages'
title: 'sys.fulltext_semantic_languages'
category: 'full-text'
description: 'Returns a row for each language whose statistics model is registered with the instance of SQL Server. When a language model is registered, that language is enabled for semantic indexing. This catalog view is similar to sys.fulltext_languages (Transact-SQL) Microsoft Windows locale identifier (LCID) for the language. Is either the value of the alias in sys.syslanguages (Transact-SQL) , or the strin'
tags: ["full-text", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT * FROM sys.fulltext_semantic_languages;
  GO
---

## Description

Returns a row for each language whose statistics model is registered with the instance of SQL Server. When a language model is registered, that language is enabled for semantic indexing. This catalog view is similar to sys.fulltext_languages (Transact-SQL) Microsoft Windows locale identifier (LCID) for the language. Is either the value of the alias in sys.syslanguages (Transact-SQL) , or the string representation of the numeric LCID.

## Syntax

```sql
SELECT * FROM sys.fulltext_semantic_languages;
GO
```

## Examples

### Example 1

```sql
SELECT * FROM sys.fulltext_semantic_languages;
GO
```
