---
title: "Execution Warnings Event Class"
topic: "event-classes"
description: ""
tags: ["event-classes","execution-warnings-event-class"]
pubDate: "2025-12-01"
---

The Execution Warnings event class indicates memory grant warnings that occurred during the

execution of a SQL Server statement or stored procedure. This event class can be monitored to

determine if queries had to wait one second or more for memory before proceeding, or if the

initial attempt to get memory failed. Information about query wait periods can help uncover

contention issues in the system that can affect performance.

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

Duration

Time (in milliseconds) that the query had to wait

to get the required memory. Valid only when

EventSubClass = 1 (Query wait).

13

Yes

Error

Not used.

31

Yes

ﾉ

Expand table
