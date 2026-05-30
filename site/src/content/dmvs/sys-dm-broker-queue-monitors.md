---
name: "sys.dm_broker_queue_monitors"
title: "sys.dm_broker_queue_monitors"
category: "service-broker"
description: "Returns a row for each queue monitor in the instance. A queue monitor manages activation for Object identifier for the database that contains the queue that the monitor watches. Object identifier for the queue that the monitor State of the monitor. This value is one of the Last time that this queue monitor activated a stored Number of sessions that are currently waiting within This value includes "
tags: ["service-broker", "dmv"]
pubDate: 2026-05-29
syntax: |
  INACTIVE
  NOTIFIED
  RECEIVES_OCCURRING
  last_empty_rowset_time
---

## Description

Returns a row for each queue monitor in the instance. A queue monitor manages activation for Object identifier for the database that contains the queue that the monitor watches. Object identifier for the queue that the monitor State of the monitor. This value is one of the Last time that this queue monitor activated a stored Number of sessions that are currently waiting within This value includes any session executing a

## Syntax

```sql
INACTIVE
NOTIFIED
RECEIVES_OCCURRING
last_empty_rowset_time
```

## Permissions

SQL Server Returns a row for each queue monitor in the instance. A queue monitor manages activation for a queue. Yes Object identifier for the database that contains the queue that the monitor watches. Yes Object identifier for the queue that the monitor watches. Yes State of the monitor. This value is one of the following options: Yes Last time that a from the queue returned an empty result. Yes Last time that this queue monitor activated a stored procedure. Yes Number of sessions that are currently waiting within a statement for this queue. This value includes any session executing a receive statement, regardless of whether the queue monitor started the session. It's for when you use together with . In other words, these tasks are waiting for messages to arrive on the queue. SQL Server 2019 (15.x) and earlier versions require permission on the server. ﾉ
