---
title: "FT:Crawl Stopped Event Class"
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

  event class indicates that a full-text crawl (population) has stopped. The

  stop can be due to a s
tags:
  - "event-classes"
  - "ftcrawl-stopped-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

event class indicates that a full-text crawl (population) has stopped. The

stop can be due to a successfully completed crawl or a fatal error.

Description

ID of the database in which the full-text crawl

has stopped. Determine the value for a

database by using the DB_ID function.

3

Yes

Type of event = 156.

27

No

Sequence of a given event within the request.

51

No

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

= user.

60

Yes

System-assigned ID of the object. The full-text

crawl has stopped for the full-text index on this

object.

22

Yes

Login name of the user who originated the

session. For example, if you connect to SQL

Server using Login1 and execute a statement as

Login2,

shows Login1 and

shows Login2. This column displays

both SQL Server and Microsoft Windows logins.

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

sp_trace_setevent (Transact-SQL)

ﾉ

Expand table
