---
title: "Stop a Trace"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to stop a trace that is running by using SQL Server Profiler.

  Stopping a trace stops data from being captur
tags:
  - "profiler"
  - "stop-a-trace"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to stop a trace that is running by using SQL Server Profiler.

Stopping a trace stops data from being captured. After a trace is stopped, it can't be restarted

without losing previously captured data, unless the data has been captured to a trace file or

trace table. You can also save the collected data to a table or file after stopping a trace. All

trace properties that were previously selected are preserved when a trace is stopped. When a

trace is stopped, you can change the name, events, columns, and filters.

1. Select a trace that is running.

2. On the

menu, select

.

SQL Server Profiler
