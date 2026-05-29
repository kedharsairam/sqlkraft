---
name: 'sys.fulltext_semantic_languages'
title: 'sys.fulltext_semantic_languages (Transact-'
category: 'full-text'
description: 'Returns a row for each language whose statistics model is registered with the instance of SQL'
tags: ["catalog-view", "full-text"]
pubDate: 2026-05-29
---

SQL)

Article

•

02/28/2023

Applies to:

SQL Server


## Returns a row for each language whose statistics model is registered with the instance of SQL
Server. When a language model is registered, that language is enabled for semantic indexing.

This catalog view is similar to

sys.fulltext_languages (Transact-SQL)

.


## Description
lcid

int

Microsoft Windows locale identifier (LCID) for the language.

name

sysname

Is either the value of the alias in

sys.syslanguages (Transact-SQL)

corresponding

to the value of

, or the string representation of the numeric LCID.

For more information, see

Install and Configure Semantic Search

.

For more information about the semantic language statistics database that is installed to

support semantic indexing, query the catalog view

sys.fulltext_semantic_language_statistics_database (Transact-SQL)

.

The visibility of the metadata in catalog views is limited to securables that a user either owns or

on which the user has been granted some permission.

ﾉ

Expand table

The following example shows how to query

to get

information about all the language models registered for semantic indexing on the current

instance of SQL Server.

Install and Configure Semantic Search

See Also

```sql
SELECT * FROM sys.fulltext_semantic_languages;
GO
```
