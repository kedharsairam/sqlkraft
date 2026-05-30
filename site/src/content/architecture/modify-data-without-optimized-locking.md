---
title: "Modify data without optimized locking"
topic: "locking"
description: "Not in the list of the transactions active when the snapshot transaction started."
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Not in the list of the transactions active when the snapshot transaction started.

Read operations performed by a

transaction retrieve the last version of each row that

had been committed at the time the

transaction started. This provides a transactionally

consistent snapshot of the data as it existed at the start of the transaction.

transactions using row versioning operate in much the same way. The difference

is that the

transaction doesn't use its own transaction sequence number when

choosing row versions. Each time a statement is started, the

transaction reads the

latest transaction sequence number issued for that instance of the Database Engine. This is the

transaction sequence number used to select the row versions for that statement. This allows

transactions to see a snapshot of the data as it exists at the start of each statement.

The behavior of data writes is different with and without optimized locking enabled.

In a

transaction using row versioning, the selection of rows to update is done

using a blocking scan where an update (

) lock is acquired on the data row as data values are

read. This is the same as a

transaction that doesn't use row versioning. If the data

row doesn't meet the update criteria, the update lock is released on that row and the next row is

locked and scanned.

Transactions running under

isolation take an optimistic approach to data modification

by acquiring locks on data before performing the modification only to enforce constraints.

Otherwise, locks aren't acquired on data until the data is to be modified. When a data row meets

the update criteria, the

transaction verifies that the data row hasn't been modified by a

concurrent transaction that committed after the

transaction began. If the data row has

been modified outside of the

transaction, an update conflict occurs and the

transaction is terminated. The update conflict is handled by the Database Engine and there's no

way to disable the update conflict detection.

７

Note

Even though

transactions using row versioning provides a transactionally

consistent view of the data at a statement level, row versions generated or accessed by this

type of transaction are maintained until the transaction completes.

`SNAPSHOT`

`SNAPSHOT`

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

```sql
READ COMMITTED
```

```sql
READ
COMMITTED
```

```sql
READ COMMITTED
```

```sql
U
```

```sql
READ COMMITTED
```

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

`SNAPSHOT`

```sql
READ COMMITTED
```
