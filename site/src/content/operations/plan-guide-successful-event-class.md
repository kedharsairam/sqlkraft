---
title: "Plan Guide Successful Event Class"
topic: "event-classes"
description: |
  Article

  •

  07/25/2023

  Applies to:

  SQL Server

  The Plan Guide Successful event class indicates that SQL Server successfully produced an

  execution plan for a query or batch that contained a plan gui
tags:
  - "event-classes"
  - "plan-guide-successful-event-class"
pubDate: 2025-12-01
---

Article

•

07/25/2023

SQL Server

The Plan Guide Successful event class indicates that SQL Server successfully produced an

execution plan for a query or batch that contained a plan guide. The event fires when the

following conditions are true:

The batch or module in the plan guide definition matches the batch or module that is

being executed.

The query in the plan guide definition matches the query being executed.

The hints in the plan guide definition, including the

hint, were applied

successfully to the query. That is, the compiled query plan honors the specified hints.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values that are

passed by the application instead of the

displayed name of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client provides the

client process ID.

9

Yes

DatabaseID

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

specified instance. SQL Server Profiler displays

the name of the database if the ServerName

data column is captured in the trace and the

3

Yes

７

Note

This event class is not available in Azure SQL Database.

ﾉ

Expand table

```cmd
USE PLAN
```
