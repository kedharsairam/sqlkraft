---
name: "operations"
title: "Operations"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Generates a manual checkpoint in the SQL Server database to which you are currently

connected.

## syntaxsql

Specifies the requested amount of time, in seconds, for the manual checkpoint to complete.

checkpoint_duration

is an advanced option.

When

checkpoint_duration

is specified, the SQL Server Database Engine attempts to perform

the checkpoint within the requested duration.

The

checkpoint_duration

must be an expression of type

and must be greater than zero.

When this parameter is omitted, the Database Engine adjusts the checkpoint duration to

minimize the performance impact on database applications.



Tip

For information about different types of database checkpoints and checkpoint operation

in general, see.

### sysadmin

### db_owner

### db_backupoperator

```sql
CHECKPOINT
[ checkpoint_duration ]
```
