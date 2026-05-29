---
title: "Customize locking for an index"
topic: "index-architecture"
description: "As shown in the following example, if the transaction isolation level is set to"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

As shown in the following example, if the transaction isolation level is set to

, and

the table-level locking hint

is used with the

statement, key-range locks typically

used to maintain

transactions aren't acquired.

SQL

The only lock acquired that references

is a schema stability (

) lock.

In this case, serializability is no longer guaranteed.

The

option of

avoids table locks during lock escalation, and

enables HoBT (partition) locks on partitioned tables. This option isn't a locking hint, and can be

used to reduce

lock escalation

. For more information, see

ALTER TABLE (Transact-SQL)

.

The Database Engine uses a dynamic locking strategy that automatically chooses the best locking

granularity for queries in most cases. We recommend that you don't override the default locking

levels, unless table or index access patterns are well understood and consistent, and there's a

resource contention problem to solve. Overriding a locking level can significantly impede

concurrent access to a table or index. For example, specifying only table-level locks on a large

table that users access heavily can cause bottlenecks because users must wait for the table-level

lock to be released before accessing the table.

```sql
SERIALIZABLE
```

```sql
NOLOCK
```

```sql
SELECT
```

```sql
SERIALIZABLE
```

```sql
HumanResources.Employee
```

```sql
Sch-S
```

```sql
LOCK_ESCALATION
```

```sql
ALTER TABLE
```

```sql
USE
AdventureWorks2022;
GO
SET
TRANSACTION
ISOLATION
LEVEL
SERIALIZABLE
;
GO
BEGIN
TRANSACTION
;
GO
SELECT
JobTitle
FROM
HumanResources.Employee
WITH
(NOLOCK);
GO
-- Get information about the locks held by
-- the transaction.
SELECT
resource_type,
resource_subtype,
request_mode
FROM
sys.dm_tran_locks
WHERE
request_session_id = @@SPID;
-- End the transaction.
ROLLBACK
;
GO
```
