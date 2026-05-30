---
title: "Trace flag 1204 example"
topic: "query-processing"
description: "Identifies the database lock."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Identifies the database lock.

is

represented in one of the following

ways:

, which

identifies the database lock taken by

database backup.

, which

identifies the lock taken by the log

backup.

Identifies an application lock.

is represented as

.

For example,

.

Represents metadata

resources involved in a deadlock.

Because

has many

subresources, the value returned

depends upon the subresource that

has deadlocked. For example,

## returns

. For

more information about

resources and subresources, see

sys.dm_tran_locks

.

Represents a heap or B-tree

involved in a deadlock.

The following example shows the output when trace flag 1204 is turned on. In this case, the

table in Node 1 is a heap with no indexes, and the table in Node 2 is a heap with a

nonclustered index. The index key in Node 2 is being updated when the deadlock occurs.

Output

`DB`

`DB`

```sql
DB: db_id
DB: db_id[BULK-OP-DB]
```

```sql
DB: db_id[BULK-OP-LOG]
```

`APP`

`APP`

```sql
APP: lock_resource
```

```sql
APP: Formf370f478
```

`METADATA`

`METADATA`

`METADATA.USER_TYPE`

```sql
user_type_id = *integer_value*
```

`METADATA`

`HOBT`

```sql
Deadlock encountered .... Printing deadlock information
Wait-for graph
```
