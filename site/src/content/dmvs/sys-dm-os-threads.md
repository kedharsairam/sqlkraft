---
name: "sys.dm_os_threads"
title: "sys.dm_os_threads"
category: "os"
description: "Analytics Platform System (PDW) Returns a list of all SQL Server Operating System threads that are running under the SQL Server Memory address (Primary Key) of the thread. Indicates the thread initiator. 1 = SQL Server started the thread. 0 = Another component started the thread, such as an extended stored procedure from within SQL Server."
tags: ["os", "dmv"]
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

Analytics Platform System (PDW) Returns a list of all SQL Server Operating System threads that are running under the SQL Server Memory address (Primary Key) of the thread. Indicates the thread initiator. 1 = SQL Server started the thread. 0 = Another component started the thread, such as an extended stored procedure from within SQL Server. ID of the thread that is assigned by the operating system. Address of the instruction that is currently being executed.

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
