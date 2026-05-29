---
title: "Progress Report: Online Index Operation Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Progress Report: Online Index Operation event class indicates the progress of an online
  
  
tags:
  - "event-classes"
  - "progress-report-online-index-operation-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Progress Report: Online Index Operation event class indicates the progress of an online

index build operation while the build process is running.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

BigintData1

Number of rows inserted.

52

Yes

BigintData2

0 = serial plan; otherwise, the thread ID during

parallel execution.

53

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

statement or the default database if no USE

database

statement has been issued for a given

instance. SQL Server Profiler displays the name

of the database if the ServerName data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the user

statement is running.

35

Yes

ﾉ

Expand table