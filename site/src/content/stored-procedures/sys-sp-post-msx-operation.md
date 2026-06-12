---
name: "sys.sp_post_msx_operation"
title: "sp_post_msx_operation"
category: "general"
description: "Inserts operations (rows) into the system table for target servers to download The type of operation for the posted operation."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  JOB
  INSERT
  UPDATE
  DELETE
  START
  STOP
  SERVER
  RE-ENLIST
  DEFECT
---

## Description

Inserts operations (rows) into the system table for target servers to download The type of operation for the posted operation.

## Syntax

```sql
JOB
INSERT
UPDATE
DELETE
START
STOP
SERVER
RE-ENLIST
DEFECT
```

## Permissions

None. must be run from the database. can always be called safely because it first determines if the current server is a multiserver Microsoft SQL Server Agent and, if so, whether @object_type is a multiserver job. After an operation is posted, it appears in the table. After a job is created and posted, subsequent changes to that job must also be communicated to the target servers (TSX). This step is also accomplished using the download list. We highly recommend that you manage the download list in SQL Server Management Studio. For more information, see View or Modify Jobs. To run this stored procedure, users must be granted the fixed server role. sp_add_jobserver (Transact-SQL) sp_delete_job (Transact-SQL) sp_delete_jobserver (Transact-SQL) sp_delete_targetserver (Transact-SQL) sp_resync_targetserver (Transact-SQL) sp_start_job (Transact-SQL) sp_stop_job (Transact-SQL) sp_update_job (Transact-SQL) sp_update_operator (Transact-SQL) System stored procedures (Transact-SQL)
