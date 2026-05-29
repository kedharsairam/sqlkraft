---
title: "Lock:Released Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Lock:Released event class indicates that a lock on a reso
tags:
  - "event-classes"
  - "lockreleased-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The Lock:Released event class indicates that a lock on a resource, such as a page, has been

released.

The Lock:Acquired and Lock:Released event classes can be used to monitor when objects are

being locked, the type of locks taken, and for how long the locks were retained. Locks retained

for long periods of time may cause contention issues and should be investigated. For example,

an application can be acquiring locks on rows in a table, and then waiting for user input.

Because the user input can take a long time to occur, the locks can block other users. In this

instance, the application should be redesigned to make lock requests only when needed and

not require user input when locks have been acquired.

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

ID of the database in which the lock was

released. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

EventClass

Type of event = 23.

27

No

EventSequence

Sequence of a given event within the request.

51

No

ﾉ

Expand table