---
name: "Use WITH STATUSONLY"
title: "Use WITH STATUSONLY"
category: "statements"
description: "Used to kill an unresolved distributed transaction with rollback. Only applicable to distributed"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Used to kill an unresolved distributed transaction with rollback. Only applicable to distributed

transactions, you must specify a

UOW

to use this option. For more information, see

distributed

transactions

.

is commonly used to end a process that is blocking other important processes with locks.

can also be used to stop a process that is executing a query that is using necessary

system resources. System processes and processes running an extended stored procedure can't

be ended.

Use

carefully, especially when critical processes are running. You can't kill your own

process. You also shouldn't kill the following processes:

Use

to display the session ID (SPID) value for the current session.

To obtain a report of active session ID values, query the

column of the

,

, and

dynamic management

views. You can also view the

column that the

system stored procedure returns. If a

rollback is in progress for a specific session ID, the

column in the

result set for that

session ID indicates

.

When a particular connection has a lock on a database resource and blocks the progress of

another connection, the session ID of the blocking connection shows up in the

column of

or the

column returned by

.

The

command can be used to resolve in-doubt distributed transactions. These

transactions are unresolved distributed transactions that occur because of unplanned restarts

of the database server or MS DTC coordinator. For more information about in-doubt

transactions, see the "Two-Phase Commit" section in

Use Marked Transactions to Recover

Related Databases Consistently

.

### sysadmin

### processadmin

### Microsoft Fabric Data Warehouse:

### Azure Synapse Analytics:

`KILL`

`KILL`

`KILL`

```sql
AWAITING COMMAND
CHECKPOINT SLEEP
LAZY WRITER
LOCK MONITOR
SIGNAL HANDLER
```

```sql
@@SPID
```

`session_id`

`sys.dm_tran_locks`

`sys.dm_exec_sessions`

`sys.dm_exec_requests`

`SPID`

`sp_who`

`cmd`

`sp_who`

```sql
KILLED/ROLLBACK
```

`blocking_session_id`

`sys.dm_exec_requests`

`blk`

`sp_who`

`KILL`
