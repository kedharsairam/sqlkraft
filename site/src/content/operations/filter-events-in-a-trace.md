---
title: "Filter events in a trace"
topic: "profiler"
description: |
  06/05/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Filters limit the events collected in a trace. If a filter isn't set, all events of the selected event
  
  classes are returned in the tra
tags:
  - "profiler"
  - "filter-events-in-a-trace"
pubDate: 2025-12-01
---

06/05/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Filters limit the events collected in a trace. If a filter isn't set, all events of the selected event

classes are returned in the trace output. It's not mandatory to set a filter for a trace. However, a

filter minimizes the overhead that is incurred during tracing.

You add filters to trace definitions by using the

tab of the

or

dialog box.

1. In the

or

dialog box, select the

tab.

The

tab contains a grid control. The grid control is a table that contains

each of the traceable event classes. The table contains one row for each event class. The

event classes might differ slightly, depending on the type and version of server to which

you connect. The event classes are identified in the

column of the grid and are

grouped by event category. The remaining columns list the data columns that can be

returned for each event class.

2. Select

.

The

dialog box appears. The

dialog box contains a list of comparison

operators that you can use to filter events in a trace.

3. To apply a filter, select the comparison operator, and type a value to use for the filter.

4. Select

.

If you set filter conditions on the

and

data columns of the Events Selection

tab, then make sure that:

The date you enter matches this format:

.

-OR-

```cmd
YYYY/MM/DD HH:mm:sec
```