---
name: "sys.sp_cdc_disable_db"
title: "sys.sp_cdc_disable_db"
category: "general"
description: "Disables change data capture (CDC) for the current database. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features of SQL Server 2022 Transact-SQL syntax conventions disables change data capture for all tables in the database currently enabled. All system objects related to ch"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.sp_cdc_disable_db"
---

## Description

Disables change data capture (CDC) for the current database. Change data capture isn't available in every edition of SQL Server. For a list of features that are supported by the editions of SQL Server, see Editions and supported features of SQL Server 2022 Transact-SQL syntax conventions disables change data capture for all tables in the database currently enabled. All system objects related to change data capture, such as change tables, jobs, stored procedures and functions, are dropped. The column for the database entry in catalog view is set to If there are many capture instances defined for the database at the time change data capture is disabled, a long running transaction can cause the execution of This problem can be avoided by disabling the individual capture instances by using

## Syntax

`sys.sp_cdc_disable_db`

## Remarks

Applies to:

Disables change data capture (CDC) for the current database. Change data capture isn't

available in every edition of SQL Server. For a list of features that are supported by the editions

of SQL Server, see

Editions and supported features of SQL Server 2022

Transact-SQL syntax conventions

(success) or

disables change data capture for all tables in the database currently

enabled. All system objects related to change data capture, such as change tables, jobs, stored

procedures and functions, are dropped. The

column for the database entry in

sys.databases

catalog view is set to

If there are many capture instances defined for the database at the time change data capture is

disabled, a long running transaction can cause the execution of

This problem can be avoided by disabling the individual capture instances by using

before running

## Examples

### Example 1

`AdventureWorks2022`

### Example 2

```sql
USE
AdventureWorks2022;
GO
EXECUTE sys.sp_cdc_disable_db;
GO
```

### Example 3

`sp_tableoption`
