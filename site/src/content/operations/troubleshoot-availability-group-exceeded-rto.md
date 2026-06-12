---
title: "Troubleshoot: Availability group exceeded RTO"
topic: "high-availability"
description: ""
tags: ["high-availability","troubleshoot-availability-group-exceeded-rto"]
pubDate: "2025-12-01"
---

After an automatic failover or a planned manual failover without data loss on an availability

group, you may find that the failover time exceeds your recovery time objective (RTO). Or,

when you estimate the failover time of a synchronous-commit secondary replica (such as an

automatic failover partner) using the method in

Monitor performance for Always On

Availability Groups

, you find that it exceeds your RTO.

If your automatic failover still has not completed, see

Troubleshooting automatic failover

problems in SQL Server 2012 Always On environments.

The following sections describe the common causes for a failover time that exceeds RTO.

1.

Reporting workload blocks the redo thread from running

2.

Redo thread falls behind due to resource contention

The redo thread on the secondary replica is blocked from making data definition language

(DDL) changes by a long-running read-only query.

On the secondary replica, the read-only queries acquire schema stability (

) locks. These

locks can block the redo thread from acquiring schema modification (

) locks to

make any DDL changes. A blocked redo thread cannot apply log records until it is unblocked.

Once unblocked, it can continue to catch up to the end of log and allow the subsequent undo

and failover process to proceed.

When the redo thread is blocked, an extended event called

is

generated. Additionally, you can query the DMV sys.dm_exec_request on the secondary replica

to find out which session is blocking the REDO thread, and then you can take corrective action.

```cmd
Sch-S
Sch-S
Sch-M sqlserver.lock_redo_blocked
```
