---
title: "Missing Column Statistics Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","missing-column-statistics-event-class"]
pubDate: "2025-12-01"
---

The Missing Column Statistics event class indicates that column statistics that could have been

useful for the optimizer are not available.

By monitoring the Missing Column Statistics event class, you can determine if there are

statistics missing for a column used by a query. This can cause the optimizer to choose a less

efficient query plan than expected.

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

Type of event=79.

27

No

EventSequence

Sequence of a given event within the request.

51

No

ﾉ

Expand table
