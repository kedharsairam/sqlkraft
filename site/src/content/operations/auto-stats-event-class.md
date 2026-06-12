---
title: "Auto Stats Event Class"
topic: "event-classes"
description: "The event class indicates that an automatic updating of index and column statistics has occurred. al"
tags: ["event-classes","auto-stats-event-class"]
pubDate: "2025-12-01"
---

The

event class indicates that an automatic updating of index and column statistics

has occurred.

also fires when statistics are being loaded for use by the optimizer.

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

Identifier of the database specified by the USE

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

Amount of time (in microseconds) taken by the

event.

13

Yes

Time at which the event ended.

15

Yes

Error number of a given event. Often this is the

error number stored in the

catalog view.

31

Yes

Type of event = 58.

27

No

ﾉ

Expand table
