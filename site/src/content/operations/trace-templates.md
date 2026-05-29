---
title: "Trace Templates"
topic: "profiler"
description: |
  SQL Server Profiler Templates
  
  06/06/2025
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  You can use SQL Server Profiler to create templates that define the event classes and data
  
  columns to i
tags:
  - "profiler"
  - "trace-templates"
pubDate: 2025-12-01
---

SQL Server Profiler Templates

06/06/2025

Applies to:

SQL Server

Azure SQL Managed Instance

You can use SQL Server Profiler to create templates that define the event classes and data

columns to include in traces. After you define and save the template, you can run a trace that

records the data for each event class you selected. You can use a template on many traces; the

template isn't itself executed.

SQL Server Profiler offers predefined trace templates that allow you to easily configure the

event classes that you'll most likely need for specific traces. The Standard template, for

example, helps you to create a generic trace for recording logins, logouts, batches completed,

and connection information. You can use this template to run traces without modification or as

a starting point for additional templates with different event configurations.

In addition to traces from predefined templates, SQL Server Profiler also allows you to create

them from a blank template, containing no event classes by default. Using the blank trace

template can be useful when a planned trace doesn't resemble the configurations of any of the

predefined templates.

SQL Server Profiler can trace a variety of server types. For example you can trace Analysis

Services and SQL Server. However, the event classes that can be included aren't the same for

each type of server. Therefore, SQL Server Profiler maintains different templates for different

servers, and makes available the specific template that matches the selected server type.

In addition to the Standard (default) template, SQL Server Profiler includes several predefined

templates for monitoring certain types of events. The following table lists the predefined

templates, their purpose, and the event classes for which they capture information.

Captures stored procedure execution behavior over time.

Standard

Generic starting point for creating a trace. Captures all stored

procedures and Transact-SQL batches that are run. Use to

monitor general database server activity.

ﾉ

Expand table

```cmd
SP_Counts
```