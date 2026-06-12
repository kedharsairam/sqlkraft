---
name: "sys.fn_hadr_distributed_ag_database_replica"
title: "sys.fn_hadr_distributed_ag_database_replica"
category: "availability-group"
description: "2016 (13.x) and later versions Used to map a database in a distributed availability group to the database in the local Is the identifier of the distributed availability group. Is the identifier of the database in a distributed availability group. Returns the following information."
tags: ["availability-group","function"]
pubDate: 2026-05-29
syntax: "sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )"
---

## Description

2016 (13.x) and later versions Used to map a database in a distributed availability group to the database in the local Is the identifier of the distributed availability group. Is the identifier of the database in a distributed availability group. Returns the following information.

## Syntax

```sql
sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )
```

## Examples

### Example 1

```sql
sys.fn_hadr_distributed_ag_database_replica( lag_Id, database_id )
```
