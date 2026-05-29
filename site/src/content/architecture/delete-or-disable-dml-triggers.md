---
title: "Delete or Disable DML Triggers"
topic: "change-data-capture"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This topic describes how to delete or disable a DML trigger in SQL Server by using SQL Server
tags:
  - "change-data-capture"
  - "delete-or-disable-dml-triggers"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to delete or disable a DML trigger in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Recommendations

Security

SQL Server Management Studio

Transact-SQL

When a trigger is deleted, it is dropped from the current database. The table and the data

upon which it is based are not affected. Deleting a table automatically deletes any

triggers on the table.

A trigger is enabled by default when it is created.

Disabling a trigger does not drop it. The trigger still exists as an object in the current

database. However, the trigger will not fire when any INSERT, UPDATE, or DELETE

statement on which it was programmed is executed. Triggers that are disabled can be

reenabled. Enabling a trigger does not re-create it. The trigger fires in the same manner

as when it was originally created.