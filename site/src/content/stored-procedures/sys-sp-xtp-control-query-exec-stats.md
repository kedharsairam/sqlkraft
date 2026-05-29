---
name: 'sys.sp_xtp_control_query_exec_stats'
title: 'sys.sp_xtp_control_query_exec_stats'
category: 'general'
description: 'Enables per query statistics collection for all natively compiled stored procedures for the instance, or specific natively compiled stored procedures. Performance decreases when you enable statistics collection. If you only need to troubleshoot one, or a few natively compiled stored procedures, you can enable statistics collection for just those few natively compiled stored procedures. To enable s'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_xtp_control_query_exec_stats
  [ [ @new_collection_value = ] collection_value ]
  [ , [ @database_id = ] database_id ]
  [ , [ @xtp_object_id = ] procedure_id ]
  , [ @old_collection_value = ] old_collection_value
  OUTPUT
  [ ; ]
---

## Description

Enables per query statistics collection for all natively compiled stored procedures for the instance, or specific natively compiled stored procedures. Performance decreases when you enable statistics collection. If you only need to troubleshoot one, or a few natively compiled stored procedures, you can enable statistics collection for just those few natively compiled stored procedures. To enable statistics collection at the procedure level for all natively compiled stored

## Syntax

```sql
sys.sp_xtp_control_query_exec_stats
[ [ @new_collection_value = ] collection_value ]
[ , [ @database_id = ] database_id ]
[ , [ @xtp_object_id = ] procedure_id ]
, [ @old_collection_value = ] old_collection_value
OUTPUT
[ ; ]
```

## Examples

### Example 1

```sql
0
```

### Example 2

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
