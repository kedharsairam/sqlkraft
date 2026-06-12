---
title: "Audit Login Event Class"
topic: "event-classes"
description: "The event class indicates that a user has successfully logged in to Microsoft SQL Server. Events in t"
tags: ["event-classes","audit-login-event-class"]
pubDate: "2025-12-01"
---

The

event class indicates that a user has successfully logged in to Microsoft SQL

Server. Events in this class are fired by new connections or by connections that are reused from

a connection pool.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

Session level settings, including ANSI nulls,

ANSI padding, cursor close on commit, null

concatenation, and quoted identifiers.

2

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

Type of event = 14.

27

No

Sequence of a given event within the request.

51

No

ﾉ

Expand table
