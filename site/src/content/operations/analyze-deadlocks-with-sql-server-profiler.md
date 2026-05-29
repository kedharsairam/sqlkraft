---
title: "Analyze Deadlocks with SQL Server Profiler"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Use SQL Server Profiler to identify the cause of a deadlock. A deadlock occurs when there's a

  cyclic dependency between two or more th
tags:
  - "profiler"
  - "analyze-deadlocks-with-sql-server-profiler"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Use SQL Server Profiler to identify the cause of a deadlock. A deadlock occurs when there's a

cyclic dependency between two or more threads, or processes, for some set of resources within

SQL Server. Using SQL Server Profiler, you can create a trace that records, replays, and displays

deadlock events for analysis.

To trace deadlock events, add the

event class to a trace. This event class

populates the

data column in the trace with XML data about the process and objects

that are involved in the deadlock. SQL Server Profiler can extract the XML document to a

deadlock XML (.xdl) file which you can view later in SQL Server Management Studio. You can

configure SQL Server Profiler to extract

events to a single file that contains all

events, or to separate files. This extraction can be done in any of the following

ways:

At trace configuration time, using the

tab. This tab doesn't

appear until you select the

event on the

tab.

Using the

option on the

menu.

Individual events can also be extracted and saved by right-clicking a specific event and

choosing

.

SQL Server Profiler and SQL Server Management Studio use a deadlock wait-for graph to

describe a deadlock. The deadlock wait-for graph contains process nodes, resource nodes, and

edges representing the relationships between the processes and the resources. The

components of wait-for graphs are defined in the following table:

Description

Process

node

A thread that performs a task; for example,

,

, or

.

Resource

node

A database object; for example, a table, index, or row.

ﾉ

Expand table

```cmd
INSERT
UPDATE
DELETE
```
