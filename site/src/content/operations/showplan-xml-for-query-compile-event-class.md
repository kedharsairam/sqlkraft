---
title: "Showplan XML for Query Compile Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The Showplan XML For Query Compile event class occurs when Microsoft SQL Server compiles

  a S
tags:
  - "event-classes"
  - "showplan-xml-for-query-compile-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Showplan XML For Query Compile event class occurs when Microsoft SQL Server compiles

a SQL statement. Include this event class to identify the Showplan operators on Microsoft SQL

Server.

The Showplan XML For Query Compile event class displays complete, compile time data, so

traces that contain this event class can incur significant performance overhead. To minimize

this, limit use of this event class to traces that monitor specific problems for brief periods of

time.

The Showplan XML documents have a schema associated with them. This schema can be found

at the

Microsoft Web Site

, or as part of your SQL Server installation.

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

Estimated cost of the query.

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

3

Yes

ﾉ

Expand table
