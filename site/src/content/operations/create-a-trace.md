---
title: "Create a Trace"
topic: "profiler"
description: "06/05/2025 This article describes how to use SQL Server Profiler to create a trace. 1. On the menu, select , and connect to an instance of SQL"
tags: ["profiler","create-a-trace"]
pubDate: "2025-12-01"
---

This article describes how to use SQL Server Profiler to create a trace.

1. On the

menu, select

, and connect to an instance of SQL Server.

The

dialog box appears.

if

is selected, the

dialog box fails to appear, and the trace begins instead. To turn off this setting, navigate

to

>

, and clear the

check box.

2. In the

box, type a name for the trace.

3. In the

list, select a trace template on which to base the trace, or select

if you don't want to use a template.

1. To save the trace results, do one of the following steps:

Select

to capture the trace to a file. Specify a value for. The default value is 5 megabytes (MB).

Optionally, select

to automatically create new files when the

maximum file size is reached. You can also optionally select

, which causes the service that is running the trace to process trace data instead

of the client application. When the server processes trace data, no events are

skipped even under stress conditions, but server performance might be affected.

Select

to capture the trace to a database table.

Optionally, select

, and specify a value.

Ｕ

Caution
