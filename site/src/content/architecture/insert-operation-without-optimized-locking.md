---
title: "Insert operation without optimized locking"
topic: "locking"
description: "database option and the"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

database option and the

isolation level also allow reads from

a row-version of the previously committed state.)

Range delete can be executed using three basic lock modes: row, page, or table lock. The row,

page, or table locking strategy is decided by Query Optimizer or can be specified by the user

through Query Optimizer hints such as

,

, or

. When

or

is used, the Database Engine immediately deallocates an index page if all rows are deleted from

this page. In contrast, when

is used, all deleted rows are marked only as deleted; they're

removed from the index page later using a background task.

When deleting a row within a transaction, the row and page locks are acquired and released

incrementally, and not held for the duration of the transaction. For example, given this DELETE

statement:

SQL

A TID lock is placed on all the modified rows for the duration of the transaction. A lock is

acquired on the TID of the index rows corresponding to the value

. With optimized locking,

page and row locks continue to be acquired for updates, but each page and row lock is released

as soon as each row is updated. The TID lock protects the rows from being updated until the

transaction is complete. Any transaction that attempts to read, insert, or delete rows with the

value

is blocked until the deleting transaction either commits or rolls back. (The

database option and the

isolation level also allow reads from

a row-version of the previously committed state.)

Otherwise, the locking mechanics of a delete operation are the same as without optimized

locking.

When inserting a row within a transaction, the range the row falls into doesn't have to be locked

for the duration of the transaction performing the insert operation. Locking the inserted key

value until the end of the transaction is sufficient to maintain serializability. For example, given

this INSERT statement:

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
ROWLOCK
```

```sql
PAGLOCK
```

```sql
TABLOCK
```

```sql
PAGLOCK
```

```sql
TABLOCK
```

```sql
ROWLOCK
```

```sql
Bob
```

```sql
Bob
```

```sql
READ_COMMITTED_SNAPSHOT
```

```sql
SNAPSHOT
```

```sql
DELETE
mytable
WHERE
name
=
'Bob'
;
```
