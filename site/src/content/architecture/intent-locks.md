---
title: "Intent locks"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: "2026-05-29"
---

Data modification statements, such as

,

, and

combine both read and

modification operations. The statement first performs read operations to acquire data before

performing the required modification operations. Data modification statements, therefore,

typically request both shared locks and exclusive locks. For example, an

statement might

modify rows in one table based on a join with another table. In this case, the

statement

requests shared locks on the rows read in the join table in addition to requesting exclusive locks

on the updated rows.

The Database Engine uses intent locks to protect placing a shared (

) lock or exclusive (

) lock

on a resource lower in the lock hierarchy. Intent locks are named "intent locks" because they're

acquired before a lock at the lower level and, therefore, signal intent to place locks at a lower

level.

Intent locks serve two purposes:

To prevent other transactions from modifying the higher-level resource in a way that would

invalidate the lock at the lower level.

To improve the efficiency of the Database Engine in detecting lock conflicts at the higher

level of granularity.

For example, a shared intent lock is requested at the table level before shared (

) locks are

requested on pages or rows within that table. Setting an intent lock at the table level prevents

another transaction from subsequently acquiring an exclusive (

) lock on the table containing

that page. Intent locks improve performance because the Database Engine examines intent locks

only at the table level to determine if a transaction can safely acquire a lock on that table. This

removes the requirement to examine every row or page lock on the table to determine if a

transaction can lock the entire table.

Intent locks include intent shared (

), intent exclusive (

), and shared with intent exclusive

(

).

## Description

hierarchy.

hierarchy.

ﾉ

`INSERT`

`UPDATE`

`DELETE`

`UPDATE`

`UPDATE`

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

`IS`

`IX`

`SIX`

`IS`

`IX`

`IS`
