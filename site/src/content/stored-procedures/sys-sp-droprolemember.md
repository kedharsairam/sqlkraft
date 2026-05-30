---
name: "sys.sp_droprolemember"
title: "sp_droprolemember"
category: "general"
description: "Analytics Platform System (PDW) Removes a security account from a SQL Server role in the current database. Transact-SQL syntax conventions Syntax for SQL Server and Azure SQL Edge. Syntax for Azure Synapse Analytics and Analytics Platform System (PDW). This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droprolemember
  [ @rolename = ]
  N
  'rolename'
  , [ @membername = ]
  N
  'membername'
  [ ; ]
  sp_droprolemember
  N
  'rolename'
  ,
  'membername'
  [ ; ]
---

## Description

Analytics Platform System (PDW) Removes a security account from a SQL Server role in the current database. Transact-SQL syntax conventions Syntax for SQL Server and Azure SQL Edge. Syntax for Azure Synapse Analytics and Analytics Platform System (PDW). This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_droprolemember
[ @rolename = ]
N
'rolename'
, [ @membername = ]
N
'membername'
[ ; ]
sp_droprolemember
N
'rolename'
,
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

## Examples

### Example 1

`sp_droprolemember`

### Example 2

`sp_droprole`

### Example 3

```sql
ALTER
AUTHORIZATION
```

### Example 4

`sp_droprole`

### Example 5

`CONTROL`

### Example 6

`Sales`

### Example 7

```sql
EXECUTE sp_droprole
'Sales'
;
GO
```
