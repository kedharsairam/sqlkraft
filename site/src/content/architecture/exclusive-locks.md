---
title: "Exclusive locks"
topic: "locking"
description: "The Database Engine places update ("
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

The Database Engine places update (

) locks as it prepares to execute an update.

locks are

compatible with

locks, but only one transaction can hold a

lock at a time on a given

resource. This is key - many concurrent transactions can hold

locks, but only one transaction

can hold a

lock on a resource. Update (

) locks are eventually upgraded to exclusive (

) locks

to update a row.

Update (

) locks can also be taken by statements other than

, when the

UPDLOCK table

hint

is specified in the statement.

Some applications use the "select a row, then update the row" pattern, where the read and

write are explicitly separated within the transaction. In this case, if the isolation level is

or

, concurrent updates might cause a deadlock, as follows:

A transaction reads data, acquiring a shared (

) lock on the resource, and then modifies the

data, which requires lock conversion to an exclusive (

) lock. If two transactions acquire

shared (

) locks on a resource and then attempt to update data concurrently, one

transaction attempts the lock conversion to an exclusive (

) lock. The shared-to-exclusive

lock conversion must wait because the exclusive (

) lock for one transaction isn't

compatible with the shared (

) lock of the other transaction; a lock wait occurs. The second

transaction attempts to acquire an exclusive (

) lock for its update. Because both

transactions are converting to exclusive (

) locks, and they're each waiting for the other

transaction to release its shared (

) lock, a deadlock occurs.

In the default

isolation level,

locks are short duration, released as soon as

they're used. While the deadlock described above is still possible, it's much less likely with

short duration locks.

To avoid this type of deadlock, applications can follow a "select a row with

hint,

then update the row" pattern.

If the

hint is used in a write when

isolation is in use, the transaction must

have access to the latest version of the row. If the latest version is no longer visible, it's

possible to receive

. For an example, see

Work with snapshot isolation

.

Exclusive (

) locks prevent access to a resource by concurrent transactions. With an exclusive (

)

lock, no other transactions can modify the data protected by the lock; read operations can take

place only with the use of the

hint or the

isolation level.

```sql
U
```

```sql
U
```

```sql
S
```

```sql
U
```

```sql
S
```

```sql
U
```

```sql
U
```

```sql
X
```

```sql
U
```

```sql
UPDATE
```

```sql
REPEATABLE READ
```

```sql
SERIALIZABLE
```

```sql
S
```

```sql
X
```

```sql
S
```

```sql
X
```

```sql
X
```

```sql
S
```

```sql
X
```

```sql
X
```

```sql
S
```

```sql
READ COMMITTED
```

```sql
S
```

```sql
UPDLOCK
```

```sql
UPDLOCK
```

```sql
SNAPSHOT
```

```sql
Msg 3960, Level 16, State 2 Snapshot isolation transaction aborted
due to update conflict
```

```sql
X
```

```sql
X
```

```sql
NOLOCK
```

```sql
READ UNCOMMITTED
```
