---
title: "Save Trace Results to a File"
topic: "profiler"
description: |
  06/06/2025

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This article describes how to save trace results to a file by using SQL Server Profiler.

  1. On the

  menu, select

  , and then connect t
tags:
  - "profiler"
  - "save-trace-results-to-a-file"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

This article describes how to save trace results to a file by using SQL Server Profiler.

1. On the

menu, select

, and then connect to an instance of SQL Server.

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

3. Select the

check box.

The

dialog box appears.

4. Specify a path and filename in the

dialog box. Select

.

Ensure that the SQL Server service has sufficient permissions to write to a file in the

directory specified.

5. In the

dialog box, enter the maximum file size in the

text box. The default value is 5 megabytes (MB).

6. Optionally, specify the following options:

Select the

check box to have SQL Server Profiler create new files

for trace data once the maximum file size is reached. This option is selected by

default.

Select the

check box to ensure that the server records

each trace event.

When

is cleared, the server doesn't record events if

recording events significantly degrades performance.
