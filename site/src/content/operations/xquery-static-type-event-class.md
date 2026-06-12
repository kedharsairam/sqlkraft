---
title: "XQuery Static Type Event Class"
topic: "event-classes"
description: "The XQuery Static Type event class occurs when SQL Server executes an XQuery expression. Thi"
tags: ["event-classes","xquery-static-type-event-class"]
pubDate: "2025-12-01"
---

The XQuery Static Type event class occurs when SQL Server executes an XQuery expression.

This event class provides the static type of the XQuery expression.

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

Type of event = 198.

27

No

EventSequence

The sequence of a given event within the

request.

51

No

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

8

Yes

ﾉ

Expand table
