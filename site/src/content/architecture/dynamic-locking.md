---
title: "Dynamic locking"
topic: "locking"
description: "Monitor lock escalation by using the"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Monitor lock escalation by using the

extended event, such as in the following

example:

SQL

Using low-level locks, such as row locks, increases concurrency by decreasing the probability that

two transactions request locks on the same piece of data at the same time. Using low-level locks

also increases the number of locks and the resources needed to manage them. Using high-level

table or page locks lowers overhead, but at the expense of lowering concurrency.

The Database Engine uses a dynamic locking strategy to determine the most effective locks. The

Database Engine automatically determines what locks are most appropriate when the query is



### Spinlock

### Memory

```sql
lock_escalation
```

```sql
-- Session creates a histogram of the number of lock escalations per database
CREATE
EVENT
SESSION
[Track_lock_escalation]
ON
SERVER
ADD
EVENT
sqlserver.lock_escalation
(
SET
collect_database_name=1,collect_statement=1
ACTION
(sqlserver.database_id,sqlserver.database_name,sqlserver.query_hash_signed,sqlse
rver.query_plan_hash_signed,sqlserver.sql_text,sqlserver.username)
)
ADD
TARGET package0.histogram
(
SET
source
=N
'sqlserver.database_id'
)
GO
```
