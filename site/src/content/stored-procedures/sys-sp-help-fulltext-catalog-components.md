---
name: 'sys.sp_help_fulltext_catalog_components'
title: 'sp_help_fulltext_catalog_components'
category: 'general'
description: 'Returns a list of all components (filters, word-breakers, and protocol handlers), used for all full- text catalogs in the current database. Transact-SQL syntax conventions Name of the full-text catalog. Type of component. One of the following values: This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications tha'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  full-text catalog
  name
---

## Description

Returns a list of all components (filters, word-breakers, and protocol handlers), used for all full- text catalogs in the current database. Transact-SQL syntax conventions Name of the full-text catalog. Type of component. One of the following values: This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
full-text catalog
name
```
