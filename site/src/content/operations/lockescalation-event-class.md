---
title: "Lock:Escalation Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","lockescalation-event-class"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

The

event class indicates that a finer-grained lock has been converted to a

coarser-grained lock; for example, a row lock that is converted to an object lock. The escalation

event class is Event ID 60.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

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

Name of the database in which the escalation

occurred.

35

Yes

Type of event = 60.

27

No

Cause of the lock escalation:

indicates the statement

exceeded the lock threshold.

indicates the

statement exceeded the memory threshold.

21

Yes

ﾉ

Expand table
