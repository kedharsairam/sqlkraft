---
title: sys.dm_os_schedulers
name: sys.dm_os_schedulers
category: execution
description:
pubDate: 2026-05-29
---

ID of the parent scheduler. This is a handle to the scheduler

information for this task. For more information, see

sys.dm_os_schedulers (Transact-SQL)

.

ID of the session that is associated with the task.

Execution context ID that is associated with the task.

ID of the request of the task. For more information, see

sys.dm_exec_requests (Transact-SQL)

.

Memory address of the worker that is running the task.

NULL = Task is either waiting for a worker to be able to run,

or the task has just finished running.

For more information, see

sys.dm_os_workers (Transact-SQL)

.

Memory address of the host.

0 = Hosting was not used to create the task. This helps

identify the host that was used to create this task.

For more information, see

sys.dm_os_hosts (Transact-SQL)

.

Memory address of the task that is the parent of the object.

: Azure Synapse Analytics, Analytics Platform

System (PDW)

The identifier for the node that this distribution is on.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

## session_id

## request_id

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```
