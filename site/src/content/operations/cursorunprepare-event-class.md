---
title: "CursorUnprepare Event Class"
topic: "event-classes"
description: "The event class provides information about cursor unprepare events that occur in applicatio"
tags: ["event-classes","cursorunprepare-event-class"]
pubDate: "2025-12-01"
---

The

event class provides information about cursor unprepare events that

occur in application programming interface (API) cursors. Cursor unprepare events occur when

the Microsoft Database Engine discards an execution plan.

Include the

event class in traces that record the performance of cursors.

When the

event class is included in a trace, the amount of overhead incurred

depends on how frequently cursors are used against the database during the trace. If cursors

are used extensively, the trace can significantly impede performance.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than with the displayed

name of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ID of the database specified by the USE

statement or the default database if no USE

statement has been issued for a given instance.

Profiler displays the name of the

database if the

data column is

captured in the trace and the server is available.

Determine the value for a database by using the

DB_ID function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

Type of event recorded = 77.

27

No

ﾉ

Expand table
