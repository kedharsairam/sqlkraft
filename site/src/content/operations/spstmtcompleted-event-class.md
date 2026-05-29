---
title: "SP:StmtCompleted Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The SP:StmtCompleted event class indicates that a Transact-SQL statement within a stored
  
  pro
tags:
  - "event-classes"
  - "spstmtcompleted-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:StmtCompleted event class indicates that a Transact-SQL statement within a stored

procedure has completed.

Description

ApplicationName

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

CPU

Amount of CPU time (in milliseconds) used by

the event.

18

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

Duration

Amount of time (in microseconds) taken by the

event.

13

Yes

EndTime

Time at which the event ended. This column is

not populated for starting event classes, such as

SQL:BatchStarting or SP:Starting.

15

Yes

EventClass

Type of event = 45.

27

No

EventSequence

Sequence of a given event within the request.

51

No

GroupID

ID of the workload group where the SQL Trace

66

Yes

ﾉ

Expand table