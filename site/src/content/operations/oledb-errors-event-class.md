---
title: "OLEDB Errors Event Class"
topic: "event-classes"
description: "The OLEDB Errors event class occurs in Microsoft SQL Server when a call to an OLE DB provider returns"
tags: ["event-classes","oledb-errors-event-class"]
pubDate: "2025-12-01"
---

The OLEDB Errors event class occurs in Microsoft SQL Server when a call to an OLE DB provider

returns an error. Include this event class in traces to view a failed HRESULT from an OLE DB

provider.

When the OLEDB Errors event class is included in a trace, the amount of overhead depends on

how frequently OLE DB provider errors occur against the database during the trace. If such

errors occur frequently, the trace might significantly impede performance.

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

statement or the default

database

if no

USE database statement has been issued for a

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

Error

The HRESULT returned by the provider.

31

Yes

EventClass

Type of event = 61.

27

No

ﾉ

Expand table
