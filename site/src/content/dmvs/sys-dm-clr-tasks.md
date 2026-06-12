---
name: "sys.dm_clr_tasks"
title: "sys.dm_clr_tasks"
category: "clr"
description: "Returns a row for all common language runtime (CLR) tasks that are currently running. A Transact-SQL batch that contains a reference to a CLR routine creates a separate task for execution of all the managed code in that batch. Multiple statements in the batch that require managed code execution use the same CLR task."
tags: ["clr", "dmv"]
pubDate: 2026-05-29
syntax: "##MS_ServerStateReader##"
---

## Description

Returns a row for all common language runtime (CLR) tasks that are currently running. A Transact-SQL batch that contains a reference to a CLR routine creates a separate task for execution of all the managed code in that batch. Multiple statements in the batch that require managed code execution use the same CLR task.

## Syntax

```sql
##MS_ServerStateReader##
```

## Permissions

Article • 10/12/2023 SQL Server Azure SQL Database Azure SQL Managed Instance Returns a row for all common language runtime (CLR) tasks that are currently running. A Transact-SQL batch that contains a reference to a CLR routine creates a separate task for execution of all the managed code in that batch. Multiple statements in the batch that require managed code execution use the same CLR task. The CLR task is responsible for maintaining objects and state pertaining to managed code execution, as well as the transitions between the instance of SQL Server and the common language runtime. Address of the CLR task. Address of the underlying Transact-SQL batch task. Address of the application domain in which this task is running. Current state of the task. State the abort is currently in (if the task was canceled) There are multiple states involved while aborting tasks. Task type. Affinity of the task. Number of times the task was forced to yield. On SQL Server and SQL Managed Instance, requires permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, either the permission on the database, or membership in the server role is required. ﾉ
