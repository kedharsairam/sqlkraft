---
title: "Server Memory Change Event Class"
topic: "event-classes"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The

  event class occurs when Microsoft SQL Server memory usage has

  increased or decreased by either 1
tags:
  - "event-classes"
  - "server-memory-change-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

event class occurs when Microsoft SQL Server memory usage has

increased or decreased by either 1 megabyte (MB) or 5 percent of the maximum server

memory, whichever is greater.

Description

Type of event = 81.

27

No

Sequence of a given event within the request.

51

No

Type of event subclass.

1=Memory Increase

2=Memory Decrease

21

Yes

New memory size, in megabytes (MB).

25

Yes

Indicates whether the event occurred on a system

process or a user process. 1 = system, 0 = user.

60

Yes

ID of the request containing the statement.

49

Yes

Name of the instance of SQL Server being traced.

26

No

The login name of the user who originated the

session. For example, if you connect to SQL Server

using Login1 and execute a statement as Login2,

shows Login1 and

shows Login2. This column displays both SQL Server

and Windows logins.

64

Yes

ID of the session on which the event occurred.

12

Yes

Time at which the event started, if available.

14

Yes

System-assigned ID of the transaction.

4

Yes

ﾉ

Expand table
