---
title: "View & Analyze Traces"
topic: "profiler"
description: "06/06/2025 Use SQL Server Profiler to view captured event data in a trace. SQL Server Profiler displays data based on defined trace properties. O"
tags: ["profiler","view-analyze-traces"]
pubDate: 2025-12-01
---

Use SQL Server Profiler to view captured event data in a trace. SQL Server Profiler displays data

based on defined trace properties. One way to analyze SQL Server data is to copy the data to

another program, such as SQL Server or Database Engine Tuning Advisor. Database Engine

Tuning Advisor can use a trace file that contains SQL batch and remote procedure call (RPC)

events if the

data column is included in the trace. To make sure that the correct events and

columns are captured for use with Database Engine Tuning Advisor, use the predefined Tuning

template that is supplied with SQL Server Profiler.

When you open a trace by using SQL Server Profiler , the trace file doesn't need to have the.trc

file extension if the file was created by either SQL Server Profiler or SQL Trace system stored

procedures.

Profiler can also read SQL Trace

files and generic SQL script files. When

opening a SQL Trace

file that doesn't have a

file extension, such as

,

specify

SQLTrace_Log

as the file format.

You can configure the SQL Server Profiler date and time display format to assist in trace

analysis.

Using SQL Server Profiler, you can troubleshoot data by grouping traces or trace files by the

,

,

, or

data columns. Examples of data you might troubleshoot are

queries that perform poorly or that have exceptionally high numbers of logical read operations.

Additional information can be found by saving traces to tables and using Transact-SQL to

query the event data. For example, to determine which

SQL:BatchCompleted

events had

excessive wait time, execute the following:

```cmd.log.log.log trace.txt
SELECT
TextData,
Duration
,
CPU
FROM trace_table_name
WHERE
EventClass = 12
```
