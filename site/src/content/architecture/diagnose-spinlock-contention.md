---
title: "Diagnose spinlock contention"
topic: "locking"
description: "As stated previously spinlocks are most common on high concurrency systems that are under"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

As stated previously spinlocks are most common on high concurrency systems that are under

heavy load.

Some of the scenarios that are prone to this issue include:

Name resolution problems caused by a failure to fully qualify names of objects. For more

information, see

## Description of SQL Server blocking caused by compile locks

. This specific

issue is described in more detail within this article.

Contention for lock hash buckets in the lock manager for workloads that frequently

access the same lock (such as a shared lock on a frequently read row). This type of

contention surfaces as a

type spinlock. In one particular case, we found that

this problem surfaced as a result of incorrectly modeled access patterns in a test

environment. In this environment, more than the expected numbers of threads were

constantly accessing the exact same row due to incorrectly configured test parameters.

High rate of DTC transactions when there's high degree of latency between the MSDTC

transaction coordinators. This specific problem is documented in detail in the SQLCAT

blog entry

Resolving DTC Related Waits and Tuning Scalability of DTC

.

This section provides information for diagnosing SQL Server spinlock contention. The primary

tools used to diagnose spinlock contention are:

Look for high CPU conditions or divergence between throughput and CPU

consumption.

ﾉ

Expand table

### Step 1

### Step 2

### Step 3

### Step 4

```sql
LOCK_HASH
```
