---
title: "ExistingConnection Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The ExistingConnection event class indicates the properties of existing user connections when
tags:
  - "event-classes"
  - "existingconnection-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The ExistingConnection event class indicates the properties of existing user connections when

the trace was started. The server raises one ExistingConnection event per existing user

connection.

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

Binary dump of option flags such as session

level settings, including ANSI nulls, ANSI

padding, cursor close on commit, null

concatenation, and quoted identifiers.

2

Yes

ClientProcessID

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

DatabaseID

The current database ID of the user connection.

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

given instance. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the user

statement is running.

35

Yes

EventClass

Type of event = 17.

27

No

EventSequence

The sequence of this event within this trace.

51

No

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

ﾉ

Expand table
