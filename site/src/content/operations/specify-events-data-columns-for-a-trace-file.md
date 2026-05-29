---
title: "Specify Events & Data Columns for a Trace File"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This article describes how to specify event classes and data columns for traces by using SQL
  
  Server Profiler.
  
  1. On the
  
  or
  
  dialog b
tags:
  - "profiler"
  - "specify-events-data-columns-for-a-trace-file"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to specify event classes and data columns for traces by using SQL

Server Profiler.

1. On the

or

dialog box, select the

tab.

The

tab contains a grid control. The grid control is a table that contains

each of the traceable event classes. The table contains one row for each event class. The

event classes can differ slightly depending on the type and version of server to which

you're connected. The event classes are identified in the

column of the grid and

are grouped by event category. The remaining columns list the data columns that can be

returned for each event class.

2. On the

tab, use the grid control to add or remove events and data

columns from the trace file.

3. To remove events from the trace, clear the check box in the

column for each event

class.

4. To include events in a trace, check the box in the

column for each event class, or

check a data column that corresponds to an event.

When you include an event class, every associated data column is also included to the trace, if

you have checked the box corresponding to an event. If you checked the box for a particular

column, only that column is included in the trace.

1. To remove data columns from an event class, clear the check boxes from the data column

in the event class row, or right-click on the column header and select the

）

Important

If the trace is going be correlated with System Monitor or Performance Monitor data, both

and

data columns must be included in the trace.