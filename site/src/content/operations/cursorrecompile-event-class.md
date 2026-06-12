---
title: "CursorRecompile Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class describes cursor recompile events that occur in application

  programming int
tags:
  - "event-classes"
  - "cursorrecompile-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class describes cursor recompile events that occur in application

programming interface (API) cursors. Cursor recompile events occur when the Microsoft

Database Engine recompiles a Transact-SQL cursor due to a schema change.

Include the

event class in traces that record the performance of cursors.

When the

event class is included in a trace, the amount of overhead incurred

depends on how frequently cursors are used against the database during the trace. If cursors

are used extensively, the trace may significantly impede performance.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ID of the database specified by the USE

database

statement or the default database if

no USE

database

statement has been issued for

a given instance. SQL Server Profiler displays

the name of the database if the

data column is captured in the trace and the

server is available. Determine the value for a

database by using the DB_ID function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

Type of event recorded = 75.

27

No

ﾉ

Expand table
