---
title: "Lock:Timeout Event Class"
topic: "event-classes"
description: "2016 (13.x) and later versions Azure SQL Managed Instance The Lock:Timeout event class indicates that a request for a l"
tags: ["event-classes","locktimeout-event-class"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

The Lock:Timeout event class indicates that a request for a lock on a resource, such as a page,

has timed out because another transaction is holding a blocking lock on the required resource.

Time-out is determined by the @@LOCK_TIMEOUT system function and can be set with the

SET LOCK_TIMEOUT statement.

Use the Lock:Timeout event class to monitor when time-out conditions occur. This information

is useful to determine if time-outs are significantly affecting the performance of your

application, and which objects are involved. You can examine the application code that

modifies these objects to determine if changes to minimize time-outs can be made.

Lock:Timeout events with a duration of 0 are commonly the result of internal lock probes and

are not necessarily an indication of a problem. The Lock:Timeout (timeout > 0) event can be

used to ignore time-outs with a duration of 0.

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

Lock resource identifier.

2

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client provides the

client process ID.

9

Yes

DatabaseID

ID of the database in which the lock time-out

occurred. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

ﾉ

Expand table
