---
title: "Advanced transaction information"
topic: "io-fundamentals"
description: "There are a few cases where disallowing page or row locking can be beneficial, if the access"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

There are a few cases where disallowing page or row locking can be beneficial, if the access

patterns are well understood and consistent. For example, a database application uses a lookup

table that is updated weekly in a batch process. Concurrent readers access the table with a

shared (

) lock and the weekly batch update accesses the table with an exclusive (

) lock.

Turning off page and row locking on the table reduces the locking overhead throughout the

week by allowing readers to concurrently access the table through shared table locks. When the

batch job runs, it can complete the update efficiently because it obtains an exclusive table lock.

Turning off page and row locking might or might not be acceptable because the weekly batch

update blocks the concurrent readers from accessing the table while the update runs. If the batch

job only changes a few rows or pages, you can change the locking level to allow row or page

level locking, which will enable other sessions to read from the table without blocking. If the

batch job has a large number of updates, obtaining an exclusive lock on the table might be the

best way to ensure the batch job runs efficiently.

In some workloads, a type of deadlock might occur when two concurrent operations acquire row

locks on the same table and then block each other because they both need to lock the page.

Disallowing row locks forces one of the operations to wait, avoiding the deadlock. For more

about deadlocks, see the

Deadlocks guide

.

The granularity of locking used on an index can be set using the

and

statements. In addition, the

and

statements can be used to set locking

granularity on

and

constraints. For backward compatibility, the

system stored procedure can also set the granularity. To display the current

locking option for a given index, use the

function. Page-level locks, row-level

locks, or both page-level and row-level locks can be disallowed for a given index.

Page level

Row-level and table-level locks

Row level

Page-level and table-level locks

Page level and row level

Table-level locks

The following sections detail complex transaction scenarios.

ﾉ

Expand table

```sql
S
```

```sql
X
```

```sql
CREATE INDEX
```

```sql
ALTER INDEX
```

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
PRIMARY KEY
```

`UNIQUE`

`sp_indexoption`

`INDEXPROPERTY`
