---
name: 'sys.sp_xtp_control_query_exec_stats'
title: 'sys.sp_xtp_control_query_exec_stats'
category: 'general'
description: 'Enables per query statistics collection for all natively compiled stored procedures for the'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

a natively compiled stored procedure are collected. Turning off statistics collection on the

instance doesn't turn off statistics collection for individual natively compiled stored procedures.

Use

sys.databases

,

sys.procedures

,

DB_ID

, or

OBJECT_ID

to get IDs for a database and stored

procedure.


## Returns the current status.
@old_collection_value

is

.

for success. Nonzero for failure.

Requires membership in the fixed

role.

The following code sample shows how to enable statistics collection for all natively compiled

stored procedures for the instance, and then for a specific natively compiled stored procedure.

SQL

System stored procedures (Transact-SQL)

In-Memory OLTP overview and usage scenarios

Related content

```sql
0
```

```sql
DECLARE
@c
AS
BIT
;
EXECUTE
sys.sp_xtp_control_query_exec_stats @new_collection_value = 1;
EXECUTE
sys.sp_xtp_control_query_exec_stats
@old_collection_value = @c
OUTPUT
;
SELECT
@c
AS
'collection status'
;
EXECUTE
sys.sp_xtp_control_query_exec_stats
@new_collection_value = 1,
@database_id = 5,
@xtp_object_id = 41576255;
EXECUTE
sys.sp_xtp_control_query_exec_stats
@database_id = 5,
@xtp_object_id = 41576255,
@old_collection_value = @c
OUTPUT
;
SELECT
@c
AS
'collection status'
;
```
