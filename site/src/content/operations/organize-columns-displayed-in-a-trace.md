---
title: "Organize Columns Displayed in a Trace"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  You can group data columns in a trace by selecting

  in the trace table or

  dialog box, or when you define a trace. Grouping the data co
tags:
  - "profiler"
  - "organize-columns-displayed-in-a-trace"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

You can group data columns in a trace by selecting

in the trace table or

dialog box, or when you define a trace. Grouping the data columns

enables you to better analyze SQL Server Profiler trace output. For more information, see

View

and analyze traces with SQL Server Profiler

.

enables you to either group the trace events, or to group and aggregate

them by the data columns you select.

Choose multiple data columns for grouping to only group trace events. When you choose

multiple data columns for grouping, the trace window displays events grouped by the

values in the data columns you selected for grouping. The following example shows how

the trace window grid would appear if you chose the

and

data

columns for grouping. The

column values are displayed in ascending order, then

the

values.

12/12/2006 3:16:43 PM

SQL:StmtStarting

2124

0

12/12/2006 5:39:23 PM

Audit Login

648

1

12/12/2006 5:24:44 PM

SQL:StmtStarting

2124

25

12/12/2006 5:24:44 PM

SQL:StmtCompleted

648

Choose only one column for grouping to group and aggregate trace events. When you

choose only one data column for grouping, the trace window displays events grouped by

the values in that data column and collapses all events under it. A plus sign (

) appears to

the left of the event in the data column you chose for grouping, and the number of

events collapsed under it appears in parentheses to the right of the event. The following

example shows how the trace window grid would appear if you chose only the

data column for grouping. All events are organized under the

data column. To

view all events, select the plus sign to expand and display all event classes of that type.

ﾉ

Expand table
