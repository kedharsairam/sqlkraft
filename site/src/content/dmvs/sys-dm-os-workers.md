---
name: 'sys.dm_os_workers'
title: 'sys.dm_os_workers'
category: 'execution'
description: 'Memory address of the scheduler. For more'
pubDate: 2026-05-29
---

sys.dm_os_workers

.

scheduler_address

Memory address of the scheduler. For more

information, see

sys.dm_os_schedulers (Transact-

SQL)

.

processor_group

Stores the processor group ID that is assigned to

this thread.

pdw_node_id

: Azure Synapse Analytics, Analytics

Platform System (PDW)

The identifier for the node that this distribution is

on.

If the worker state is RUNNING and the worker is running nonpreemptively, the worker address

matches the active_worker_address in sys.dm_os_schedulers.

When a worker that is waiting on an event is signaled, the worker is placed at the head of the

runnable queue. SQL Server allows for this to happen one thousand times in a row, after which

the worker is placed at the end of the queue. Moving a worker to the end of the queue has

some performance implications.

On SQL Server, requires

permission.

On SQL Database Premium Tiers, requires the

permission in the database.

On SQL Database Standard and Basic Tiers, requires the

role membership, or an

account.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

You can use the following query to find out how long a worker has been running in a

SUSPENDED or RUNNABLE state.

SQL

Here's the result set.

In the output, when

and

are equal, this represents the time that the

worker is in the SUSPENDED state. Otherwise,

represents the time that is spent by

the worker in the RUNNABLE state. In the output, session

is

for

milliseconds.

SQL Server Operating System Related Dynamic Management Views (Transact-SQL)

Query Processing Architecture Guide

Thread and Task Architecture Guide

Last updated on 11/18/2025

Article

•

02/28/2023

SQL Server

This section contains the following dynamic management objects.

sys.dm_tran_active_snapshot_database_transactions (Transact-SQL)

sys.dm_tran_current_snapshot (Transact-SQL)

sys.dm_tran_database_transactions (Transact-SQL)

sys.dm_tran_session_transactions (Transact-SQL)

sys.dm_tran_transactions_snapshot (Transact-SQL)

sys.dm_tran_version_store_space_usage

sys.dm_tran_active_transactions (Transact-SQL)

sys.dm_tran_current_transaction (Transact-SQL)

sys.dm_tran_distributed_transaction_stats (Transact-SQL)

sys.dm_tran_locks (Transact-SQL)

sys.dm_tran_top_version_generators (Transact-SQL)

sys.dm_tran_version_store (Transact-SQL)

## sys.dm_pdw_nodes_tran_active_snapshot_database_transactions

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

In a SQL Server instance, this dynamic management view returns a virtual table for all active

transactions that generate or potentially access row versions. Transactions are included for one

or more of the following conditions:

When either or both ALLOW_SNAPSHOT_ISOLATION and READ_COMMITTED_SNAPSHOT

database options are set to ON:

There is one row for each transaction that is running under snapshot isolation level, or

read-committed isolation level that is using row versioning.

There is one row for each transaction that causes a row version to be created in the

current database. For example, the transaction generates a row version by updating or

deleting a row in the current database.

When a trigger is fired, there is one row for the transaction under which the trigger is

executing.

When an online indexing procedure is running, there is one row for the transaction that is

creating the index.

When Multiple Active Results Sets (MARS) session is enabled, there is one row for each

transaction that is accessing row versions.

This dynamic management view does not include system transactions.

７

To call this from Azure Synapse Analytics or Analytics Platform System (PDW), use the

name

. This syntax is not

supported by serverless SQL pool in Azure Synapse Analytics.

Unique identification number assigned for the transaction.

The transaction ID is primarily used to identify the

transaction in locking operations.

Transaction sequence number. This is a unique sequence

number that is assigned to a transaction when it starts.

Transactions that do not generate version records and do

not use snapshot scans will not receive a transaction

sequence number.

Sequence number that indicates when the transaction

finishes (commits or stops). For active transactions, the value

is NULL.

0 = Is not a snapshot isolation transaction.

1 = Is a snapshot isolation transaction.

ID of the session that started the transaction.

Lowest transaction sequence number of the transactions

that were active when a snapshot was taken. On execution,

a snapshot transaction takes a snapshot of all of the active

transactions at that time. For nonsnapshot transactions, this

column shows 0.

Maximum length of the version chain that is traversed to

find the transactionally consistent version.

Average number of row versions in the version chains that

are traversed.

Elapsed time since the transaction obtained its transaction

sequence number.

: Azure Synapse Analytics, Analytics Platform

System (PDW)

ﾉ

```sql
VIEW SERVER STATE
```

```sql
VIEW DATABASE STATE
```

```sql
Server Admin
```

```sql
Azure Active Directory admin
```

```sql
w_runnable
```

```sql
w_suspended
```

```sql
w_runnable
```

```sql
52
```

```sql
SUSPENDED
```

```sql
35,094
```

```sql
SELECT
t1.session_id,
CONVERT
(
varchar
(10), t1.status)
AS
status
,
CONVERT
(
varchar
(15), t1.command)
AS
command,
CONVERT
(
varchar
(10), t2.state)
AS
worker_state,
w_suspended =
CASE
t2.wait_started_ms_ticks
WHEN
0
THEN
0
ELSE
t3.ms_ticks - t2.wait_started_ms_ticks
END
,
w_runnable =
CASE
t2.wait_resumed_ms_ticks
WHEN
0
THEN
0
ELSE
t3.ms_ticks - t2.wait_resumed_ms_ticks
END
FROM
sys.dm_exec_requests
AS
t1
INNER
JOIN
sys.dm_os_workers
AS
t2
ON
t2.task_address = t1.task_address
CROSS
JOIN
sys.dm_os_sys_info
AS
t3
WHERE
t1.scheduler_id
IS
NOT
NULL
;
session_id status     command         worker_state w_suspended w_runnable
---------- ---------- --------------- ------------ ----------- --------------------
4          background LAZY WRITER     SUSPENDED    688         688
6          background LOCK MONITOR    SUSPENDED    4657        4657
19         background BRKR TASK       SUSPENDED    603820344   603820344
14         background BRKR EVENT HNDL SUSPENDED    63583641    63583641
51         running    SELECT          RUNNING      0           0
2          background RESOURCE MONITO RUNNING      0           603825954
3          background LAZY WRITER     SUSPENDED    422         422
7          background SIGNAL HANDLER  SUSPENDED    603820485   603820485
13         background TASK MANAGER    SUSPENDED    603824704   603824704
18         background BRKR TASK       SUSPENDED    603820407   603820407
9          background TRACE QUEUE TAS SUSPENDED    454         454
52         suspended  SELECT          SUSPENDED    35094       35094
1          background RESOURCE MONITO RUNNING      0           603825954
```

```sql
sys.dm_tran_active_snapshot_database_transactions
```
