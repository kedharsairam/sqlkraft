---
title: "Attention Event Class"
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
  
  event class indicates that an attention event, such as cancel, client-interrupt
  
  requests, or brok
tags:
  - "event-classes"
  - "attention-event-class"
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

event class indicates that an attention event, such as cancel, client-interrupt

requests, or broken client connections, has occurred. Cancel operations can also be seen as

part of implementing data access driver time-outs.

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

Amount of time (in microseconds) taken by the

event.

13

Yes

End time of the interrupted action.

15

Yes

Type of event = 16.

27

No

Sequence of a given event within the request.

51

No

ﾉ

Expand table