---
title: "Analyze Queries with SHOWPLAN Results in SQL Server Profiler"
topic: "profiler"
description: |
  SQL Server Profiler

  06/05/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  You can add Showplan event classes to a trace definition that cause SQL Server Profiler to

  gather and display que
tags:
  - "profiler"
  - "analyze-queries-with-showplan-results-in-sql-server-profiler"
pubDate: 2025-12-01
---

Profiler

06/05/2025

SQL Server

Azure SQL Managed Instance

You can add Showplan event classes to a trace definition that cause SQL Server Profiler to

gather and display query plan information in the trace. It's also possible to extract Showplan

events from the other events collected in the trace and to save these Showplan events in a

separate XML file.

Extracting Showplan events from the trace can be done in any of the following ways:

At trace configuration time, using the

tab. This tab doesn't

appear until you select a one of the Showplan events on the

tab.

Using the

option on the

menu.

By extracting and saving individual events by right-clicking a specific event and choosing.

The Showplan trace events are listed and described in the following table.

Description

Indicates the first time a compiled Showplan is cached, when it's recompiled, and

when it's dropped from the plan cache. The

column contains the Showplan

in XML format. For more information, see

Performance Statistics Event Class.

Displays the query plan with full compilation details of the executed Transact-SQL

statement. For example, it might display costing estimates and column lists. For

more information, see

Showplan All Event Class.

Occurs when a query is compiled or recompiled on SQL Server. This is the compile

time counterpart of the

event.

occurs when a query is

executed.

occurs when a query is compiled. For

more information, see

Showplan All for Query Compile Event Class.

Displays the query plan with full run-time details of the Transact-SQL statement

being executed, including the actual number of rows passing through each

ﾉ

Expand table
