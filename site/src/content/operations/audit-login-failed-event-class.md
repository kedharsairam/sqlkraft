---
title: "Audit Login Failed Event Class"
topic: "event-classes"
description: |
  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The

  event class indicates that a user tried to sign in to Microsoft SQL Server

  and failed. Events in this class
tags:
  - "event-classes"
  - "audit-login-failed-event-class"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Managed Instance

The

event class indicates that a user tried to sign in to Microsoft SQL Server

and failed. Events in this class are fired by new connections or by connections that are reused

from a connection pool.

This event class is part of

SQL Trace

, which is deprecated. For Azure SQL Database, use

auditing

for Azure SQL Database

instead.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application instead of the displayed name

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

Error number of a given event. Often this is the

error number stored in the

catalog view.

31

Yes

ﾉ

Expand table
