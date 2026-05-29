---
title: 'Update locks'
topic: 'locking'
description: 'Additional locking resources are available for'
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Additional locking resources are available for

lock resources. For more information, see

Diagnostic additions for optimized locking

.

The Database Engine locks resources using different lock modes that determine how the

resources can be accessed by concurrent transactions.

The following table shows the resource lock modes that the Database Engine uses.


## Description
Used for read operations that don't change or update data, such as a

statement.

Used on resources that can be updated. Prevents a common form of deadlock that occurs

when multiple sessions are reading, locking, and potentially updating resources later.

Used for data-modification operations, such as

,

, or

. Ensures that

multiple updates can't be made to the same resource at the same time.

Used to establish a lock hierarchy. The types of intent locks are: intent shared (

), intent

exclusive (

), and shared with intent exclusive (

).

Used when an operation dependent on the schema of a table is executing. The types of

schema locks are: schema modification (

) and schema stability (

).

Used when bulk copying data into a table with the

hint.

Protects the range of rows read by a query when using the

transaction isolation

level. Ensures that other transactions can't insert rows that would qualify for the queries of the

transaction if the queries were run again.

Shared (

) locks allow concurrent transactions to read a resource under pessimistic concurrency

control. No other transactions can modify the data while shared (

) locks exist on the resource.

Shared (

) locks on a resource are released as soon as the read operation completes, unless the

transaction isolation level is set to

or higher, or a locking hint is used to retain

the shared (

) locks for the duration of the transaction.

2

ﾉ

Expand table

```sql
XACT
```

```sql
S
```

```sql
SELECT
```

```sql
U
```

```sql
X
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
IS
```

```sql
IX
```

```sql
SIX
```

```sql
Sch-M
```

```sql
Sch-S
```

```sql
BU
```

```sql
TABLOCK
```

```sql
SERIALIZABLE
```

```sql
SERIALIZABLE
```

```sql
S
```

```sql
S
```

```sql
S
```

```sql
REPEATABLE READ
```

```sql
S
```
