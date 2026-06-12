---
title: "Locks Event Category"
topic: "event-classes"
description: ""
tags: ["event-classes","locks-event-category"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Use the event classes in the

event category to monitor locking activity in an instance of

the Microsoft SQL Server Database Engine. These event classes can help you investigate

locking problems caused by multiple users reading and modifying data concurrently.

Because the Database Engine often processes many locks, capturing the

event classes

during a trace can incur significant overhead and result in large trace files or tables.

Description

Deadlock Graph Event

Class

Provides an XML description of a deadlock.

Lock:Acquired Event

Class

Indicates that a lock has been acquired on a resource, such as a row in a table.

Lock:Cancel Event

Class

Tracks requests for locks that were canceled before the lock was acquired (for

example, to prevent a deadlock).

Lock:Deadlock Chain

Event Class

Monitors when deadlock conditions occur and which objects are involved.

Lock:Deadlock Event

Class

Tracks when a transaction has requested a lock on a resource already locked by

another transaction, resulting in a deadlock.

Lock:Escalation Event

Class

Indicates that a finer-grained lock has been converted to a coarser-grained lock.

Lock:Released Event

Class

Tracks when a lock is released.

Lock:Timeout (timeout

> 0. Event Class

Tracks when lock requests cannot be completed because another transaction

has a blocking lock on the requested resource. This event occurs only in

situations where the lock time-out value is greater than zero.

Lock:Timeout Event

Class

Tracks when lock requests cannot be completed because another transaction

has a blocking lock on the requested resource.

ﾉ

Expand table
