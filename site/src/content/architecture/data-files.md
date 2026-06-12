---
title: "data files"
topic: "query-processing"
description: "The number of files depends on the number of (logical) processors on the machine. As a"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

The number of files depends on the number of (logical) processors on the machine. As a

general rule, if the number of logical processors is less than or equal to eight, use the same

number of data files as logical processors. If the number of logical processors is greater than

eight, use eight data files and then if contention continues, increase the number of data files by

multiples of 4 until the contention is reduced to acceptable levels or make changes to the

workload/code. Also keep in mind other recommendations for

, available in

Optimizing

tempdb performance in SQL Server.

However, by carefully considering the concurrency needs of

, you can reduce database

management overhead. For example, if a system has 64 CPUs and usually only 32 queries use

, increasing the number of

files to 64 will not improve performance.

The following table lists SQL Server components and indicates whether they can use more that

64 CPUs.

Database Engine

Sqlserver.exe

Yes

Reporting Services

Rs.exe

No

SQL Trace and SQL Server Profiler are deprecated. The

Microsoft.SqlServer.Management.Trace

namespace that contains the SQL Server Trace and

Replay objects are also deprecated.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Events instead. For more information on

, see

and.

７

Note

Profiler for Analysis Services workloads is NOT deprecated, and will continue to

be supported.

components that can use more than 64 CPUs

ﾉ

Expand table

Analysis Services

As.exe

No

Integration Services

Is.exe

No

Service Broker

Sb.exe

No

Full-Text Search

Fts.exe

No

Agent

Sqlagent.exe

No

Management Studio

Ssms.exe

No

Setup

Setup.exe

No

`tempdb`

`tempdb`

`tempdb`

`tempdb`
