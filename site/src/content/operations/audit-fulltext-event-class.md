---
title: "Audit Fulltext Event Class"
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

  event class occurs when SQL Server connects to and communicates with the

  full-text filter daemon
tags:
  - "event-classes"
  - "audit-fulltext-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The

event class occurs when SQL Server connects to and communicates with the

full-text filter daemon process.

Description

The SQL Server error number, if this event

reports an error.

31

Yes

The sequence of a given event within the

request.

51

No

Type of connection used by the login. 1 =

Nonpooled, 2 = Pooled.

21

Yes

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

= user.

60

Yes

Login name of the user who originated the

session. For example, if you connect to SQL

Server using Login1 and execute a statement as

Login2,

shows Login1 and

shows Login2. This column displays

both SQL Server and Windows logins.

64

Yes

ID of the session on which the event occurred.

12

Yes

Time at which the event started, if available.

14

Yes

1 = success. 0 = failure. For example, a value of

1 indicates success of a permissions check and

a value of 0 indicates failure of that check.

23

Yes

For actions that target a login (for example,

adding a new login), the name of the targeted

login.

42

Yes

For actions that target a login (for example,

adding a new login), the security identification

43

Yes

ﾉ

Expand table
