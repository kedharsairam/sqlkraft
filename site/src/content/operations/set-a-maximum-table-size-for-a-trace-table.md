---
title: "Set a Maximum Table Size for a Trace Table"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to set a maximum table size for trace tables by using SQL Server

  Profiler.

  1. On the

  menu, select

  , and
tags:
  - "profiler"
  - "set-a-maximum-table-size-for-a-trace-table"
pubDate: 2025-12-01
---

06/06/2025

SQL Server

Azure SQL Managed Instance

This article describes how to set a maximum table size for trace tables by using SQL Server

Profiler.

1. On the

menu, select

, and then connect to an instance of SQL Server.

The

dialog box appears.

If

is selected, the

dialog box fails to appear and the trace begins instead. To turn off this setting, on the

menu, select

, and clear the

check box.

2. In the

box, type a name for the trace.

3. In the

list, select a trace template.

4. Select the

check box.

5. Connect to the server on which you want the trace to be stored.

The

dialog box appears.

6. Select a database for the trace from the

list.

7. In the

box, type or select a table name.

8. Select the

check box, and specify a maximum number of rows for the

trace table.

When the number of rows in the table exceeds the maximum that you have specified, the

trace events are no longer recorded. However, tracing continues.

Profiler
