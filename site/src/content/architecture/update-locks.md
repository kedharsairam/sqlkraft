---
title: "Update locks"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

Additional locking resources are available for

lock resources. For more information, see

Diagnostic additions for optimized locking.

The Database Engine locks resources using different lock modes that determine how the

resources can be accessed by concurrent transactions.

The following table shows the resource lock modes that the Database Engine uses.

## Description

Used for read operations that don't change or update data, such as a

statement.

Used on resources that can be updated. Prevents a common form of deadlock that occurs

when multiple sessions are reading, locking, and potentially updating resources later.

,

, or.

multiple updates can't be made to the same resource at the same time.

Used to establish a lock hierarchy. The types of intent locks are: intent shared (

), intent

exclusive (

), and shared with intent exclusive (

).

Used when an operation dependent on the schema of a table is executing.

schema locks are: schema modification (

) and schema stability (

).

hint.

transaction isolation

level.

transaction if the queries were run again.

Shared (

) locks allow concurrent transactions to read a resource under pessimistic concurrency

control. No other transactions can modify the data while shared (

) locks exist on the resource.

Shared (

or higher, or a locking hint is used to retain

the shared (

) locks for the duration of the transaction.

2

ﾉ

`XACT`

```sql
S
```

`SELECT`

```sql
U
```

```sql
X
```

`INSERT`

`UPDATE`

`DELETE`

`IS`

`IX`

`SIX`

```sql
Sch-M
```

```sql
Sch-S
```

`BU`

`TABLOCK`

`SERIALIZABLE`

`SERIALIZABLE`

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
