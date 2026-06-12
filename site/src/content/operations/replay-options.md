---
title: "Replay Options"
topic: "profiler"
description: "06/06/2025 Before replaying a captured trace with SQL Server Profiler, specify replay options in the dialog box."
tags: ["profiler","replay-options"]
pubDate: "2025-12-01"
---

Before replaying a captured trace with SQL Server Profiler, specify replay options in the

dialog box. To launch this dialog box, open the replay trace file or table in SQL

Server Profiler, and on the

menu, select. For information about what permissions

are required to replay a trace, see

Permissions required to run SQL Server Profiler.

This article describes the options specified with the

dialog box.

You should use the Distributed Replay Utility for replaying an intensive OLTP application (with

many active concurrent connections or high throughput). The Distributed Replay Utility can

replay trace data from multiple computers, better simulating a mission-critical workload. For

more information, see

Distributed Replay overview.

The server is the name of the instance of SQL Server against which you want to replay the

trace. The server must adhere to the replay requirements described in

Replay Requirements."

The output file where the result of replaying the trace is written for later viewing. By default,

Profiler displays only the results of replaying the trace on the screen.

The database table where the result of replaying the trace is written for later viewing.

Specify the number of replay threads to use concurrently. A higher number consumes more

resources during replay, but replay is faster. Event ordering isn't fully maintained when multiple

threads are used.
