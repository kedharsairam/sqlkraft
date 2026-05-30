---
name: "sys.sp_helpsort"
title: "sp_helpsort"
category: "general"
description: "SQL database in Microsoft Fabric Displays the sort order and character set for the instance of SQL Server. Transact-SQL syntax conventions Returns server default collation. If an instance of SQL Server is installed with a collation specified to be compatible with an earlier installation of SQL Server, returns blank results. When this behavior occurs, you can determine the collation by querying the"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  SELECT
  SERVERPROPERTY ('Collation');
---

## Description

SQL database in Microsoft Fabric Displays the sort order and character set for the instance of SQL Server. Transact-SQL syntax conventions Returns server default collation. If an instance of SQL Server is installed with a collation specified to be compatible with an earlier installation of SQL Server, returns blank results. When this behavior occurs, you can determine the collation by querying the

## Syntax

```sql
SELECT
SERVERPROPERTY ('Collation');
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Displays the sort order and character set for the instance of SQL Server. Transact-SQL syntax conventions syntaxsql None. (success) or (failure). Returns server default collation. If an instance of SQL Server is installed with a collation specified to be compatible with an earlier installation of SQL Server, returns blank results. When this behavior occurs, you can determine the collation by querying the object, such as: . Requires membership in the role.

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
