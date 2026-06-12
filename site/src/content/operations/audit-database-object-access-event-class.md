---
title: "Audit Database Object Access Event Class"
topic: "event-classes"
description: "The event class occurs when database objects, such as schemas, are accessed."
tags: ["event-classes","audit-database-object-access-event-class"]
pubDate: "2025-12-01"
---

The

event class occurs when database objects, such as schemas,

are accessed.

Description

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

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

user name of the client.

40

Yes

Sequence of a given event within the request.

51

No

Name of the computer on which the client is

running. This data column is populated if the

client provides the host name. To determine the

host name, use the HOST_NAME function.

8

Yes

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

= user.

60

Yes

ﾉ

Expand table
