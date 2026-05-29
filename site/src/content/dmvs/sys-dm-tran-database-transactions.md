---
title: sys.dm_tran_database_transactions
name: sys.dm_tran_database_transactions
category: execution
description:
pubDate: 2026-05-29
---

The following example returns information that associates a

with a Windows thread

ID. The performance of the thread can be monitored in the Windows Performance Monitor. This

query does not return a

that is currently sleeping.

SQL

sys.dm_tran_database_transactions (Transact-SQL)

Transaction locking and row versioning guide

System dynamic management views

Transaction Related Dynamic Management Views and Functions (Transact-SQL)

SQL Server, Locks object

Last updated on 11/18/2025

## Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

The

dynamic management view returns correlation

information for associated transactions and sessions.

ID of the session under which the transaction is running.

ID of the transaction.

Transaction identifier used by SQL Server when communicating

with the client driver.

Number of active requests in the session working on the

transaction.

1 = The transaction was initiated by a user request.

0 = System transaction.

1 = Local transaction.

0 = Distributed transaction or an enlisted bound session

transaction.

1 = Enlisted distributed transaction.

0 = Not an enlisted distributed transaction.

1 = The transaction is active on the session via bound sessions.

0 = The transaction is not active on the session via bound

sessions.

The number of open transactions for each session.

: Azure Synapse Analytics, Analytics Platform System

(PDW)

ﾉ

## Contributor

## Basic

## S0

## S1

## elastic pools

```sql
session_id
```

```sql
session_id
```

```sql
ROLLBACK
;
GO
```

```sql
SELECT
STasks.session_id, SThreads.os_thread_id
FROM
sys.dm_os_tasks
AS
STasks
INNER
JOIN
sys.dm_os_threads
AS
SThreads
ON
STasks.worker_address = SThreads.worker_address
WHERE
STasks.session_id
IS
NOT
NULL
ORDER
BY
STasks.session_id;
GO
```

```sql
sys.dm_tran_session_transactions
```

```sql
session_id
```

```sql
transaction_id
```

```sql
transaction_descriptor
```

```sql
enlist_count
```

```sql
is_user_transaction
```

```sql
is_local
```

```sql
is_enlisted
```

```sql
is_bound
```

```sql
open_transaction_count
```

```sql
pdw_node_id
```
