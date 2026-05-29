---
title: "Correlate a Trace with Windows Performance Log Data"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Using SQL Server Profiler, you can open a Microsoft Windows performance log, choose the
  
  counters you want to correlate with a trace, a
tags:
  - "profiler"
  - "correlate-a-trace-with-windows-performance-log-data"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Using SQL Server Profiler, you can open a Microsoft Windows performance log, choose the

counters you want to correlate with a trace, and display the selected performance counters

alongside the trace in the SQL Server Profiler graphical user interface. When you select an

event in the trace window, a vertical red bar in the System Monitor data window pane of SQL

Server Profiler indicates the performance log data that correlates with the selected trace event.

To correlate a trace with performance counters, open a trace file or table that contains the

and

data columns, and then select

on the SQL

Server Profiler

menu. You can then open a performance log, and select the System Monitor

objects and counters that you want to correlate with the trace.

1. In SQL Server Profiler, open a saved trace file or trace table. You can't correlate a running

trace that is still collecting event data. For accurate correlation with System Monitor data,

the trace must contain both

and

data columns.

2. On the SQL Server Profiler

menu, select

.

3. In the

dialog box, select a file that contains a performance log. The performance

log data must have been captured during the same time period in which the trace data is

captured.

4. In the

dialog box, select the check boxes that correspond to

the System Monitor objects and counters that you want to display alongside the trace.

Select

.

5. Select an event in the trace events window, or navigate through several adjacent rows in

the trace events window by using the arrow keys. The vertical red bar in the

window indicates the performance log data that is correlated with the

selected trace event.

6. Select a point of interest in the System Monitor graph. The corresponding trace row that

is nearest in time is selected. To zoom in on a time range, press and drag the mouse

pointer in the System Monitor graph.