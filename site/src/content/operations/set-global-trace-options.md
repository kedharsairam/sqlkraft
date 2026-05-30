---
title: "Set Global Trace Options"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to set options that apply to all traces that are created with a specific

  instance of SQL Server Profiler.

tags:
  - "profiler"
  - "set-global-trace-options"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to set options that apply to all traces that are created with a specific

instance of SQL Server Profiler.

1. On the

menu, select

.

2. In the

dialog box, select

to modify the display options, and

then select

.

3. Optionally, select

.

4. Optionally, select

. This option is

recommended and is selected by default. When this option is selected, the trace

definition is automatically updated to the current version of the server where tracing is

performed.

5. Optionally, specify how the server should manage rollover files:

Select

to automatically load

rollover files during replay.

Select

to control rollover files during replay.

Select

to replay only one file at a time.

6. Optionally, set replay options:

controls the number of processor threads to use

during replay. A higher number of threads causes replay to complete faster, but

causes server performance to degrade during replay. The recommended setting is

. The following table lists the available options:

ﾉ

Expand table

```cmd
4
```
