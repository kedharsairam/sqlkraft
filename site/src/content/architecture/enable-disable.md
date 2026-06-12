---
title: "Enable & disable"
topic: "change-data-capture"
description: |
  08/22/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to enable and disable change data capture (CDC) for a database and

  a table for SQL Server and Azure SQL Man
tags:
  - "change-data-capture"
  - "enable-disable"
pubDate: 2025-12-01
---

08/22/2025

SQL Server

Azure SQL Managed Instance

This article describes how to enable and disable change data capture (CDC) for a database and

a table for SQL Server and Azure SQL Managed Instance. For Azure SQL Database, see

CDC

with Azure SQL Database.

The

permissions are required to enable or disable change data capture in SQL Server

and Azure SQL Managed Instance.

Before you can create a capture instance for individual tables, you must enable change data

capture for the database.

To enable change data capture, run the stored procedure

sys.sp_cdc_enable_db (Transact-SQL)

in the database context. To determine if a database already has CDC enabled, query the

column in the

catalog view.

When a database has change data capture enabled, the

schema,

user, metadata tables,

and other system objects are created for the database. The

schema contains the change

data capture metadata tables and, after source tables are enabled for change data capture, the

individual change tables serve as a repository for change data. The

schema also contains

associated system functions used to query for change data.

Change data capture requires exclusive use of the

schema and

user. If either a schema

or a database user named

cdc

currently exists in a database, the change data capture can't be

enabled for the database until the schema and/or user is dropped or renamed.

```sql
sysadmin sys.databases
-- ====
-- Enable Database for CDC
-- ====
USE
MyDB
GO
EXEC sys.sp_cdc_enable_db
GO
```
