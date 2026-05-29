---
title: "FT:Crawl Aborted Event Class"
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
  
  event class indicates that an exception has been encountered during a
  
  full-text crawl. The error 
tags:
  - "event-classes"
  - "ftcrawl-aborted-event-class"
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

event class indicates that an exception has been encountered during a

full-text crawl. The error usually causes the full-text crawl to stop. Check the Microsoft

Windows event log or the crawl log for more detailed error information.

Description

ID of the database in which the full-text crawl is

running. Determine the value for a database by

using the DB_ID function.

3

Yes

Error number of a given event. Often this is the

error number stored in the

table.

31

Yes

Type of event = 157.

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

System-assigned ID of the object on which the

full-text crawl is running when the failure

occurs.

22

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

Equivalent to an error state code.

30

Yes

ﾉ

Expand table