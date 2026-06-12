---
name: "sys.dm_exec_background_job_queue"
title: "sys.dm_exec_background_job_queue"
category: "execution"
description: "Returns a row for each query processor job that is scheduled for asynchronous (background) Time when the job was added to the queue. Database on which the job is to execute. Value depends on the job type. For more information, see the Remarks Value depends on the job type. For more information, see the Remarks Value depends on the job type."
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_pdw_nodes_exec_background_job_queue"
---

## Description

Analytics Platform System (PDW) Returns a row for each query processor job that is scheduled for asynchronous (background) Time when the job was added to the queue. Database on which the job is to execute. Value depends on the job type. For more information, see the Remarks Value depends on the job type. For more information, see the Remarks Value depends on the job type. For more information, see the Remarks

## Syntax

`sys.dm_pdw_nodes_exec_background_job_queue`

## Examples

### Example 1

```sql
SELECT
DB_NAME(database_id)
AS
[
Database
],
COUNT (*)
AS
[Active Async Jobs]
FROM sys.dm_exec_background_job_queue
WHERE in_progress = 1
GROUP
BY database_id;
GO
```

### Example 2

```sql
KILL
STATS JOB 53;
GO
```
