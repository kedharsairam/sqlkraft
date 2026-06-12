---
title: "Mount Tape Event Class"
topic: "event-classes"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The Mount Tape event class occurs when a tape mount request is received. Use this event class

  to monit
tags:
  - "event-classes"
  - "mount-tape-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The Mount Tape event class occurs when a tape mount request is received. Use this event class

to monitor tape mount requests and their success or failure.

Description

ApplicationName

Name of the client application that created the

connection to an instance of SQL Server. This

column is populated with the values passed by

the application.

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

specified instance. SQL Server displays the name

of the database if the ServerName data column

is captured in the trace and the server is

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

Amount of time (in microseconds) taken by the

event.

13

Yes

EndTime

For Mount Request events, the time of the

mount time-out if a time-out occurs; otherwise,

the time of the event itself (in such cases,

StartTime indicates the time of the

corresponding mount request).

15

Yes

EventClass

Type of event = 195.

27

No

ﾉ

Expand table
