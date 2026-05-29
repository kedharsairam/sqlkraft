---
title: "Permissions Required to Run SQL Server Profiler"
topic: "profiler"
description: |
  06/05/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  By default, running SQL Server Profiler requires the same user permissions as the Transact-SQL

  stored procedures that are used to crea
tags:
  - "profiler"
  - "permissions-required-to-run-sql-server-profiler"
pubDate: 2025-12-01
---

06/05/2025

Applies to:

SQL Server

Azure SQL Managed Instance

By default, running SQL Server Profiler requires the same user permissions as the Transact-SQL

stored procedures that are used to create traces. To run SQL Server Profiler, users must be

granted the

permission. For more information, see

GRANT Server Permissions

.

Query plans and query text, captured by SQL Trace as well as by other means, for

example, dynamic management views (DMVs), dynamic management functions (DMFs),

and Extended Events, can contain sensitive information. Therefore, the permissions

,

, and the covering permission

should be granted to

only users who need these permissions to fulfill their job functions, based on the principle

of least privilege.

Additionally, we recommend that you only save Showplan files or trace files that contain

Showplan-related events to a location that uses the NTFS file system and restrict access

to users who are authorized to view potentially sensitive information.

SQL Server Profiler for Analysis Services workloads are supported.

When you try to connect to an Azure SQL Database from SQL Server Profiler, it incorrectly

throws a misleading error message:

７

Note

SQL Trace and SQL Server Profiler are deprecated. The

namespace that contains the Microsoft SQL Server

Trace and Replay objects is also deprecated.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Events instead. For more information on

, see

Quickstart: Extended Events

and

.

```cmd
ALTER TRACE
ALTER
TRACE
SHOWPLAN
VIEW SERVER STATE
Microsoft.SqlServer.Management.Trace
```
