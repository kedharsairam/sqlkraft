---
title: "Save traces & templates"
topic: "profiler"
description: |
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  It's important to distinguish saving trace files from saving trace templates. Saving a trace file
  
  involves saving the captured event d
tags:
  - "profiler"
  - "save-traces-templates"
pubDate: 2025-12-01
---

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

It's important to distinguish saving trace files from saving trace templates. Saving a trace file

involves saving the captured event data to a specified place. Saving a trace template involves

saving the definition of the trace, such as specified data columns, event classes, or filters.

Save captured event data to a file or a SQL Server table when you need to analyze or replay the

captured data at a later time. Use a trace file to do the following:

Use a trace file or trace table to create a workload that is used as input for Database

Engine Tuning Advisor.

Use a trace file to capture events and send the trace file to the support provider for

analysis.

Use the query processing tools in SQL Server to access the data or to view the data in SQL

Server Profiler. Only members of the

fixed server role or the table creator can

access the trace table directly.

Capturing trace data to a table is a slower operation than capturing trace data to a file. An

alternative is to capture trace data to a file, open the trace file, and then save the trace as a

trace table.

When you use a trace file, SQL Server Profiler saves captured event data (not trace definitions)

to a SQL Server Profiler Trace (*.trc) file. The extension is added to the end of the file

automatically when the trace file is saved, regardless of any other specified extension. For

example, if you specify a trace file called

, the file created is called

.

）

Important

Users who have the SHOWPLAN, the ALTER TRACE, or the VIEW SERVER STATE permission

can view queries that are captured in Showplan output. These queries might contain

sensitive information such as passwords. Therefore, we recommend that you only grant

these permissions to users who are authorized to view sensitive information, such as

members of the

fixed database role, or members of the

fixed server

role. Additionally, we recommend that you only save Showplan files or trace files that

```cmd
Trace.dat
Trace.dat.trc
```