---
title: "OLEDB DataRead Event Class"
topic: "event-classes"
description: "The OLEDB DataRead event class occurs when SQL Server calls an OLE DB provider for distributed queries"
tags: ["event-classes","oledb-dataread-event-class"]
pubDate: 2025-12-01
---

The OLEDB DataRead event class occurs when SQL Server calls an OLE DB provider for

distributed queries and remote stored procedures. Include this event class in traces that

monitor when SQL Server makes a data request call to the OLE DB provider.

When the OLEDB DataRead class is included in a trace, the amount of overhead incurred will be

high. It is recommended that you limit the use of this event class to traces that monitor specific

problems for brief periods of time.

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

Length of time to complete the OLE DB Call

event.

13

No

EndTime

Time the event ended.

15

Yes

ﾉ

Expand table
