---
title: "SP:CacheRemove Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The SP:CacheRemove event class indicates that the stored procedure has been removed from
  
  the
tags:
  - "event-classes"
  - "spcacheremove-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:CacheRemove event class indicates that the stored procedure has been removed from

the plan cache.

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

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

DatabaseID

ID of the database in which the stored

procedure is running. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the stored

procedure is running.

35

Yes

EventClass

Type of event = 36.

27

No

EventSequence

Sequence of a given event within the request.

51

No

EventSubClass

Type of event subclass.

1=Compplan Remove: A compiled query plan

has been removed from the cache.

2=Proc Cache Flush: All entries have been

removed from the procedure cache.

21

Yes

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

ﾉ

Expand table