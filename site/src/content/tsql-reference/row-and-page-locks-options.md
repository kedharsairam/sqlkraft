---
name: "Row and page locks options"
title: "Row and page locks options"
category: "operators"
description: "option is equivalent to"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

option is equivalent to

.

=

time

[

]

The wait time (an integer value specified in minutes) that the online index operation waits

using low priority locks. If the operation is blocked for the

time, the specified

action is executed.

time is always in minutes, and the word

can be omitted.

= [

|

|

]

: Continue waiting for the lock with normal priority.

: Exit the online index operation currently being executed, without taking any action.

The option

can't be used when

is 0.

: Kill all user transactions that block the online index operation so that the

operation can continue. The

option requires the principal executing the

or

statement to have the

permission.

You can use the following extended events to monitor index operations that wait for locks at

low priority:

When

and

, row-, page-, and table-level locks are

allowed when accessing the index. The Database Engine chooses the appropriate lock and can

escalate the lock from a row or page lock to a table lock.

When

and

, only a table-level lock is allowed

when accessing the index.

２

Warning

It is not recommended to disable row or page locks on an index. Concurrency-related

problems might occur, and certain functionality might be unavailable. For example, an

index can't be reorganized when

is set to

.

### Applies to

`WAIT_AT_LOW_PRIORITY`

```sql
WAIT_AT_LOW_PRIORITY (MAX_DURATION = 0 minutes, ABORT_AFTER_WAIT = NONE)
```

`MAX_DURATION`

`MINUTES`

`MAX_DURATION`

`ABORT_AFTER_WAIT`

`MAX_DURATION`

`MINUTES`

`ABORT_AFTER_WAIT`

`NONE`

`SELF`

`BLOCKERS`

`NONE`

`SELF`

`SELF`

`MAX_DURATION`

`BLOCKERS`

`BLOCKERS`

```sql
CREATE
INDEX
```

```sql
ALTER INDEX
```

```sql
ALTER ANY CONNECTION
```

```sql
lock_request_priority_state process_killed_by_abort_blockers ddl_with_wait_at_low_priority
```

```sql
ALLOW_ROW_LOCKS = ON
```

```sql
ALLOW_PAGE_LOCK = ON
```

```sql
ALLOW_ROW_LOCKS = OFF
```

```sql
ALLOW_PAGE_LOCK = OFF
```

`ALLOW_PAGE_LOCKS`

`OFF`
