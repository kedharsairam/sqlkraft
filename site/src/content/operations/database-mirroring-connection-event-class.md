---
title: "Database Mirroring Connection Event Class"
topic: "event-classes"
description: "generates a event to report the status of a transport connection managed by Database Mirroring."
tags: ["event-classes","database-mirroring-connection-event-class"]
pubDate: "2025-12-01"
---

generates a

event to report the status of a

transport connection managed by Database Mirroring.

Description

The name of the client application that

created the connection to an instance of. This column is populated with

the values passed by the application

rather than the displayed name of the

program.

10

Yes

The ID assigned by the host computer to

the process where the client application is

running. This data column is populated if

the client process ID is provided by the

client.

9

Yes

The ID of the database specified by the

USE

database

statement, or the ID of the

default database if no USE

database

statement has been issued for a

given instance. SQL Server Profiler

displays the name of the database if the

data column is captured in

the trace and the server is available.

Determine the value for a database by

using the

function.

3

Yes

The message ID number in

for the text in the event. If this event

reports an error, this is the SQL Server

error number.

31

No

The type of event class captured. Always

27

No

ﾉ

Expand table
