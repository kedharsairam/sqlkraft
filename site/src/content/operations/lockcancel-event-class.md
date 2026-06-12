---
title: "Lock:Cancel Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","lockcancel-event-class"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

The

event class indicates that acquisition of a lock on a resource has been

canceled; for example, due to a query being canceled.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

Lock resource identifier.

2

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ID of the database in which the lock was

acquired. SQL Server Profiler displays the name

of the database if the

data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

Name of the database in which the lock acquire

was attempted.

35

Yes

Amount of time (in microseconds) between the

time the lock request was issued and the time

the lock was canceled.

13

Yes

Time at which the event ended.

15

Yes

Type of event = 26.

27

No

Sequence of a given event within the request.

51

No

ﾉ

Expand table
