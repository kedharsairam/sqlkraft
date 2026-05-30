---
title: "Sort Warnings Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The Sort Warnings event class indicates that sort operations do not fit into memory. This doe
tags:
  - "event-classes"
  - "sort-warnings-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Sort Warnings event class indicates that sort operations do not fit into memory. This does

not include sort operations involving the creation of indexes, only sort operations within a

query (such as an ORDER BY clause used in a SELECT statement).

If a query involving a sort operation generates a Sort Warnings event class with an

EventSubClass data column value of 2, the performance of the query can be affected because

multiple passes over the data are required to sort the data. Investigate the query further to

determine if the sort operation can be eliminated.

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

Type of event = 69.

27

No

ﾉ

Expand table
