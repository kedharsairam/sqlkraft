---
title: "Deadlocks"
topic: "locking"
description: "), and the log sequence number (LSN) of the"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

(

), and the log sequence number (LSN) of the

begin

record in

the transaction log (

).

For more information, see

sys.dm_tran_database_transactions (Transact-SQL)

.

This statement lets you identify the user ID of the owner of the transaction, so you can

potentially track down the source of the transaction for the appropriate termination

(commit or roll back). For more information, see

DBCC OPENTRAN (Transact-SQL)

.

To terminate a transaction on a specific session, use the

statement. Use this statement very

carefully, however, especially when critical processes are running. For more information, see

KILL

(Transact-SQL)

.

Deadlocks are a complex topic related to locking, but different from blocking.

For more information on deadlocks, including monitoring, diagnosis, and samples, see the

Deadlocks guide

.

For more information on deadlocks specific to Azure SQL Database, see

Analyze and

prevent deadlocks in Azure SQL Database

.

Understand and resolve SQL Server blocking problems

Understand and resolve Azure SQL Database blocking problems

Transaction Related Dynamic Management Views and Functions (Transact-SQL)

Overhead of Row Versioning

sys.dm_tran_locks (Transact-SQL)

Last updated on 04/22/2026

Related content

```sql
database_transaction_state
```

```sql
database_transaction_begin_lsn
```

```sql
DBCC OPENTRAN
```

```sql
KILL
```
