---
title: "SQL:StmtCompleted Event Class"
topic: "event-classes"
description: |
  SQL:StmtCompleted Event Class

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The SQL:StmtCompleted event class indicates that a Transact-SQ
tags:
  - "event-classes"
  - "sqlstmtcompleted-event-class"
pubDate: 2025-12-01
---

SQL:StmtCompleted Event Class

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SQL:StmtCompleted event class indicates that a Transact-SQL statement has completed.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client provides the

client process ID.

9

Yes

CPU

Amount of CPU time (in milliseconds) used by

the event.

18

Yes

DatabaseID

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

given instance. SQL Server Profiler displays the

name of the database if the ServerName data

column is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the user

statement is running.

35

Yes

Duration

Amount of time (in microseconds) taken by the

event.

13

Yes

EndTime

Time at which the event ended.

15

Yes

EventClass

Type of event = 41.

27

No

EventSequence

Sequence of a given event within the request.

51

No

SQL:StmtCompleted Event Class Data Columns

ﾉ

Expand table
