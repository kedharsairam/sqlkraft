---
title: "Replay Traces"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Replay is the ability to reproduce activity that has been captured in a trace. When you create or

  edit a trace, you can save the trace
tags:
  - "profiler"
  - "replay-traces"
pubDate: 2025-12-01
---

06/06/2025

SQL Server

Azure SQL Managed Instance

Replay is the ability to reproduce activity that has been captured in a trace. When you create or

edit a trace, you can save the trace to a file and replay it later. You can use SQL Server Profiler

to replay trace activity from a single computer. For large workloads, use the Distributed Replay

Utility to replay trace data from multiple computers.

This section describes how to use the replay features of SQL Server Profiler. For more

information about the Distributed Replay Utility, see

Distributed Replay overview.

Profiler features a multithreaded playback engine that can simulate user

connections and SQL Server Authentication. Replay is useful to troubleshoot an application or

process problem. When you have identified the problem and implemented corrections, run the

trace that found the potential problem against the corrected application or process. Then,

replay the original trace and compare results.

Trace replay supports debugging by using the

and the

options on the SQL Server Profiler

menu. These options especially improve the analysis

of long scripts because they can break the replay of the trace into short segments so they can

be analyzed incrementally.

For information about the permissions required to replay traces, see

Permissions required to

run SQL Server Profiler.

Description

Replay Requirements

Describes the events that must be included in a trace definition so

that it can be replayed with SQL Server Profiler.

Replay Options (SQL Server

Profiler)

Describes the options you can set in the

dialog box of SQL Server Profiler.

Considerations for replaying

traces (SQL Server Profiler)

Describes trace events that can't be replayed with SQL Server Profiler

and the effects on server performance of replaying traces.

ﾉ

Expand table
