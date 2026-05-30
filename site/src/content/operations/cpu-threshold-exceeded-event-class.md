---
title: "CPU Threshold Exceeded Event Class"
topic: "event-classes"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The

  event class indicates that resource governor detected a batch

  request that exceeds the
tags:
  - "event-classes"
  - "cpu-threshold-exceeded-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The

event class indicates that resource governor detected a batch

request that exceeds the CPU threshold specified for the

argument

of a

workload group

. For more information, see

CREATE WORKLOAD GROUP

.

Description

CPU usage in milliseconds.

18

Yes

214

27

No

CPU limit violation.

21

Yes

Group ID where the violation occurred.

66

Yes

SPID of the process that caused the violation.

58

Yes

ID of the server process that fires this event.

Note: This can differ from the actual user SPID if a

system thread validates CPU usage as a

background task.

12

Yes

The time when this event fired.

14

Yes

sp_trace_setevent

Resource governor

Resource governor workload group

ALTER WORKLOAD GROUP

Last updated on 11/18/2025

ﾉ

Expand table

```cmd
REQUEST_MAX_CPU_TIME_SEC
CPU
EventClass
EventSubClass
GroupID
```
