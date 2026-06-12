---
title: "RPC:Completed Event Class"
topic: "event-classes"
description: "The event class indicates that a remote procedure call has been completed. Description Nam"
tags: ["event-classes","rpccompleted-event-class"]
pubDate: "2025-12-01"
---

The

event class indicates that a remote procedure call has been completed.

Description

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name of

the program.

10

Yes

Binary value dependent on the event class

captured in the trace.

2

Yes

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client process ID is

provided by the client.

9

Yes

Amount of CPU time used by the event. In

microseconds beginning with SQL Server 2012

(11.x). In milliseconds in earlier versions.

18

Yes

ID of the database specified by the

statement or the default database if

no

statement has been issued for

a given instance. SQL Server Profiler displays the

name of the database if the ServerName data

column is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

Name of the database in which the user

statement is running.

35

Yes

Amount of time taken by the event. In

microseconds beginning with SQL Server 2008 R2

(10.50.x). In milliseconds in earlier versions.

13

Yes

ﾉ

Expand table

```cmd
RPC:Completed
ApplicationName
BinaryData
ClientProcessID
CPU
```
