---
title: "Showplan All for Query Compile Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Showplan All for Query Compile event class occurs when Microsoft SQL Server compiles a
  
  S
tags:
  - "event-classes"
  - "showplan-all-for-query-compile-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Showplan All for Query Compile event class occurs when Microsoft SQL Server compiles a

SQL statement. Include this event class to identify the Showplan operators. The information

included is a subset of the information available in the Showplan XML For Query Compile event

class.

The Showplan All for Query Compileevent class displays complete, compile-time data, and so

traces that contain Showplan All for Query Compile may incur significant performance

overhead. To minimize this, limit use of this event class to traces monitoring specific problems

for brief periods of time.

When the Showplan All for Query Compile event class is included in a trace, the BinaryData

data column must be selected. If it is not, information for this event class will not be displayed

in the trace.

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

3

Yes

ﾉ

Expand table