---
title: "Replay to a Cursor"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to replay trace files or tables that pause when a cursor is reached by

  using SQL Server Profiler. Pausing t
tags:
  - "profiler"
  - "replay-to-a-cursor"
pubDate: 2025-12-01
---

06/06/2025

SQL Server

Azure SQL Managed Instance

This article describes how to replay trace files or tables that pause when a cursor is reached by

using SQL Server Profiler. Pausing traces at cursors supports debugging because you can break

the replay of long trace scripts into short segments that can be analyzed incrementally.

1. Open the trace file or trace table you want to replay. For more information, see

Open a

trace file (SQL Server Profiler)

or

Open a trace table (SQL Server Profiler).

Make sure that the trace file or table you open contains the event classes necessary for

replay. For more information, see

Replay Requirements.

2. In the trace window, select an event.

3. On the

menu, select

, and then connect to the server where you

want to replay the trace.

4. In the

dialog box, verify the settings, and then select.

The replay starts, pausing when the first cursor is reached.

5. Press F5 to resume the trace.

6. Repeat Step 5 through the end of the trace.

Replay to a breakpoint (SQL Server Profiler)

Replay Traces

Profiler
