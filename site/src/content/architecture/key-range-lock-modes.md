---
title: "Key-range lock modes"
topic: "locking"
description: "Key-range locks protect a range of rows implicitly included in a record set being read by a"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

Key-range locks protect a range of rows implicitly included in a record set being read by a

Transact-SQL statement while using the

transaction isolation level. The

isolation level requires that any query executed during a transaction must obtain

the same set of rows every time it's executed during the transaction. A key range lock satisfies

this requirement by preventing other transactions from inserting new rows whose keys would fall

in the range of keys read by the

transaction.

Key-range locking prevents phantom reads. By protecting the ranges of keys between rows, it

also prevents phantom insertions into a set of records accessed by a transaction.

A key-range lock is placed on an index, specifying a beginning and ending key value. This lock

blocks any attempt to insert, update, or delete any row with a key value that falls in the range

because those operations would first have to acquire a lock on the index. For example, a

transaction could issue a

statement that reads all rows whose key values

match the condition

. A key-range lock on the key values in the range

from

to

prevents other transactions from inserting rows with key values anywhere in

that range, such as

,

, or

.

Key-range locks include both a range and a row component specified in range-row format:

Range represents the lock mode protecting the range between two consecutive index

entries.

Row represents the lock mode protecting the index entry.

Mode represents the combined lock mode used. Key-range lock modes consist of two parts.

The first represents the type of lock used to lock the index range (Range

T

) and the second

represents the lock type used to lock a specific key (

K

). The two parts are connected with a

hyphen (-), such as Range

T

-

K

.

## Description

Shared range, shared resource lock;

range scan.

Shared range, update resource lock;

update scan.

ﾉ

Expand table

`SERIALIZABLE`

`SERIALIZABLE`

`SERIALIZABLE`

`SERIALIZABLE`

`SELECT`

```sql
BETWEEN 'AAA' AND 'CZZ'
```

```sql
RangeS
S
RangeS-
S
```

`SERIALIZABLE`

```sql
RangeS
U
RangeS-
U
```

`SERIALIZABLE`
