---
title: "Modify or Rename DML Triggers"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This article describes how to modify or rename a DML trigger in SQL Server by using SQL

  Serv
tags:
  - "change-data-capture"
  - "modify-or-rename-dml-triggers"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to modify or rename a DML trigger in SQL Server by using SQL

Server Management Studio or Transact-SQL.

When you rename a trigger, the trigger must be in the current database, and the new name

must follow the rules for

identifiers

.

Avoid using the

sp_rename

stored procedure to rename a trigger. Changing any part of an

object name can break scripts and stored procedures. Renaming a trigger doesn't change the

name of the corresponding object name in the definition column of the

sys.sql_modules

catalog view. We recommend that you drop and re-create the trigger instead.

If you change the name of an object referenced by a DML trigger, you must modify the trigger

so that its text reflects the new name. Therefore, before you rename an object, display the

dependencies of the object first to determine whether the proposed change affects any

triggers.

A DML trigger can also be modified to encrypt its definition.

To view the dependencies of a trigger, you can use SQL Server Management Studio or the

following function and catalog views:

sys.sql_expression_dependencies

sys.dm_sql_referenced_entities

sys.dm_sql_referencing_entities

To alter a DML trigger requires

permission on the table or view on which the trigger is

defined.

```sql
ALTER
```
