---
name: 'sys.sp_xtp_control_proc_exec_stats'
title: 'sys.sp_xtp_control_proc_exec_stats'
category: 'general'
description: 'Enables statistics collection for natively compiled stored procedures for the instance.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

Requires membership in the fixed

role.

To set

@new_collection_value

and query for the value of

@new_collection_value

:

SQL

System stored procedures (Transact-SQL)

In-Memory OLTP overview and usage scenarios

Related content

```sql
EXECUTE
sys.sp_xtp_control_proc_exec_stats @new_collection_value = 1;
DECLARE
@c
AS
BIT
;
EXECUTE
sys.sp_xtp_control_proc_exec_stats
@old_collection_value = @c
OUTPUT
;
SELECT
@c
AS
'collection status'
;
```
