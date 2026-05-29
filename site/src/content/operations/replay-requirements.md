---
title: "Replay Requirements"
topic: "profiler"
description: |
  06/05/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  In order to replay trace data with SQL Server Profiler or the Distributed Replay Utility, a specific
  
  set of event classes and columns 
tags:
  - "profiler"
  - "replay-requirements"
pubDate: 2025-12-01
---

06/05/2025

Applies to:

SQL Server

Azure SQL Managed Instance

In order to replay trace data with SQL Server Profiler or the Distributed Replay Utility, a specific

set of event classes and columns must be captured in the trace. These settings are enabled by

default if the

trace template is used to configure a trace that is later used for

replay. This topic describes these settings and other replay requirements.

You should use the Distributed Replay Utility for replaying an intensive OLTP application (with

many active concurrent connections or high throughput). The Distributed Replay Utility can

replay trace data from multiple computers, better simulating a mission-critical workload. For

more information, see

SQL Server Distributed Replay overview

.

To be replayed by SQL Server Profiler, the following set of event classes, in addition to any

other event classes you want to monitor, must be captured in the trace:

(only required when replaying server-side cursors)

(only required when replaying server-side cursors)

(only required when replaying server-side cursors)

(only required when replaying server-side cursors)

(only required when replaying server-side cursors)

(only required when replaying server-side prepared SQL statements)

(only required when replaying server-side prepared SQL statements)

SQL:BatchCompleted

SQL:BatchStarting

In addition to any other data columns you want to capture, the following data columns must

be captured in a trace to allow the trace to be replayed: