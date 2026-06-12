---
title: "Object:Deleted Event Class"
topic: "event-classes"
description: "The Object:Deleted event class indicates that an object has been deleted; for example, by DR"
tags: ["event-classes","objectdeleted-event-class"]
pubDate: "2025-12-01"
---

The Object:Deleted event class indicates that an object has been deleted; for example, by

DROP INDEX and DROP TABLE statements. This event class can be used to determine if objects

are being deleted, for example, by ODBC applications that often create temporary stored

procedures.

By monitoring the LoginName and NTUserName default data columns, in addition to the

Objects event classes, you can determine the name of the user who is creating, deleting, or

accessing objects.

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

Type of event = 47.

27

No

EventSequence

Sequence of a given event within the request.

51

No

ﾉ

Expand table
