---
name: 'sys.fn_hadr_is_primary_replica'
title: 'sys.fn_hadr_is_primary_replica'
category: 'availability-group'
description: 'Used to determine if the current replica is the primary replica. Transact-SQL syntax conventions Is the name of the database. is type sysname. Returns data type : 1 if the database on the current instance is the primary replica, otherwise if the database doesn''t exist, or isn''t part of an availability group. Use this function to conveniently determine whether the local instance is hosting the prim'
tags: ["availability-group", "function"]
pubDate: 2026-05-29
syntax: |
  sys.fn_hadr_is_primary_replica (
  'dbname'
  )
---

## Description

Used to determine if the current replica is the primary replica. Transact-SQL syntax conventions Is the name of the database. is type sysname. Returns data type : 1 if the database on the current instance is the primary replica, otherwise if the database doesn't exist, or isn't part of an availability group. Use this function to conveniently determine whether the local instance is hosting the primary replica of the specified availability database. Sample code could be similar to the following.

## Syntax

```sql
sys.fn_hadr_is_primary_replica (
'dbname'
)
```

## Permissions

The following example returns 1 if the specified database on the local instance is the primary replica. SQL Requires VIEW SERVER STATE permission on the server. Always On Availability Groups Functions (Transact-SQL) sys.dm_hadr_database_replica_states (Transact-SQL) Always On Availability Groups (SQL Server) CREATE AVAILABILITY GROUP (Transact-SQL) ALTER AVAILABILITY GROUP (Transact-SQL) Always On Availability Groups Catalog Views (Transact-SQL) See Also

## Remarks

Applies to:

Used to determine if the current replica is the primary replica.

Transact-SQL syntax conventions

Is the name of the database.

is type sysname.

Returns data type

: 1 if the database on the current instance is the primary replica, otherwise

if the database doesn't exist, or isn't part of an availability group.

Use this function to conveniently determine whether the local instance is hosting the primary

replica of the specified availability database. Sample code could be similar to the following.
