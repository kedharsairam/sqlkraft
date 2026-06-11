---
name: "sys.fulltext_languages"
title: "sys.fulltext_languages"
category: "full-text"
description: "This catalog view contains one row per language whose word breakers are registered with SQL Server. Each row displays the LCID and name of the language. When word breakers are registered for a language, its other linguistic resources (such as , and thesaurus files) become available to full-text indexing/querying operations."
tags: ["full-text", "catalog-view"]
pubDate: 2026-05-29
---

## Description

This catalog view contains one row per language whose word breakers are registered with SQL Server. Each row displays the LCID and name of the language. When word breakers are registered for a language, its other linguistic resources (such as , and thesaurus files) become available to full-text indexing/querying operations. The value of can be specified in the full-text queries and full-text index Transact-SQL statements.

## Code Blocks

`name`

`lcid`
