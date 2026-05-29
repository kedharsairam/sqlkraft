---
title: "Filter server process IDs (SPIDs) in a trace"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to filter session identifiers (SPIDs) in a trace by using SQL Server

  Profiler.

  1. On the

  menu, select

  ,
tags:
  - "profiler"
  - "filter-server-process-ids-spids-in-a-trace"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to filter session identifiers (SPIDs) in a trace by using SQL Server

Profiler.

1. On the

menu, select

, and then connect to an instance of SQL Server.

The

dialog box appears.

If

is selected, the

dialog box fails to appear, and the trace begins instead. To turn off this setting, on the

menu, select

, and clear the

check box.

2. In the

box, type a name for the trace.

3. In the

name list, select a trace template.

4. Optionally, specify a destination file or table in which to save the trace results.

5. On the

tab, select the

column heading to launch the

dialog box. You can also right-click the column heading and choose

. If

the

column doesn't appear, check the

box.

6. In the

dialog box, expand the appropriate comparison operator, and enter a

session ID as a value for the comparison.

SQL Server Profiler
