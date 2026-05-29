---
name: 'sys.sp_fulltext_semantic_register_language_statistics_db'
title: 'sp_fulltext_semantic_register_language_statistics_db'
category: 'general'
description: 'The Semantic Language Statistics database contains language-related statistics that are required for semantic processing of textual content. 1. Checks that the instance of SQL Server is a version that supports semantic processing. 2. Checks that the instance of SQL Server doesn''t already have a Semantic Language 3. Checks that the database is a valid Semantic Language Statistics database. 4. Sets '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_fulltext_semantic_register_language_statistics_db'
---

## Description

The Semantic Language Statistics database contains language-related statistics that are required for semantic processing of textual content. 1. Checks that the instance of SQL Server is a version that supports semantic processing. 2. Checks that the instance of SQL Server doesn't already have a Semantic Language 3. Checks that the database is a valid Semantic Language Statistics database. 4. Sets permissions on the Semantic Language Statistics database to restrict access to the

## Syntax

```sql
sp_fulltext_semantic_register_language_statistics_db
```

## Examples

### Example 1

```sql
sp_fulltext_semantic_register_language_statistics_db
```

### Example 2

```sql
sp_fulltext_semantic_register_language_statistics_db
```

### Example 3

```sql
EXECUTE
sp_fulltext_semantic_register_language_statistics_db @dbname =
'semanticsDb'
;
GO
```
