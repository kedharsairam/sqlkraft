---
title: "Trace File Close Event Class"
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
  
  event class indicates that a trace file has been closed during a trace file
  
  rollover.
  
  Descriptio
tags:
  - "event-classes"
  - "trace-file-close-event-class"
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

event class indicates that a trace file has been closed during a trace file

rollover.

Description

Type of event = 150.

27

No

The unique timestamp of this event fired in this

trace. This number increases monotonically for

each event fired.

51

No

The logical name of the trace file being closed.

36

Yes

Indicates whether the event occurred on a

system process or a user process. 1 = system,

NULL = user. The value is always 1 for this event

class.

60

Yes

Name of the login of the user (either SQL Server

security login or the Microsoft Windows login

credentials in the form of DOMAIN\username).

The value is always "sa" for this event class.

11

Yes

System-assigned ID of the trace.

22

Yes

Name of the instance of SQL Server being

traced.

26

No

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

ﾉ

Expand table