---
title: "Get Information About DML Triggers"
topic: "change-data-capture"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This topic describes how to get information about DML triggers in SQL Server by using SQL

  Se
tags:
  - "change-data-capture"
  - "get-information-about-dml-triggers"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to get information about DML triggers in SQL Server by using SQL

Server Management Studio or Transact-SQL. This information can include the types of triggers

on a table, the name of a trigger, its owner and the date it was created or modified. If the

trigger was not encrypted when it was created, you obtain the definition of the trigger. You can

use the definition to help you understand how a trigger affects the table up on which it is

defined. Also, you can find out the objects that a specific trigger uses. With this information,

you can identify the objects that affect the trigger if they are changed or deleted in the

database.

Security

SQL Server Management Studio

Transact-SQL

,

,

,

,

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

OBJECT_DEFINITION, OBJECTPROPERTY,

Requires membership in the

role. The definition of user objects is visible to the object

owner or grantees that have any one of the following permissions: ALTER, CONTROL, TAKE

OWNERSHIP, or VIEW DEFINITION. These permissions are implicitly held by members of the

,

, and

fixed database roles.
