---
name: "sys.sp_query_store_force_plan"
title: "sp_query_store_force_plan"
category: "general"
description: "2016 (13.x) and later versions SQL database in Microsoft Fabric Enables forcing a particular plan for a particular query in the Query Store. When a plan is forced for a particular query, every time SQL Server encounters the query, it tries to force the plan in the Query Optimizer."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_query_store_force_plan
  [ @query_id = ] query_id ,
  [ @plan_id = ] plan_id ,
  [ @disable_optimized_plan_forcing = ] disable_optimized_plan_forcing ,
  [ @replica_group_id = ]
  'replica_group_id'
  [ ; ]
---

## Description

2016 (13.x) and later versions SQL database in Microsoft Fabric Enables forcing a particular plan for a particular query in the Query Store. When a plan is forced for a particular query, every time SQL Server encounters the query, it tries to force the plan in the Query Optimizer. If plan forcing fails, an Extended Event is fired and the Query Optimizer is instructed to optimize in the normal way.

## Syntax

```sql
sp_query_store_force_plan
[ @query_id = ] query_id ,
[ @plan_id = ] plan_id ,
[ @disable_optimized_plan_forcing = ] disable_optimized_plan_forcing ,
[ @replica_group_id = ]
'replica_group_id'
[ ; ]
```

## Examples

### Example 1

```sql
0
```

### Example 2

`sp_query_store_force_plan`

### Example 3

`sp_query_store_unforce_plan`

### Example 4

```sql
0
```

### Example 5

```sql
1
```

### Example 6

`sys.sp_query_store_force_plan`

### Example 7

`ALTER`

### Example 8

```sql
SELECT txt.query_text_id,
txt.query_sql_text,
pl.plan_id,
qry.*
FROM sys.query_store_plan
AS pl
INNER
JOIN sys.query_store_query
AS qry
```

### Example 9

```sql
ON pl.query_id = qry.query_id
INNER
JOIN sys.query_store_query_text
AS txt
ON qry.query_text_id = txt.query_text_id;
EXECUTE sp_query_store_force_plan
@query_id = 3,
@plan_id = 3;
SELECT query_plan
FROM sys.query_store_plan
AS qsp
INNER
JOIN sys.query_store_plan_forcing_locations
AS pfl
ON pfl.query_id = qsp.query_id
INNER
JOIN sys.query_store_replicas
AS qsr
ON qsr.replica_group_id = qsp.replica_group_id
WHERE qsr.replica_name =
'yourSecondaryReplicaName'
;
```
