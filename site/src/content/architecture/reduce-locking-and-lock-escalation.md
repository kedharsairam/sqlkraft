---
title: "Reduce locking and lock escalation"
topic: "locking"
description: ") locks on the clustered index pages containing those rows."
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Intent exclusive (

) locks on the clustered index pages containing those rows.

An

lock on the clustered index and another on the table.

The

statement acquires these locks:

Shared (

) locks on all data rows it reads, unless the row is already protected by an

lock

from the

statement.

Intent Shared (

) locks on all clustered index pages containing those rows, unless the page

is already protected by an

lock.

No lock on the clustered index or table because they're already protected by

locks.

If the

statement acquires enough locks to trigger lock escalation and the escalation

succeeds, the

lock on the table is converted to an

lock, and all the row, page, and index

locks are released. Both the updates and reads are protected by the

lock on the table.

In most cases, the Database Engine delivers the best performance when operating with its default

settings for locking and lock escalation.

Take advantage of

optimized locking

.

Optimized locking

offers an improved transaction locking mechanism that reduces lock

memory consumption and blocking for concurrent transactions. Lock escalation is far less

likely to ever occur when optimized locking is enabled.

Avoid using

table hints with optimized locking

. Table hints might reduce the effectiveness

of optimized locking.

Enable the

READ_COMMITTED_SNAPSHOT

option for the database for the most benefit

from optimized locking. This is the default in Azure SQL Database.

Optimized locking requires

accelerated database recovery (ADR)

to be enabled on the

database.

If an instance of the Database Engine generates a lot of locks and is seeing frequent lock

escalations, consider reducing the amount of locking with the following strategies:

Use an isolation level that doesn't generate shared locks for read operations:

isolation level when the

database option is

.

isolation level.

isolation level. This can only be used for systems that can operate with

dirty reads.

Use the

or

table hints to have the Database Engine use page, heap, or

index locks instead of low-level locks. Using this option, however, increases the problems of

users blocking other users attempting to access the same data and shouldn't be used in

systems with more than a few concurrent users.

If optimized locking isn't available, for partitioned tables, use the

option of

ALTER TABLE

to escalate locks to the partition instead of the table, or to disable lock

escalation for a table.

Break up large batch operations into several smaller operations. For example, suppose you

ran the following query to remove several hundred thousand old rows from an audit table,

and then you found that it caused a lock escalation that blocked other users:

By removing these rows a few hundred at a time, you can dramatically reduce the number

of locks that accumulate per transaction and prevent lock escalation. For example:

Reduce a query lock footprint by making the query as efficient as possible. Large scans or

large numbers of key lookups might increase the chance of lock escalation; additionally,

that increases the chance of deadlocks, and generally adversely affects concurrency and

performance. After you find the query that causes lock escalation, look for opportunities to

create new indexes or to add columns to an existing index to remove full index or table

scans and to maximize the efficiency of index seeks. Consider using the

Database Engine

Tuning Advisor

to perform an automatic index analysis on the query. For more information,

see

Tutorial: Database Engine Tuning Advisor

. One goal of this optimization is to make

index seeks return as few rows as possible to minimize the cost of key lookups (maximize

the selectivity of the index for the particular query). If the Database Engine estimates that a

key lookup logical operator might return many rows, it might use a prefetch optimization to

perform the lookup. If the Database Engine does use prefetch for a lookup, it must increase

the transaction isolation level of a portion of the query to

. This means that

what might look similar to a

statement at a

isolation level might

acquire many thousands of key locks (on both the clustered index and one nonclustered

index), which can cause such a query to exceed the lock escalation thresholds. This is

especially important if you find that the escalated lock is a shared table lock, which,

however, isn't commonly seen at the default

isolation level.

If a key lookup with the prefetch optimization is causing lock escalation, consider adding

additional columns to the nonclustered index that appears in the Index Seek or the Index

Scan logical operator below the key lookup logical operator in the query plan. It might be

possible to create a covering index (an index that includes all columns in a table that were

used in the query), or at least an index that covers the columns that were used for join

criteria or in the

clause if including everything in the

column list is impractical.

A Nested Loop join might also use the prefetch optimization, and this causes the same

locking behavior.

Lock escalation can't occur if a different SPID is currently holding an incompatible table lock.

Lock escalation always escalates to a table lock, and never to page locks. Additionally, if a

lock escalation attempt fails because another SPID holds an incompatible table lock, the

query that attempted escalation doesn't block while waiting for a table lock. Instead, it

continues to acquire locks at its original, more granular level (row, key, or page), periodically

making additional escalation attempts. Therefore, one method to prevent lock escalation on

a particular table is to acquire and hold a lock on a different connection that isn't

compatible with the escalated lock type. An intent exclusive (

) lock at the table level

doesn't lock any rows or pages, but it's still not compatible with an escalated shared (

) or

exclusive (

) table lock. For example, assume that you must run a batch job that modifies a

large number of rows in the

table and that has caused blocking that occurs

because of lock escalation. If this job always completes in less than an hour, you might

create a Transact-SQL job that contains the following code, and schedule the new job to

start several minutes before the batch job's start time:

### MSSQLSERVER_1204

`IX`

`IX`

`SELECT`

```sql
S
```

```sql
X
```

`UPDATE`

`IS`

`IX`

`IX`

`SELECT`

`IX`

```sql
X
```

```sql
X
```

```sql
READ COMMITTED
```

`READ_COMMITTED_SNAPSHOT`

`ON`

`SNAPSHOT`

```sql
READ UNCOMMITTED
```

`PAGLOCK`

`TABLOCK`

`LOCK_ESCALATION`

```sql
DELETE
FROM
LogMessages
WHERE
LogDate <
'2024-09-26'
DECLARE
@DeletedRows int
;
WHILE @DeletedRows IS NULL OR @DeletedRows > 0
BEGIN
DELETE
TOP (500)
FROM
LogMessages
WHERE
LogDate <
'2024-09-26'
SELECT
@DeletedRows = @@ROWCOUNT;
END
;
```

```sql
REPEATABLE READ
```

`SELECT`

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

`WHERE`

`SELECT`

`IX`

```sql
S
```

```sql
X
```

`mytable`

```sql
BEGIN
TRAN;
SELECT
*
FROM mytable
WITH (UPDLOCK, HOLDLOCK)
```
