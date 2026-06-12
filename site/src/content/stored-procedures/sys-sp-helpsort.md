---
name: "sys.sp_helpsort"
title: "sp_helpsort"
category: "general"
description: "Displays the sort order and character set for the instance of SQL Server. Returns server default collation. If an instance of SQL Server is installed with a collation specified to be compatible with an earlier installation of SQL Server, returns blank results."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  SELECT
      SERVERPROPERTY ('Collation');
---

## Description

Displays the sort order and character set for the instance of SQL Server. Returns server default collation. If an instance of SQL Server is installed with a collation specified to be compatible with an earlier installation of SQL Server, returns blank results.

## Syntax

```sql
SELECT
SERVERPROPERTY ('Collation');
```

## Permissions

## Examples

### Example 1

```sql
EXECUTE sp_helpsort;
Server default collation
------------------------
Latin1-General , case-sensitive , accent-sensitive , kanatype-insensitive , width-
insensitive for Unicode Data , SQL Server Sort Order 51 on Code Page 1252 for non-
Unicode Data.
```
