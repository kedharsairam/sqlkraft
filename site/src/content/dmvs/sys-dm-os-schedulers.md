---
name: "sys.dm_os_schedulers"
title: "sys.dm_os_schedulers"
category: "os"
description: "Returns one row per scheduler in SQL Server where each scheduler is mapped to an individual processor. Use this view to monitor the condition of a scheduler or to identify runaway tasks. For more information about schedulers, see the Thread and Task Architecture Guide Memory address of the scheduler. Is not nullable."
tags: ["os","dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

Analytics Platform System (PDW) Returns one row per scheduler in SQL Server where each scheduler is mapped to an individual processor. Use this view to monitor the condition of a scheduler or to identify runaway tasks. For more information about schedulers, see the Thread and Task Architecture Guide Memory address of the scheduler. Is not nullable.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

ID of the parent scheduler. This is a handle to the scheduler information for this task. For more information, see sys.dm_os_schedulers (Transact-SQL). ID of the session that is associated with the task. Execution context ID that is associated with the task. ID of the request of the task. For more information, see sys.dm_exec_requests (Transact-SQL). Memory address of the worker that is running the task. NULL = Task is either waiting for a worker to be able to run, or the task has just finished running. For more information, see sys.dm_os_workers (Transact-SQL). Memory address of the host. 0 = Hosting was not used to create the task. This helps identify the host that was used to create this task. For more information, see sys.dm_os_hosts (Transact-SQL). Memory address of the task that is the parent of the object. : Azure Synapse Analytics, Analytics Platform System (PDW) The identifier for the node that this distribution is on. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. Change which cluster manages the metadata for replicas in an Always On availability group sys.dm_os_schedulers (Transact-SQL) sys.dm_os_memory_nodes (Transact-SQL) sys.dm_os_buffer_pool_extension_configuration (Transact-SQL) Buffer pool extension
