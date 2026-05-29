---
title: "Audit Login GDR Event Class"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  The
  
  event class occurs whenever a Microsoft Windows login right is added or
  
  removed. This event class
tags:
  - "event-classes"
  - "audit-login-gdr-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

event class occurs whenever a Microsoft Windows login right is added or

removed. This event class is for the

,

, and

stored

procedures.

This event class may be removed in a future version of SQL Server. It is recommended that you

use the

event class instead.

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

process ID is provided by the client.

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

Type of event = 105.

27

No

Sequence of a given event within the request.

51

No

Type of event subclass.

21

Yes

ﾉ

Expand table