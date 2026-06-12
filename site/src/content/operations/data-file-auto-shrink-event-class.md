---
title: "Data File Auto Shrink Event Class"
topic: "event-classes"
description: "The event class indicates that the data file has been shrunk. This event is not triggered i"
tags: ["event-classes","data-file-auto-shrink-event-class"]
pubDate: 2025-12-01
---

The

event class indicates that the data file has been shrunk. This event is

not triggered if the data file shrinks because of an explicit ALTER DATABASE statement. Include

the

event class in traces that monitor the data file size changes.

When the

event class is included in a trace, the amount of overhead

incurred is low unless the data file frequently shrinks.

Description

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

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

Time (in milliseconds) to shrink the file.

13

Yes

Time that the auto shrink ended.

18

Yes

Type of event recorded = 94.

27

No

ﾉ

Expand table
