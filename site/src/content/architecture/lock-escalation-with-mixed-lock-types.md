---
title: "Lock escalation with mixed lock types"
topic: "locking"
description: "and at least 5,000 row locks in the clustered index for"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

index for

and at least 5,000 row locks in the clustered index for

, but hasn't yet

accessed

. When the Database Engine detects that the statement has acquired at least

5,000 row locks in

, it attempts to escalate all locks held by the current transaction on

. It also attempts to escalate all locks held by the current transaction on

, but since

the number of locks on

is less than 5,000, the escalation won't succeed. No lock

escalation is attempted for

because it hadn't yet been accessed when the escalation

occurred.

Whenever the number of locks is greater than the memory threshold for lock escalation, the

Database Engine triggers lock escalation. The memory threshold depends on the setting of the

locks

configuration option:

If the

option is set to its default setting of 0, then the lock escalation threshold is

reached when the memory used by lock objects is 24 percent of the memory used by the

Database Engine, excluding AWE memory. The data structure used to represent a lock is

approximately 100 bytes long. This threshold is dynamic because the Database Engine

dynamically acquires and frees memory to adjust for varying workloads.

If the

option is a value other than 0, then the lock escalation threshold is 40 percent

(or less if there's a memory pressure) of the value of the locks option.

The Database Engine can choose any active statement from any session for escalation, and for

every 1,250 new locks it will choose statements for escalation as long as the lock memory used in

the instance remains above the threshold.

When lock escalation occurs, the lock selected for the heap or index is strong enough to meet

the requirements of the most restrictive lower level lock.

For example, assume a session:

Begins a transaction.

Updates a table containing a clustered index.

Issues a

statement that references the same table.

The

statement acquires these locks:

Exclusive (

) locks on the updated data rows.

```sql
TableA
```

```sql
TableB
```

```sql
TableC
```

```sql
TableB
```

```sql
TableB
```

```sql
TableA
```

```sql
TableA
```

```sql
TableC
```

```sql
locks
```

```sql
locks
```

```sql
SELECT
```

```sql
UPDATE
```

```sql
X
```
