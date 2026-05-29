---
title: "Object:Altered Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Object:Altered event class indicates that an object has been altered; for example, by an
  
tags:
  - "event-classes"
  - "objectaltered-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Object:Altered event class indicates that an object has been altered; for example, by an

ALTER INDEX, ALTER TABLE, or ALTER DATABASE statement. This event class can be used to

determine if objects are being altered; for example, by ODBC applications, which often create

temporary stored procedures.

The Object:Altered event class always occurs as two events. The first event indicates the Begin

phase. The second event indicates the Rollback or Commit phase.

By monitoring the LoginName and NTUserName data columns, you can determine the name of

the user who is creating, deleting, or altering objects.

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