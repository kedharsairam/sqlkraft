---
title: "Showplan XML Event Class"
topic: "event-classes"
description: "The Showplan XML event class occurs when Microsoft SQL Server executes a SQL statement. Incl"
tags: ["event-classes","showplan-xml-event-class"]
pubDate: "2025-12-01"
---

The Showplan XML event class occurs when Microsoft SQL Server executes a SQL statement.

Include the Showplan XML event class to identify the Showplan operators. This event class

stores each event as a well-defined XML document.

When the Showplan XML event class is included in a trace, the amount of overhead will

significantly impede performance. Showplan XML stores a query plan that is created when the

query is optimized. To minimize the overhead incurred, limit use of this event class to traces

that monitor specific problems for brief periods of time.

The Showplan XML documents have a schema associated with them. This schema can be found

at the

Microsoft Web Site

, or as part of your Microsoft SQL Server installation.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

BinaryData

Estimated cost of the query.

2

No

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

ﾉ

Expand table
