---
title: "SP:StmtStarting Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The SP:StmtStarting event class indicates that a Transact-SQL statement within a stored

  proc
tags:
  - "event-classes"
  - "spstmtstarting-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:StmtStarting event class indicates that a Transact-SQL statement within a stored

procedure has started.

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

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

DatabaseID

ID of the database in which the stored

procedure is running. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the stored

procedure is running.

35

Yes

EventClass

Type of event = 44.

27

No

EventSequence

Sequence of a given event within the request.

51

No

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

client provides the host name. To determine the

host name, use the HOST_NAME function.

8

Yes

IntegerData2

End offset (in bytes) of the statement that is

being executed.

55

Yes

ﾉ

Expand table
