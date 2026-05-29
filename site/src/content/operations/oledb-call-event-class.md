---
title: "OLEDB Call Event Class"
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

  event class occurs when SQL Server calls an OLE DB provider for distributed

  queries and remote st
tags:
  - "event-classes"
  - "oledb-call-event-class"
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

event class occurs when SQL Server calls an OLE DB provider for distributed

queries and remote stored procedures.

Include the

event class in traces to monitor only those calls that do not request

data or calls that are not made to the

method. When the

event

class is included in a trace the amount of overhead incurred depends on how frequently OLE

DB calls occur against the database during the trace. If calls occur frequently, the trace may

significantly impede performance.

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

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

DatabaseID

ID of the database specified by the USE

database

statement or the default database if

no USE

database

statement has been issued for

a given instance. SQL Server Profiler displays the

name of the database if the

data

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

Duration

Length of time to complete the OLE DB Call

event.

13

No

ﾉ

Expand table
