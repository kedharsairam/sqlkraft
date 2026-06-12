---
title: "CLR Event Category"
topic: "event-classes"
description: "The event category includes event classes that are produced by the execution of .NET Framework common"
tags: ["event-classes","clr-event-category"]
pubDate: 2025-12-01
---

The

event category includes event classes that are produced by the execution of.NET

Framework common language runtime (CLR) objects inside SQL Server.

The

event class occurs when a request to load an assembly is executed.

Include the

event class in traces where you want to monitor assembly loads.

This can be useful when troubleshooting a query that uses common language runtime (CLR),

when troubleshooting a slow running server that is running CLR queries, or when monitoring a

server to gather user, database, success, or other information about assembly loads.

Description

The name of the application that requested the

load.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

Yes

ID of the database specified by the USE

database statement or the default database if

no USE database statement has been issued for

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

Sequence of a given event within the request.

51

No

ﾉ

Expand table
