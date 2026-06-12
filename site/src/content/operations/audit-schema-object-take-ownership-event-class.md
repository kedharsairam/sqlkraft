---
title: "Audit Schema Object Take Ownership Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","audit-schema-object-take-ownership-event-class"]
pubDate: "2025-12-01"
---

The

event class occurs when the permissions to change

the owner of schema object (such as a table, procedure, or function) is checked. This happens

when the ALTER AUTHORIZATION statement is used to assign an owner to an object.

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

ﾉ

Expand table
