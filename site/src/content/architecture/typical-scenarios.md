---
title: "Typical scenarios"
topic: "io-fundamentals"
description: "Spinlock contention can occur for any number of reasons that might be unrelated to database"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Spinlock contention can occur for any number of reasons that might be unrelated to database

design decisions. Because spinlocks gate access to internal data structures, spinlock contention

isn't manifested in the same way as buffer latch contention, which is directly affected by

schema design choices and data access patterns.

The symptom primarily associated with spinlock contention is high CPU consumption as a

result of the large number of spins and many threads attempting to acquire the same spinlock.

In general, this has been observed on systems with 24 and more CPU cores, and most

commonly on systems with more than 32 CPU cores. As stated before, some level of

contention on spinlocks is normal for high concurrency OLTP systems with significant load and

there's often a large number of spins (billions/trillions) reported from the

DMV on systems that have been running for a long time. Again,

observing a high number of spins for any given spinlock type isn't enough information to

determine that there's negative impact to workload performance.

A combination of several of the following symptoms might indicate spinlock contention. If all

of these conditions are true, perform further investigation into possible spinlock contention

issues.

A high number of spins and backoffs are observed for a particular spinlock type.

The system is experiencing heavy CPU utilization or spikes in CPU consumption. In heavy

CPU scenarios, you see high signal waits on

(reported by the DMV

).

The system is experiencing high concurrency.

The CPU usage and spins are increased disproportionate to throughput.

One common phenomenon easily diagnosed is a significant divergence in throughput and CPU

usage. Many OLTP workloads have a relationship between (throughput / number of users on

the system) and CPU consumption. High spins observed in conjunction with a significant

divergence of CPU consumption and throughput can be an indication of spinlock contention

introducing CPU overhead. An important thing to note here is that it's also common to see this

type of divergence on systems when certain queries become more expensive over time. For

example, queries that are issued against datasets that perform more logical reads over time

can result in similar symptoms.

）

Important

```sql
sys.dm_os_spinlock_stats
```

```sql
SOS_SCHEDULER_YIELD
```

```sql
sys.dm_os_wait_stats
```
