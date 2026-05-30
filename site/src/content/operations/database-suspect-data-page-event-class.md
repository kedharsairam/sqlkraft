---
title: "Database Suspect Data Page Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class indicates when a page is added to the

  suspect_pages

  table in

  msdb

  . Incl
tags:
  - "event-classes"
  - "database-suspect-data-page-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates when a page is added to the

suspect_pages

table in

msdb

. Include this event class in traces that are monitoring the

occurrence of suspect pages.

When the

event class is included in a trace the relative overhead

is low. The overhead might be greater if the number of suspect pages increases, for example, if

a disk drive is experiencing problems.

Description

ID of the database for which the suspect page

event has been raised. This is the same as the

column of the

table.

3

Yes

The type of the event is 213.

27

No

Sequence of event class in batch.

51

No

ID of the SQL Server task that encountered the

suspect page.

12

Yes

Time that the event occurred.

14

Yes

ID of the database file that contains the suspect

page. This is the same as the

column of

the

table.

22

Yes

７

Note

This event is issued asynchronously from the insertion of a corresponding row into the

table. Therefore, a job listening on this event might not find the

corresponding

entry immediately.

ﾉ

Expand table
