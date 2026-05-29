---
title: "Log File Auto Grow Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The
  
  event class indicates that the log file grew automatically. This event is
  
  not triggered
tags:
  - "event-classes"
  - "log-file-auto-grow-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates that the log file grew automatically. This event is

not triggered if the log file is grown explicitly through ALTER DATABASE.

Include the

event class in traces that are monitoring the log file growth.

When this event class is included in a trace the amount of overhead incurred will be low unless

the log file is growing automatically frequently.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ID of the database specified by the USE

database

statement or the default database if

no USE

database

statement has been issued for

a given instance. SQL Server Profiler displays

the name of the database if the

data column is captured in the trace and the

server is available. Determine the value for a

database by using the DB_ID function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

Length of time (in milliseconds) necessary to

extend the file.

13

Yes

Time that the log file

ended.

18

Yes

ﾉ

Expand table