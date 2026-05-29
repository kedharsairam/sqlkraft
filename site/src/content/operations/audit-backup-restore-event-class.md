---
title: "Audit Backup & Restore Event Class"
topic: "event-classes"
description: |
  Article

  •

  08/27/2024

  Applies to:

  SQL Server

  The

  event class occurs whenever a backup or restore command is

  issued.

  Description

  Name of the client application that created the

  connection to a
tags:
  - "event-classes"
  - "audit-backup-restore-event-class"
pubDate: 2025-12-01
---

Article

•

08/27/2024

Applies to:

SQL Server

The

event class occurs whenever a backup or restore command is

issued.

Description

Name of the client application that created the

connection to an instance of Microsoft SQL

Server. This column is populated with the values

passed by the application rather than the

displayed name of the program.

10

Yes

ID assigned by the host computer to the

process where the client application is running.

This data column is populated if the client

provides the client process ID.

9

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

The issuer's username in the database.

40

Yes

Type of event = 115.

27

No

Sequence of a given event within the request.

51

No

Type of event subclass.

1=Backup

21

Yes

ﾉ

Expand table
