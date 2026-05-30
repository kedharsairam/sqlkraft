---
title: "SQL:FullTextQuery Event Class"
topic: "event-classes"
description: |
  SQL:FullTextQuery Event Class

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The SQL:FullTextQuery event class occurs when SQL Server execu
tags:
  - "event-classes"
  - "sqlfulltextquery-event-class"
pubDate: 2025-12-01
---

SQL:FullTextQuery Event Class

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SQL:FullTextQuery event class occurs when SQL Server executes a full text query. Include

this event class in traces that are monitoring problems associated with full text catalogs.

When the SQL:FullTextQuery event class is included, the amount of overhead will be high. If

such events occur frequently, the trace may significantly impede performance. To minimize this,

limit the use of this event class to traces that monitor specific problems for brief periods of

time.

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

Duration

Length of time to complete the Full Text Query.

13

No

EndTime

Time event ended

15

Yes

SQL:FullTextQuery Event Class Data Columns

ﾉ

Expand table
