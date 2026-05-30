---
title: "Blocked Process Report Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class indicates that a task has been blocked for more than a

  specified amount of
tags:
  - "event-classes"
  - "blocked-process-report-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates that a task has been blocked for more than a

specified amount of time. This event class does not include system tasks or tasks that are

waiting on non deadlock-detectable resources.

To configure the threshold and frequency at which reports are generated, use the

command to configure the

option, which can be set in seconds. By

default, no blocked process reports are produced. For more information about setting the

option, see

blocked process threshold Server Configuration Option

.

For information about filtering the data returned by the

event class,

see

Filter Events in a Trace (SQL Server Profiler)

,

Set a Trace Filter (Transact-SQL)

, or

sp_trace_setfilter (Transact-SQL)

.

Description

ID of the database in which the lock was

acquired. SQL Server Profiler displays the name

of the database if the

data column

is captured in the trace and the server is

available. Determine the value for a database by

using the DB_ID function.

3

Yes

The amount of time (in microseconds) that the

process was blocked.

13

Yes

Time at which the event ended. This column is

not populated for starting event classes, such as

SQL:BatchStarting

or

.

15

Yes

Type of event = 137.

27

No

The sequence of a given event within the

request.

51

No

ID for the index on the object affected by the

event. To determine the index ID for an object,

24

Yes

ﾉ

Expand table
