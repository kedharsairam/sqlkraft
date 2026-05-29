---
title: "Showplan Text (Unencoded) Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Showplan Text (Unencoded) event class occurs when Microsoft SQL Server executes a SQL
  
  st
tags:
  - "event-classes"
  - "showplan-text-unencoded-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Showplan Text (Unencoded) event class occurs when Microsoft SQL Server executes a SQL

statement. This event class is the same as the Showplan Text event class, except the event

information is formatted as a string rather than as binary data.

The information included is a subset of the information available in Showplan All, Showplan

XML, or Showplan XML Statistics Profile event classes.

When the Showplan Text (Unencoded) event class is included in a trace, the amount of

overhead can significantly impede performance. Showplan Text (Unencoded) will not incur as

much overhead as other Showplan event classes. To minimize overhead incurred, limit the use

of this event class to traces that monitor specific problems for brief periods of time.

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

Binary value dependent on the event class

captured in the trace.

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

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

given instance. SQL Server Profiler displays the

name of the database if the ServerName data

column is captured in the trace and the server is

3

Yes

ﾉ

Expand table