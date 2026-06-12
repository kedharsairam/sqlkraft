---
title: "Lock escalation"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

The

mode key-range lock is placed on the index row corresponding to the name

to test the range. If the lock is granted, a row with the value

is inserted and an exclusive (

)

lock is placed on the inserted row. The

mode key-range lock is necessary only to test

the range and isn't held for the duration of the transaction performing the insert operation. Other

transactions can insert or delete values before or after the inserted row with the value.

However, any transaction attempting to read, insert, or delete the row with the value

is

blocked until the inserting transaction either commits or rolls back.

When inserting a row within a transaction, the range the row falls into doesn't have to be locked

for the duration of the transaction performing the insert operation. Row and page locks are rarely

acquired, only when there's an online index rebuild in progress, or when there are concurrent

transactions. If row and page locks are acquired, they're released quickly and not

held for the duration of the transaction. Placing an exclusive TID lock on the inserted key value

until the end of the transaction is sufficient to maintain serializability. For example, given this

statement:

With optimized locking, a

lock is only acquired if there at least one transaction that's

using the

isolation level in the instance. The

mode key-range lock is

placed on the index row corresponding to the name

to test the range. If the lock is

granted, a row with the value

is inserted and an exclusive (

) lock is placed on the inserted

row. The

mode key-range lock is necessary only to test the range and isn't held for the

duration of the transaction performing the insert operation. Other transactions can insert or

delete values before or after the inserted row with the value. However, any transaction

attempting to read, insert, or delete the row with the value

is blocked until the inserting

transaction either commits or rolls back.

Lock escalation is the process of converting many fine-grained locks into fewer coarse-grain

locks, reducing system overhead while increasing the probability of concurrency contention.

```sql
RangeI-N
```

`David`

`Dan`

```sql
X
```

```sql
RangeI-N
```

`Dan`

`Dan`

`SERIALIZABLE`

`INSERT`

```sql
RangeI-N
```

`SERIALIZABLE`

```sql
RangeI-N
```

`David`

`Dan`

```sql
X
```

```sql
RangeI-N
```

`Dan`

`Dan`

```sql
INSERT mytable
VALUES (
'Dan'
);
```

```sql
INSERT mytable
VALUES (
'Dan'
);
```
