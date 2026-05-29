---
title: "Lock:Deadlock Chain Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Lock:Deadlock Chain event class is produced for each part
tags:
  - "event-classes"
  - "lockdeadlock-chain-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

The Lock:Deadlock Chain event class is produced for each participant in a deadlock.

Use the Lock:Deadlock Chain event class to monitor when deadlock conditions occur. This

information is useful to determine if deadlocks are significantly affecting the performance of

your application, and which objects are involved. You can examine the application code that

modifies these objects to determine if changes to minimize deadlocks can be made.

Description

BinaryData

Lock resource identifier.

2

Yes

DatabaseID

ID of the database to which this resource

belongs. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database to which the resource

belongs.

35

Yes

EventClass

Type of event = 59.

27

No

EventSequence

Sequence of a given event within the request.

51

No

EventSubClass

Type of event subclass.

101=Resource type Lock

102=Resource type Exchange

21

Yes

IntegerData

Deadlock number. Numbers are assigned

beginning with 0 when the server is started, and

incremented for each deadlock.

25

Yes

IntegerData2

Identified for informational purposes only. Not

supported. Future compatibility is not

55

Yes

ﾉ

Expand table