---
title: 'Lock compatibility'
topic: 'locking'
description: ') locks allow multiple threads to bulk load data concurrently into the same table'
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Bulk update (

) locks allow multiple threads to bulk load data concurrently into the same table

while preventing other processes that aren't bulk loading data from accessing the table. The

Database Engine uses bulk update (

) locks when both of the following conditions are true.

You use the Transact-SQL

statement, or the

function, or you

use one of the Bulk Insert API commands such as .NET

, OLEDB Fast Load APIs,

or the ODBC Bulk Copy APIs to bulk copy data into a table.

The

hint is specified or the

table option is set using

sp_tableoption

.

Key-range locks protect a range of rows implicitly included in a record set being read by a

Transact-SQL statement while using the

transaction isolation level. Key-range

locking prevents phantom reads. By protecting the ranges of keys between rows, it also prevents

phantom insertions or deletions into a record set accessed by a transaction.

Lock compatibility controls whether multiple transactions can acquire locks on the same resource

at the same time. If a resource is already locked by another transaction, a new lock request can

be granted only if the mode of the requested lock is compatible with the mode of the existing

lock. If the mode of the requested lock isn't compatible with the existing lock, the transaction

requesting the new lock waits for the existing lock to be released or for the lock timeout interval

to expire. For example, no lock modes are compatible with exclusive locks. While an exclusive (

)

lock is held, no other transaction can acquire a lock of any kind (shared, update, or exclusive) on

that resource until the exclusive (

) lock is released. Conversely, if a shared (

) lock has been

applied to a resource, other transactions can also acquire a shared lock or an update (

) lock on

that resource even if the first transaction hasn't completed. However, other transactions can't

acquire an exclusive lock until the shared lock has been released.

The following table shows the compatibility of the most commonly encountered lock modes.



Tip

Unlike the BULK INSERT statement, which holds a less restrictive Bulk Update (

) lock,

with the

hint holds an intent exclusive (

) lock on the table.

This means that you can't insert rows using parallel insert operations.

Yes

Yes

Yes

Yes

Yes

No

Yes

Yes

Yes

No

No

No

Yes

Yes

No

No

No

No

Yes

No

No

Yes

No

No

Yes

No

No

No

No

No

No

No

No

No

No

No

Use the following table to determine the compatibility of all the lock modes available in the

Database Engine.

ﾉ

Expand table

７

Note

An intent exclusive (

) lock is compatible with an

lock mode because

means the

intention is to update only some of the rows rather than all of them. Other transactions that

attempt to read or update some of the rows are also permitted as long as they aren't the

same rows being updated by other transactions. Further, if two transactions attempt to

update the same row, both transactions are granted an

lock at table and page level.

However, one transaction is granted an

lock at row level. The other transaction must wait

until the row-level lock is removed.




## Description
No conflict

Illegal

Conflict

No lock

Schema stability lock

Schema modification lock

Shared

Update

Exclusive

Intent shared

Intent update

Intent exclusive

Share with intent update

Share with intent exclusive

Update with intent exclusive

Bulk update

Shared range-shared

Shared range-update

Insert range-null

Insert range-shared

Insert range-update

Insert range-exclusive

Exclusive range-shared

Exclusive range-update

Exclusive range-exclusive

ﾉ

Expand table

### 'AAA'

### 'CZZ'

### 'ADG'

### 'BBD'

### 'CAL'

```sql
BU
```

```sql
BU
```

```sql
BULK INSERT
```

```sql
OPENROWSET(BULK)
```

```sql
SqlBulkCopy
```

```sql
TABLOCK
```

```sql
table lock on bulk load
```

```sql
SERIALIZABLE
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
U
```

```sql
BU
```

```sql
INSERT INTO...SELECT
```

```sql
TABLOCK
```

```sql
IX
```

```sql
IS
S
U
IX
SIX
X
```

```sql
IS
```

```sql
S
```

```sql
U
```

```sql
IX
```

```sql
SIX
```

```sql
X
```

```sql
IX
```

```sql
IX
```

```sql
IX
```

```sql
IX
```

```sql
X
```

```sql
N
```

```sql
I
```

```sql
C
```

```sql
NL
```

```sql
SCH-S
```

```sql
SCH-M
```

```sql
S
```

```sql
U
```

```sql
X
```

```sql
IS
```

```sql
IU
```

```sql
IX
```

```sql
SIU
```

```sql
SIX
```

```sql
UIX
```

```sql
BU
```

```sql
RS-S
```

```sql
RS-U
```

```sql
RI-N
```

```sql
RI-S
```

```sql
RI-U
```

```sql
RI-X
```

```sql
RX-S
```

```sql
RX-U
```

```sql
RX-X
```
