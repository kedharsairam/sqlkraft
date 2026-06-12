---
title: "TM: Save Tran Starting Event Class"
topic: "event-classes"
description: "The TM: Save Tran Starting event class indicates that a SAVE TRANSACTION request is starting."
tags: ["event-classes","tm-save-tran-starting-event-class"]
pubDate: "2025-12-01"
---

The TM: Save Tran Starting event class indicates that a SAVE TRANSACTION request is starting.

The request is sent from the client through a transaction management interface.

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

column is populated if the client process ID is

provided by the client.

9

Yes

DatabaseID

ID of the database specified by the USE

database

statement or the default database if no

USE

database

statement has been issued for a

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

EventClass

Type of event = 191.

27

No

EventSequence

The sequence of a given event within the

request.

51

No

GroupID

ID of the workload group where the SQL Trace

event fires.

66

Yes

HostName

Name of the computer on which the client is

running. This data column is populated if the

8

Yes

ﾉ

Expand table
