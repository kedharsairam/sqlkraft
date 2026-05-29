---
title: "Replay to a Breakpoint"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This article describes how to set breakpoints in a trace file or table that you want to replay by
  
  using SQL Server Profiler. Setting b
tags:
  - "profiler"
  - "replay-to-a-breakpoint"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to set breakpoints in a trace file or table that you want to replay by

using SQL Server Profiler. Setting breakpoints in a trace file or table before you start to replay

the trace, enables you to pause replay of the trace at specific events. Using breakpoints while

replaying a trace supports debugging because you can break the replay of long trace scripts

into short segments that can be analyzed incrementally.

1. Open the trace file or trace table you want to replay. For more information, see

Open a

trace file (SQL Server Profiler)

or

Open a trace table (SQL Server Profiler)

.

Make sure that the trace file or table you open contains the event classes necessary for

replay. For more information, see

Replay Requirements

.

2. In the trace window, select an event that you want to use as a breakpoint. Use one of the

following three methods to set a breakpoint:

Press F9.

On the

menu, select

.

Right-click the event, and then select

.

A red bullet appears next to the selected trace event, indicating that it's the trace

breakpoint.

Repeat this step to set several breakpoints.

3. On the

menu, select

, and connect to the server where you want to replay the

trace.

4. In the

dialog box, verify the settings, and then select

.

The replay starts, pausing when the breakpoint is reached.

5. Press F5 to resume the replay and proceed to the next breakpoint.

6. Repeat Step 5 through the end of the trace.