---
title: "Replay a Trace Table"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Replay is the ability to open a saved trace and replay it again. SQL Server Profiler features a

  multithreaded playback engine that can
tags:
  - "profiler"
  - "replay-a-trace-table"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Replay is the ability to open a saved trace and replay it again. SQL Server Profiler features a

multithreaded playback engine that can simulate user connections and SQL Server

Authentication. Replay is useful to troubleshoot an application or process problem. When you

identify the problem and implement corrections, run the trace that found the potential

problem against the corrected application or process. Then, replay the original trace and

compare results.

In addition to any other event classes you want to monitor, specific event classes must be

captured to enable replay. These events are captured by default if you use the

trace template. For more information, see

Replay Requirements

.

1. Open a trace table that contains the event classes necessary for replay.

2. On the

menu, select

, and connect to the server instance where you want to

replay the trace.

3. In the

dialog box, on the

tab, specify

. Select

to change the server that is displayed in the

box.

4. Optionally, select one of the following destinations in which to save the replay:

, which specifies a file in which to save the replay.

, which specifies a database table in which to save the replay.

5. Choose either

or

. The following table explains the difference between these settings.

Description

Replays events in the order they were recorded. This option enables

debugging.

This option uses multiple threads to replay each event regardless of

the sequence. This option optimizes performance.

ﾉ

Expand table
