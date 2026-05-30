---
title: "Monitor lock escalation"
topic: "locking"
description: "This query acquires and holds an"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

This query acquires and holds an

lock on

for one hour, which prevents lock

escalation on the table during that time. This batch doesn't modify any data or block other

queries (unless the other query forces a table lock with the

hint or if an

administrator has disabled page or row locks on an index on

).

You can also use trace flags 1211 and 1224 to disable all or some lock escalations. However,

these

trace flags

disable all lock escalation globally for the entire Database Engine instance.

Lock escalation serves a useful purpose in the Database Engine by maximizing the efficiency

of queries that are otherwise slowed down by the overhead of acquiring and releasing

several thousands of locks. Lock escalation also helps minimize the required memory to

keep track of locks. The memory that the Database Engine can dynamically allocate for lock

structures is finite, so if you disable lock escalation and the lock memory grows large

enough, attempts to allocate additional locks for any query might fail and the following

error occurs:

Starting with SQL Server 2008 (10.0.x), the behavior of lock escalation has changed with the

introduction of the

table option. For more information, see the

option of

ALTER TABLE

.

７

Note

When the

error occurs, it stops the processing of the current

statement and causes a rollback of the active transaction. The rollback itself might

block users or lead to a long database recovery time if you restart the database service.

７

Note

Using a lock hint such as

only alters the initial lock acquisition. Lock hints don't

prevent lock escalation.

`IX`

`mytable`

`TABLOCK`

`mytable`

```sql
Error: 1204, Severity: 19, State: 1 The SQL Server cannot obtain a LOCK resource at this time. Rerun your statement when there are fewer active users or ask the system administrator to check the SQL Server lock and memory configuration.
```

`LOCK_ESCALATION`

`LOCK_ESCALATION`

```sql
WHERE
1 = 0;
WAITFOR DELAY '1:00:00';
COMMIT
TRAN;
```

`ROWLOCK`
