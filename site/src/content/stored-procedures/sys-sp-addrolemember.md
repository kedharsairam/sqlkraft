---
name: "sys.sp_addrolemember"
title: "sp_addrolemember"
category: "general"
description: "Analytics Platform System (PDW) Adds a database user, database role, Windows login, or Windows group to a database role in Transact-SQL syntax conventions The name of the database role in the current database. The security account being added to the role. can be a database user, database role, Windows login, or Windows group. This feature will be removed in a future version of SQL Server. Avoid us"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addrolemember
  [ @rolename = ]
  N
  'rolename'
  , [ @membername = ]
  N
  'membername'
  [ ; ]
---

## Description

Analytics Platform System (PDW) Adds a database user, database role, Windows login, or Windows group to a database role in Transact-SQL syntax conventions The name of the database role in the current database. The security account being added to the role. can be a database user, database role, Windows login, or Windows group. This feature will be removed in a future version of SQL Server. Avoid using this feature in

## Syntax

```sql
sp_addrolemember
[ @rolename = ]
N
'rolename'
, [ @membername = ]
N
'membername'
[ ; ]
```

## Arguments

Applies to:

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

Adds or removes members to or from a database role, or changes the name of a user-defined

database role.

Transact-SQL syntax conventions

Syntax for SQL Server (starting with 2012), Azure SQL Managed Instance, Azure SQL Database,

and Microsoft Fabric.

Syntax for SQL Server prior to 2012.

To add or drop members from roles in Azure Synapse Analytics and Analytics Platform

System (PDW) use
