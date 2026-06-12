---
title: "Unprepare SQL Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","unprepare-sql-event-class"]
pubDate: "2025-12-01"
---

The Unprepare SQL event class indicates that the SqlClient, ODBC, OLE DB, or DB-Library has

unprepared (deleted) a prepared Transact-SQL statement or statements.

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

column is populated if the client process ID is

provided by the client.

9

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

EventClass

Type of event = 73.

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

Handle

Handle of the prepared Transact-SQL statement.

33

Yes

ﾉ

Expand table
