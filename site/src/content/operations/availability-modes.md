---
title: "Availability modes"
topic: "high-availability"
description: |
  06/26/2025
  
  Applies to:
  
  SQL Server
  
  In Always On availability groups, the
  
  availability mode
  
  is a replica property that determines
  
  whether a given availability replica can run in synchronous-commit
tags:
  - "high-availability"
  - "availability-modes"
pubDate: 2025-12-01
---

06/26/2025

Applies to:

SQL Server

In Always On availability groups, the

availability mode

is a replica property that determines

whether a given availability replica can run in synchronous-commit mode. For each availability

replica, the availability mode must be configured for either synchronous-commit mode,

asynchronous-commit, or configuration only mode.

If the primary replica is configured for

asynchronous-commit mode

, it doesn't wait for any

secondary replica to write incoming transaction log records to disk (to

harden the log

).

If a given secondary replica is configured for asynchronous-commit mode, the primary replica

doesn't wait for that secondary replica to harden the log. If both the primary replica and a

given secondary replica are both configured for

synchronous-commit mode

, the primary replica

waits for the secondary replica to confirm that it has hardened the log (unless the secondary

replica fails to ping the primary replica within the primary's

session-timeout period

).

Always On availability groups supports three availability modes:

Asynchronous-commit mode

Synchronous-commit mode

Configuration only mode

Asynchronous-commit mode

is a disaster-recovery solution that works well when the availability

replicas are distributed over considerable distances. If every secondary replica is running under

asynchronous-commit mode, the primary replica doesn't wait for any of the secondary replicas

to harden the log. Rather, immediately after writing the log record to the local log file, the

７

Note

If a synchronous-commit secondary replica exceeds the primary replica's session-timeout

period (default is

), the primary replica temporarily marks the synchronization

state of every database on this secondary replica as

and the replica

state as

. When the secondary replica reconnects with the primary replica,

they resume synchronous-commit mode.

```cmd
NOT SYNCHRONIZING
NOT_HEALTHY
```