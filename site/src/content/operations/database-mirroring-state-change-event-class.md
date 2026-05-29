---
title: "Database Mirroring State Change Event Class"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  The
  
  event class indicates when the state of a mirrored
  
  database changes. Include this event class in traces that are monitoring c
tags:
  - "event-classes"
  - "database-mirroring-state-change-event-class"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

The

event class indicates when the state of a mirrored

database changes. Include this event class in traces that are monitoring conditions of mirrored

databases.

When the

event class is included in a trace the relative

overhead is low. The overhead may be greater if the state of the mirrored databases increase.

Description

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

Name of the mirrored database.

35

Yes

Type of event = 167.

27

No

Sequence of event class in batch.

51

No

Prior state ID.

25

Yes

Indicates whether the event occurred on a

system process or a user process. 1 = system, 0

= user.

60

Yes

Security identification number (SID) of the

logged-in user. You can find this information in

41

Yes

ﾉ

Expand table