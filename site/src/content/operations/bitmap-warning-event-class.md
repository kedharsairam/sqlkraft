---
title: "Bitmap Warning Event Class"
topic: "event-classes"
description: "The event class can be used to monitor bitmap filter usage in queries. The event subclass c"
tags: ["event-classes","bitmap-warning-event-class"]
pubDate: 2025-12-01
---

The

event class can be used to monitor bitmap filter usage in queries. The

event subclass can be used to report when bitmap filters have been disabled in a query.

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

Type of event = 212.

27

No

Sequence of a given event within the request.

51

No

Type of event subclass. 0 = bitmap filter is

disabled.

21

Yes

Name of the computer on which the client is

running. This data column is populated if the

host name is provided by the client. To

8

Yes

ﾉ

Expand table
