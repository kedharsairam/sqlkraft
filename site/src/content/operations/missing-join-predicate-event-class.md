---
title: "Missing Join Predicate Event Class"
topic: "event-classes"
description: "The Missing Join Predicate event class indicates that a query is being executed that has no j"
tags: ["event-classes","missing-join-predicate-event-class"]
pubDate: "2025-12-01"
---

The Missing Join Predicate event class indicates that a query is being executed that has no join

predicate. This could result in a long-running query. For more information on join predicates,

see

Predicates (Transact-SQL).

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

EventClass

Type of event = 80.

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

8

Yes

ﾉ

Expand table
