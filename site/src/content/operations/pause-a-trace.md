---
title: "Pause a Trace"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  Pausing a trace prevents further event data from being captured until the trace is restarted.
  
  When you pause a trace, you prevent even
tags:
  - "profiler"
  - "pause-a-trace"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

Pausing a trace prevents further event data from being captured until the trace is restarted.

When you pause a trace, you prevent event data from being captured until the trace is

restarted. Restarting a trace lets trace operations resume. No previously captured data is lost

after a restart. When the trace is restarted, data capturing resumes from that point onward.

While a trace is paused, you can change the name, events, columns, and filters. However, you

can't change the destinations to which you're sending the trace data, nor change the server

connection.

1. Select a window that contains a running trace.

2. On the

menu, select

.

SQL Server Profiler