---
title: "SP:CacheHit Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The SP:CacheHit event class indicates that a stored procedure is in the plan cache.

  Descript
tags:
  - "event-classes"
  - "spcachehit-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:CacheHit event class indicates that a stored procedure is in the plan cache.

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

Type of event = 38.

27

No

EventSequence

The sequence of a given event within the

request.

51

No

EventSubClass

1=Execution Context Hit: A free execution plan

was found in the plan cache.

2=Compplan Hit: A compiled plan was found in

the plan cache.

21

Yes

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

8

Yes

ﾉ

Expand table
