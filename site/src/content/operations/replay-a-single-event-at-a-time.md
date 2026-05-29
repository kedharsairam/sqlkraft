---
title: "Replay a Single Event at a Time"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This article describes how to replay one event at a time in a replay trace file or table by using
  
  SQL Server Profiler.
  
  1. Open the tr
tags:
  - "profiler"
  - "replay-a-single-event-at-a-time"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to replay one event at a time in a replay trace file or table by using

SQL Server Profiler.

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

2. On the

menu, select

, and connect to the server instance where you want to

replay the trace.

3. In the

dialog box, verify the settings, and then select

. For more

information about specifying settings on the

dialog box, see

Replay

a trace file (SQL Server Profiler)

or

Replay a trace table (SQL Server Profiler)

.

4. To replay the first event, select

in the

dialog box.

5. To replay subsequent events, on the

menu, select

, or press F10. Repeat

selecting

or pressing F10 for each event.

Replay Traces

SQL Server Profiler