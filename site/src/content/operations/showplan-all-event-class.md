---
title: "Showplan All Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The Showplan All event class occurs when Microsoft SQL Server executes a SQL statement. The

tags:
  - "event-classes"
  - "showplan-all-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Showplan All event class occurs when Microsoft SQL Server executes a SQL statement. The

information included is a subset of the information available in the Showplan XML Statistics

Profile or Showplan XML event class.

The Showplan All event class displays complete, compile-time data, and so traces that contain

Showplan All may incur significant performance overhead. To minimize this, limit use of this

event class to traces that monitor specific problems for brief periods of time.

When the Showplan All event class is included in a trace, the BinaryData data column must be

selected. If it is not, information for this event class will not be displayed in the trace.

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

Estimated cost of the Showplan text.

2

No

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client process ID is

provided by the client.

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

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the user

35

Yes

ﾉ

Expand table
