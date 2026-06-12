---
title: "Audit Change Audit Event Class"
topic: "event-classes"
description: "The event class occurs whenever an audit trace modification is made. Description Name of the client"
tags: ["event-classes","audit-change-audit-event-class"]
pubDate: "2025-12-01"
---

The

event class occurs whenever an audit trace modification is made.

Description

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the

values passed by the application rather than

the displayed name of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

Indicator of whether a column permission was

set. Parse the statement text to determine

which permissions were applied to which

columns.

44

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

user name of the client.

40

Yes

Type of event = 117.

27

No

Sequence of a given event within the request.

51

No

ﾉ

Expand table
