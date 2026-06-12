---
title: "TM: Commit Tran Completed Event Class"
topic: "event-classes"
description: "The TM: Commit Tran Completed event class indicates that a COMMIT TRANSACTION request comple"
tags: ["event-classes","tm-commit-tran-completed-event-class"]
pubDate: 2025-12-01
---

The TM: Commit Tran Completed event class indicates that a COMMIT TRANSACTION request

completed. The request was sent from the client through the transaction management

interface. The EventSubClass column indicates if a new transaction will be started after the

current transaction is committed.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This column

is populated with the values passed by the application

rather than the displayed name of the program.

10

Yes

ClientProcessID

ID assigned by the host computer to the process

where the client application is running. This data

column is populated if the client process ID is provided

by the client.

9

Yes

DatabaseID

ID of the database specified by the USE database

statement or the default database if no USE database

statement has been issued for a given instance. SQL

Server Profiler displays the name of the database if the

ServerName data column is captured in the trace and

the server is available. Determine the value for a

database by using the DB_ID function.

3

Yes

DatabaseName

Name of the database in which the user statement is

running.

35

Yes

Error

Error number of a given event. Often this is the error

number stored in the sys.messages catalog view.

31

Yes

EventClass

Type of event = 186.

27

No

EventSequence

The sequence of a given event within the request.

51

No

ﾉ

Expand table
