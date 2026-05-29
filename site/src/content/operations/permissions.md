---
title: "Permissions"
topic: "profiler"
description: |
  SQL Server Profiler templates and
  
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  SQL Server Profiler shows how SQL Server resolves queries internally. This allows administrators
  
  to
tags:
  - "profiler"
  - "permissions"
pubDate: 2025-12-01
---

SQL Server Profiler templates and

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server Profiler shows how SQL Server resolves queries internally. This allows administrators

to see exactly what Transact-SQL statements or Multi-Dimensional Expressions are submitted

to the server and how the server accesses the database or cube to return result sets.

Using SQL Server Profiler, you can do the following:

Create a trace that is based on a reusable template

Watch the trace results as the trace runs

Store the trace results in a table

Start, stop, pause, and modify the trace results as necessary

Replay the trace results

Use SQL Server Profiler to monitor only the events in which you're interested. If traces are

becoming too large, you can filter them based on the information you want, so that only a

subset of the event data is collected. Monitoring too many events adds overhead to the server

and the monitoring process, and can cause the trace file or trace table to grow very large,

especially when the monitoring process takes place over a long period of time.

Trace column values greater than 1 GB return an error and are truncated in the trace output.

Description

SQL Server Profiler Templates

Contains information about the predefined trace templates that

ship with SQL Server Profiler.

Permissions required to run SQL

Server Profiler

Contains information about the permissions that are required to

run SQL Server Profiler.

Save traces and trace templates

Contains information about saving trace output and about saving

trace definitions into a template.

Modify trace templates

Contains information about modifying trace templates by using

SQL Server Profiler or by using Transact-SQL.

ﾉ

Expand table