---
name: 'sys.sp_cdc_help_change_data_capture'
title: 'sys.sp_cdc_help_change_data_capture'
category: 'general'
description: 'Azure SQL Managed Instance'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## specified table


## Description
List of captured source columns.

When both

@source_schema

and

@source_name

default to

, or are explicitly set the

,

this stored procedure returns information for all of the database capture instances that the

caller has SELECT access to. When

@source_schema

and

@source_name

are non-null, only

information on the specific named enabled table is returned.

When

@source_schema

and

@source_name

are

, the caller's authorization determines

which enabled tables are included in the result set. Callers must have SELECT permission on all

of the captured columns of the capture instance and also membership in any defined gating

roles for the table information to be included.

Members of the

database role can view information about all defined capture

instances. When information for a specific enabled table is requested, the same SELECT and

membership criteria are applied for the named table.

The following example returns the change data capture configuration for the

table.

SQL

## B. Return change data capture configuration information for

## all tables

The following example returns configuration information for all enabled tables in the database

that contain change data that the caller is authorized to access.

SQL

Last updated on 12/16/2025

```sql
captured_column_list
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
HumanResources.Employee
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_help_change_data_capture
@source_schema = N
'HumanResources'
,
@source_name = N
'Employee'
;
GO
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_help_change_data_capture;
GO
```
