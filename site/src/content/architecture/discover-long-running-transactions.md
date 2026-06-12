---
title: "Discover long-running transactions"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

In addition, when the

isolation level is enabled, although a new transaction won't hold

locks, a long-running transaction will prevent the old versions from being removed from the

version store.

A

long-running transaction

is an active transaction that hasn't been committed or roll backed in a

timely manner. For example, if the beginning and end of a transaction is controlled by the user, a

typical cause of a long-running transaction is a user starting a transaction and then leaving while

the transaction waits for a response from the user.

A long running transaction can cause serious problems for a database, as follows:

If a server instance is shut down after an active transaction has performed many

uncommitted modifications, the recovery phase of the subsequent restart can take much

longer than the time specified by the

server configuration option or by

the

option. These options control active and

indirect checkpoints, respectively. For more information about the types of checkpoints, see

Database checkpoints (SQL Server).

More importantly, although a waiting transaction might generate very little log, it holds up

log truncation indefinitely, causing the transaction log to grow and possibly fill up. If the

transaction log fills up, the database can't perform any more writes. For more information,

see

transaction log architecture and management guide

,

Troubleshoot a full

transaction log (SQL Server Error 9002)

, and

The transaction log.

To look for long-running transactions, use one of the following:

This dynamic management view returns information about transactions at the database

level. For a long-running transaction, columns of particular interest include the time of the

first log record (

), the current state of the transaction

）

Important

In Azure SQL Database, idle transactions (transactions that haven't written to the transaction

log for six hours) are automatically terminated to free up resources.

`SNAPSHOT`

```sql
recovery interval
```

```sql
ALTER DATABASE. SET TARGET_RECOVERY_TIME
```

`sys.dm_tran_database_transactions`

`database_transaction_begin_time`
