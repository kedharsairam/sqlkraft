---
title: "Lock escalation without optimized locking"
topic: "locking"
description: "Lock escalation behaves differently depending on whether"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Lock escalation behaves differently depending on whether

optimized locking

is enabled.

As the Database Engine acquires low-level locks, it also places intent locks on the objects that

contain the lower-level objects:

When locking rows or index key ranges, the Database Engine places an intent lock on the

pages that contain the rows or keys.

When locking pages, the Database Engine places an intent lock on the higher level objects

that contain the pages. In addition to intent lock on the object, intent page locks are

requested on the following objects:

Leaf-level pages of nonclustered indexes

Data pages of clustered indexes

Heap data pages

The Database Engine might do both row and page locking for the same statement to minimize

the number of locks and reduce the likelihood that lock escalation is necessary. For example, the

Database Engine could place page locks on a nonclustered index (if enough contiguous keys in

the index node are selected to satisfy the query) and row locks on the clustered index or heap.

To escalate locks, the Database Engine attempts to change the intent lock on the table to the

corresponding full lock, for example, changing an intent exclusive (

) lock to an exclusive (

)

lock, or an intent shared (

) lock to a shared (

) lock. If the lock escalation attempt succeeds

and the full table lock is acquired, then all HoBT, page (

), or row-level (

,

) locks held

by the transaction on the heap or index are released. If the full lock can't be acquired, no lock

escalation happens at that time and the Database Engine continues to acquire row, key, or page

locks.

The Database Engine doesn't escalate row or key-range locks to page locks, but escalates them

directly to table locks. Similarly, page locks are always escalated to table locks. Locking of

partitioned tables can escalate to the HoBT level for the associated partition instead of to the

table lock. A HoBT-level lock doesn't necessarily lock the aligned HoBTs for the partition.

７

Note

HoBT-level locks usually increase concurrency, but introduce the potential for deadlocks

when transactions that are locking different partitions each want to expand their exclusive

If a lock escalation attempt fails because of conflicting locks held by concurrent transactions, the

Database Engine retries the lock escalation for each additional 1,250 locks acquired by the

transaction.

Each escalation event operates primarily at the level of a single Transact-SQL statement. When

the event starts, the Database Engine attempts to escalate all the locks owned by the current

transaction in any of the tables that have been referenced by the active statement provided it

meets the escalation threshold requirements. If the escalation event starts before the statement

has accessed a table, no attempt is made to escalate the locks on that table. If lock escalation

succeeds, any locks acquired by the transaction in a previous statement and still held at the time

the event starts are escalated if the table is referenced by the current statement and is included in

the escalation event.

For example, assume that a session performs these operations:

Begins a transaction.

Updates

. This generates exclusive row locks in

that are held until the

transaction completes.

Updates

. This generates exclusive row locks in

that are held until the

transaction completes.

Performs a

that joins

with

. The query execution plan calls for the

rows to be retrieved from

before the rows are retrieved from

.

The

statement triggers lock escalation while it's retrieving rows from

and

before it has accessed

.

If lock escalation succeeds, only the locks held by the session on

are escalated. This

includes both the shared locks from the

statement and the exclusive locks from the

previous

statement. While only the locks the session acquired in

for the

statement are counted to determine if lock escalation should be done, once escalation is

successful all locks held by the session in

are escalated to an exclusive lock on the table,

and all other lower-granularity locks, including intent locks, on

are released.

No attempt is made to escalate locks on

because there was no active reference to

in the

statement. Similarly no attempt is made to escalate the locks on

, which

aren't escalated because it hadn't yet been accessed when the escalation occurred.

locks to the other partitions. In rare instances,

locking granularity might perform

better.

```sql
IX
```

```sql
X
```

```sql
IS
```

```sql
S
```

```sql
PAGE
```

```sql
RID
```

```sql
KEY
```

```sql
TableA
```

```sql
TableA
```

```sql
TableB
```

```sql
TableB
```

```sql
SELECT
```

```sql
TableA
```

```sql
TableC
```

```sql
TableA
```

```sql
TableC
```

```sql
SELECT
```

```sql
TableA
```

```sql
TableC
```

```sql
TableA
```

```sql
SELECT
```

```sql
UPDATE
```

```sql
TableA
```

```sql
SELECT
```

```sql
TableA
```

```sql
TableA
```

```sql
TableB
```

```sql
TableB
```

```sql
SELECT
```

```sql
TableC
```

```sql
TABLE
```
