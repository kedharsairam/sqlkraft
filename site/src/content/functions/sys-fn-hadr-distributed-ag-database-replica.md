---
name: "sys.fn_hadr_distributed_ag_database_replica"
title: "sys.fn_hadr_distributed_ag_database_replica"
category: "availability-group"
description: "SQL Server 2016 (13.x) and later versions Used to map a database in a distributed availability group to the database in the local Transact-SQL syntax conventions Is the identifier of the distributed availability group. Is the identifier of the database in a distributed availability group. Returns the following information. ID of the database in the local availability group."
tags: ["availability-group", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )"
---

## Description

SQL Server 2016 (13.x) and later versions Used to map a database in a distributed availability group to the database in the local Transact-SQL syntax conventions Is the identifier of the distributed availability group. Is the identifier of the database in a distributed availability group. Returns the following information. ID of the database in the local availability group.

## Syntax

```sql
sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )
```

## Examples

### Example 1

```sql
sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )
```
