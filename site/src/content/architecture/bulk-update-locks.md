---
title: "Bulk update locks"
topic: "locking"
description: "Protects requested or acquired shared locks on all resources lower in the hierarchy and intent"
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

## Description

resources.

Protects requested or acquired shared locks on all resources lower in the hierarchy and intent

exclusive locks on some (but not all) of the lower level resources. Concurrent

top-level resource are allowed. For example, acquiring a

lock on a table also acquires

intent exclusive locks on the pages being modified and exclusive locks on the modified rows.

lock per resource at one time, preventing updates to the resource

hierarchy by obtaining

locks at the table level.

Protects requested or acquired update locks on all resources lower in the hierarchy.

locks

are used only on page resources.

locks if an update operation

takes place.

and

simultaneously holding both locks.

hint and then executes an update operation.

hint

lock.

and

simultaneously holding both locks.

The Database Engine uses schema modification (

) locks during a table data definition

language (DDL) operation, such as adding a column or dropping a table. During the time that it's

lock prevents concurrent access to the table.

outside operations until the lock is released.

prevent access to affected tables by concurrent operations.

The Database Engine uses schema stability (

) locks when compiling and executing queries.

locks don't block any transactional locks, including exclusive (

) locks.

compiled. However, concurrent DDL operations, and concurrent DML operations that acquire

locks.

`IX`

`SIX`

`IS`

`SIX`

`SIX`

`IS`

`IU`

`IU`

`IU`

`IX`

`SIU`

```sql
S
```

`IU`

`PAGLOCK`

`PAGLOCK`

```sql
S
```

`IU`

`UIX`

```sql
U
```

`IX`

```sql
Sch-M
```

```sql
Sch-M
```

```sql
Sch-M
```

```sql
Sch-M
```

```sql
Sch-S
```

```sql
Sch-S
```

```sql
X
```

```sql
X
```

```sql
Sch-M
```

```sql
Sch-S
```
