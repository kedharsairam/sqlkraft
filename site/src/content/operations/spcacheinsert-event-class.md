---
title: "SP:CacheInsert Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The SP:CacheInsert event class indicates that the stored procedure has been inserted into the
tags:
  - "event-classes"
  - "spcacheinsert-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:CacheInsert event class indicates that the stored procedure has been inserted into the

procedure cache.

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

Type of event = 35.

27

No

EventSequence

The sequence of a given event within the

request.

51

No

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

client provides the host name. To determine the

host name, use the HOST_NAME function.

8

Yes

IsSystem

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

60

Yes

ﾉ

Expand table
