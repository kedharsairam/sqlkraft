---
name: "sys.sp_xtp_control_proc_exec_stats"
title: "sys.sp_xtp_control_proc_exec_stats"
category: "general"
description: "Enables statistics collection for natively compiled stored procedures for the instance. To enable statistics collection at the query level for natively compiled stored procedures, see sys.sp_xtp_control_query_exec_stats Determines whether procedure-level statistics collection is on ( @new_collection_value is set to zero when SQL Server or the database starts. for success. Nonzero for failure."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_xtp_control_proc_exec_stats
  [ [ @new_collection_value = ] collection_value ]
  , [ @old_collection_value = ] old_collection_value
  OUTPUT
  [ ; ]
---

## Description

Enables statistics collection for natively compiled stored procedures for the instance. To enable statistics collection at the query level for natively compiled stored procedures, see sys.sp_xtp_control_query_exec_stats Determines whether procedure-level statistics collection is on ( @new_collection_value is set to zero when SQL Server or the database starts. for success. Nonzero for failure.

## Syntax

```sql
sys.sp_xtp_control_proc_exec_stats
[ [ @new_collection_value = ] collection_value ]
, [ @old_collection_value = ] old_collection_value
OUTPUT
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Enables statistics collection for natively compiled stored procedures for the instance. To enable statistics collection at the query level for natively compiled stored procedures, see sys.sp_xtp_control_query_exec_stats . syntaxsql Determines whether procedure-level statistics collection is on ( ) or off ( ). @new_collection_value is . @new_collection_value is set to zero when SQL Server or the database starts. Returns the current status. @old_collection_value is . for success. Nonzero for failure.

## Examples

### Example 1

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
