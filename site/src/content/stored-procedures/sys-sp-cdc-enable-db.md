---
name: "sys.sp_cdc_enable_db"
title: "sys.sp_cdc_enable_db"
category: "general"
description: "Enables change data capture for the current database. This procedure must be executed for a database before any tables can be enabled for change data capture (CDC) in that database. Change data capture records insert, update, and delete activity applied to enabled tables, making the details of the changes available in an easily consumed relational format. Column information that mirrors the column"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_enable_db
  [ ; ]
---

## Description

Enables change data capture for the current database. This procedure must be executed for a database before any tables can be enabled for change data capture (CDC) in that database. Change data capture records insert, update, and delete activity applied to enabled tables, making the details of the changes available in an easily consumed relational format. Column information that mirrors the column structure of a tracked source table is captured for the modified rows, along with the metadata needed to apply the changes to a target environment. Change data capture can't be enabled on system databases or distribution databases. Change data capture isn't available in every edition of SQL Server.

## Syntax

```sql
sys.sp_cdc_enable_db
[ ; ]
```

## Remarks

Enables change data capture for the current database. This procedure must be executed for a

database before any tables can be enabled for change data capture (CDC) in that database.

Change data capture records insert, update, and delete activity applied to enabled tables,

making the details of the changes available in an easily consumed relational format. Column

information that mirrors the column structure of a tracked source table is captured for the

modified rows, along with the metadata needed to apply the changes to a target environment.

(success) or

Change data capture can't be enabled on

system databases

or distribution databases.

Change data capture isn't available in every edition of SQL Server. For a list of features

that are supported by the editions of SQL Server, see

2022

## Examples

### Example 1

`sys.sp_cdc_enable_db`

### Example 2

`is_cdc_enabled`

### Example 3

```sql
1
```

### Example 4

```sql
USE
AdventureWorks2022;
GO
EXECUTE sys.sp_cdc_enable_db;
GO
```
