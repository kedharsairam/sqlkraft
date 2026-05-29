---
title: "Start a Trace"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  After you have defined a new trace or created a template by using SQL Server Profiler, you can

  start, pause, or stop capturing data by
tags:
  - "profiler"
  - "start-a-trace"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

After you have defined a new trace or created a template by using SQL Server Profiler, you can

start, pause, or stop capturing data by using the new trace definition or template.

When you start a trace and the defined source is an instance of the SQL Server Database

Engine or Analysis Services, SQL Server creates a queue that provides a temporary holding

place for captured server events.

When you use SQL Server Profiler to access SQL Trace, a new trace window opens (if one isn't

already open) when a trace is started, and data is immediately captured.

When you use Transact-SQL system stored procedures to access SQL Trace, you must start a

trace every time an instance of SQL Server starts for data to be captured. When a trace has

been started, you can modify only the name of the trace.

When working with existing traces, you can view the properties, but you can't modify the

properties. To modify the properties, stop or pause the trace.

Start a trace automatically after connecting to a server (SQL Server Profiler)

Pause a trace (SQL Server Profiler)

Stop a trace (SQL Server Profiler)

Clear a trace window (SQL Server Profiler)

Run a trace after it has been paused or stopped (SQL Server Profiler)
