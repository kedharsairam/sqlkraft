---
title: "User-Configurable Event Class"
topic: "event-classes"
description: "Use the User-Configurable event category to monitor user-defined events. Create user-defined"
tags: ["event-classes","user-configurable-event-class"]
pubDate: "2025-12-01"
---

Use the User-Configurable event category to monitor user-defined events. Create user-defined

event classes to monitor events that cannot be monitored by the system-supplied event classes

in other event categories. For example, a user-defined event can be created to monitor the

progress of the application you are testing. As the application runs, it can generate events at

predefined points, allowing you to determine the current execution point in your application.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application rather than the displayed name

of the program.

10

Yes

BinaryData

Binary value dependent on the event class

captured in the trace.

2

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

Type of event = 82-91.

27

No

ﾉ

Expand table
