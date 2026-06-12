---
name: "sys.sp_query_store_set_hints"
title: "sp_query_store_set_hints"
category: "general"
description: "2022 (16.x) and later versions SQL database in Microsoft Fabric A character string of query options beginning with argument, the single quotes around individual hint names must be repeated. For example, Arguments for extended stored procedures must be entered in the specific order as section."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  @query_hints = N'OPTION (MAXDOP = 1, USE HINTS
              (''ENABLE_QUERY_OPTIMIZER_HOTFIXES'',''QUERY_OPTIMIZER_COMPATIBILITY_LEVEL_150''))'
---

## Description

2022 (16.x) and later versions SQL database in Microsoft Fabric A character string of query options beginning with argument, the single quotes around individual hint names must be repeated. For example, Arguments for extended stored procedures must be entered in the specific order as section.

## Syntax

```sql
@query_hints = N'OPTION (MAXDOP = 1, USE HINTS (''ENABLE_QUERY_OPTIMIZER_HOTFIXES'',''QUERY_OPTIMIZER_COMPATIBILITY_LEVEL_150''))'
```
