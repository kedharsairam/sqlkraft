---
name: "sys.dm_os_tasks"
title: "sys.dm_os_tasks"
category: "os"
description: "Returns one row for each task that is active in the instance of SQL Server. A task is the basic unit of execution in SQL Server. Examples of tasks include a query, a login, a logout, and system tasks like ghost cleanup activity, checkpoint activity, log writer, parallel redo activity. For more information about tasks, see the Thread and Task Architecture Guide State"
tags: ["os","dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT
                task_address,
                task_state,
                context_switches_count,
                pending_io_count,
                pending_io_byte_count,
                pending_io_byte_average,
                scheduler_id,
                session_id,
                exec_context_id,
                request_id,
                worker_address,
                host_address
                FROM
                sys.dm_os_tasks
                ORDER
                BY
                session_id, request_id;
---

## Description

Analytics Platform System (PDW) Returns one row for each task that is active in the instance of SQL Server. A task is the basic unit of execution in SQL Server. Examples of tasks include a query, a login, a logout, and system tasks like ghost cleanup activity, checkpoint activity, log writer, parallel redo activity. For more information about tasks, see the Thread and Task Architecture Guide State of the task. This can be one of the following:

## Syntax

```sql
SELECT task_address,
task_state,
context_switches_count,
pending_io_count,
pending_io_byte_count,
pending_io_byte_average,
scheduler_id,
session_id,
exec_context_id,
request_id,
worker_address,
host_address
FROM sys.dm_os_tasks
ORDER
BY session_id, request_id;
```
