---
title: "RPC Output Parameter Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The RPC Output Parameter event class traces the output parameter values of remote procedure

tags:
  - "event-classes"
  - "rpc-output-parameter-event-class"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The RPC Output Parameter event class traces the output parameter values of remote procedure

calls (RPCs) after execution.

Use this class to examine the output values returned by stored procedures. For example, if an

application is not producing the expected output values after executing a remote procedure

call, you can use this event class to help isolate the problem between the client code and the

server code.

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

EventClass

Type of event = 100.

27

No

EventSequence

Sequence of a given event within the request.

51

No

ﾉ

Expand table
