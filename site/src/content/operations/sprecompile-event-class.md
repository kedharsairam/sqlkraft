---
title: "SP:Recompile Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The SP:Recompile event class indicates that a stored procedure, trigger, or user-defined
  
  fun
tags:
  - "event-classes"
  - "sprecompile-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SP:Recompile event class indicates that a stored procedure, trigger, or user-defined

function has been recompiled. Recompilations reported by this event class occur at the

statement level.

The preferred way to trace statement-level recompilations is to use the SQL:StmtRecompile

event class. The SP:Recompile event class is deprecated. For more information, see

SQL:StmtRecompile Event Class

.

Description

ApplicationName

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the process ID.

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

Type of event = 37.

27

No

EventSequence

The sequence of a given event within the

request.

51

No

EventSubClass

Type of event subclass. Indicates the reason for

recompilation.

1 = Schema Changed

21

Yes

ﾉ

Expand table