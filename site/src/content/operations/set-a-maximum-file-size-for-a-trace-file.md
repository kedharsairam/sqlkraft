---
title: "Set a Maximum File Size for a Trace File"
topic: "profiler"
description: "06/06/2025 Use the following procedure to set the maximum file size for a trace file. 1. On the menu, select , and then connect to an instance"
tags: ["profiler","set-a-maximum-file-size-for-a-trace-file"]
pubDate: "2025-12-01"
---

Use the following procedure to set the maximum file size for a trace file.

1. On the

menu, select

, and then connect to an instance of Microsoft SQL

Server.

The

dialog box appears.

If

is selected, the

dialog box fails to appear and the trace begins instead. To turn off this setting, on the

menu, select

, and clear the

check box.

2. In the

box, type a name for the trace.

3. In the

list, select a trace template.

4. Select

, and then specify a file to store the trace information.

5. In the

check box, specify a maximum file size for the trace. When

the file size reaches this maximum, trace events are no longer recorded in this file. If you

select

(which is selected by default), the following occurs:

The file rollover option causes SQL Server to close the current file and create a new file

when the maximum file size is reached. The new file has the same name as the previous

file, but an integer is appended to the name to indicate its sequence; for example, if the

original trace file is named filename_1.trc, the next trace file is filename_2.trc, and so on. If

the name assigned to a new rollover file is already used by an existing file, the existing file

is overwritten unless it's read-only. The file rollover option is enabled by default when

you're saving trace data to a file.

With the file rollover option on, the trace continues until it's stopped by some other

means. To stop the trace after you have reached the file size limit, disable the file rollover

option.
