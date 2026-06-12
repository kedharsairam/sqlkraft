---
title: "SQLTransaction Event Class"
topic: "event-classes"
description: "SQLTransaction Event Class Use the SQLTransaction event class to monitor when transactions b"
tags: ["event-classes","sqltransaction-event-class"]
pubDate: 2025-12-01
---

SQLTransaction Event Class

Use the SQLTransaction event class to monitor when transactions begin and are completed,

especially when you test applications, triggers, or stored procedures.

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

Type of event = 50.

27

No

EventSequence

Sequence of a given event within the request.

51

No

SQLTransaction Event Class Data Columns

ﾉ

Expand table
