---
title: "CursorClose Event Class"
topic: "event-classes"
description: "Cursor close events occur when the Database Engine closes and deallocates a cursor."
tags: ["event-classes","cursorclose-event-class"]
pubDate: 2025-12-01
---

Cursor close events occur when the Database Engine closes and deallocates a cursor. The

event class describes cursor close events that occur in application programming

interface (API) cursors. This event class occurs when a Transact-SQL cursor statement by ODBC,

OLE DB, or DB-Library is closed.

Include the

event class in traces that are recording the performance of cursors.

The amount of overhead incurred depends on how frequently cursors are used against the

database during the trace. If cursors are used extensively, the trace can significantly impede

performance.

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

Type of event recorded = 78.

27

No

ﾉ

Expand table
