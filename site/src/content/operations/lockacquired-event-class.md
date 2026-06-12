---
title: "Lock:Acquired Event Class"
topic: "event-classes"
description: "2016 (13.x) and later versions Azure SQL Managed Instance The Lock:Acquired event class indicates that acquisition of a"
tags: ["event-classes","lockacquired-event-class"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

The Lock:Acquired event class indicates that acquisition of a lock on a resource, such as a data

page, has been achieved.

The Lock:Acquired and Lock:Released event classes can be used to monitor when objects are

being locked, the type of locks taken, and for how long the locks were retained. Locks retained

for long periods of time might cause contention issues and should be investigated. For

example, an application can be acquiring locks on rows in a table, and then waiting for user

input. Because the user input can take a long time to occur, the locks can block other users. In

this instance, the application should be redesigned to make lock requests only when needed

and not require user input when locks have been acquired.

Description

ApplicationName

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

Yes

BigintData1

Partition ID if the lock resource is partitioned.

52

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

ID of the database in which the lock was

acquired. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

Duration

Amount of time (in microseconds) between the

time the lock was acquired and the time the lock

13

Yes

ﾉ

Expand table
