---
title: "Log File Auto Shrink Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class indicates that the log file shrank automatically. This event

  is not trigger
tags:
  - "event-classes"
  - "log-file-auto-shrink-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates that the log file shrank automatically. This event

is not triggered if the log file shrinks because of an explicit ALTER DATABASE statement.

Include the

event class in traces that monitor the shrinking of the log file.

When this event class is included in a trace the amount of overhead incurred will be low unless

the file frequently shrinks.

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

Length of time (in milliseconds) necessary to

extend the file.

13

Yes

Time that the log file

ended.

18

Yes

ﾉ

Expand table
