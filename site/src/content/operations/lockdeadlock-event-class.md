---
title: "Lock:Deadlock Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  The Lock:Deadlock event class is produced when an attempt to
tags:
  - "event-classes"
  - "lockdeadlock-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The Lock:Deadlock event class is produced when an attempt to acquire a lock is canceled

because the attempt was part of a deadlock and was chosen as the deadlock victim.

Use the Lock:Deadlock event class to monitor when deadlocks occur and which objects are

involved. You can use this information to determine if deadlocks are significantly affecting the

performance of your application. You can then examine the application code to determine if

you can make changes to minimize deadlocks.

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

column is populated if the client process ID is

provided by the client.

9

Yes

DatabaseID

ID of the database in which the lock was being

acquired. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the lock was

being acquired.

35

Yes

Duration

Amount of time (in microseconds) between the

time the lock request was issued and the time

the deadlock occurred.

13

Yes

ﾉ

Expand table
