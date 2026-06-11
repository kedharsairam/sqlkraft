---
title: "Replication transactions"
topic: "io-fundamentals"
description: "The active log must include every part of all uncommitted transactions."
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

The active log must include every part of all uncommitted transactions. An application that

starts a transaction and doesn't commit it or roll it back prevents the Database Engine from

advancing the MinLSN. This situation can cause two types of problems:

If the system is shut down after the transaction has performed many uncommitted

modifications, the recovery phase of the subsequent restart can take much longer than

the time specified in the

option.

The log might grow very large, because the log can't be truncated past the MinLSN. This

occurs even if the database is using the simple recovery model, in which the transaction

log is truncated on each automatic checkpoint.

Recovery of long-running transactions, and the problems described in this article, can be

avoided by using

Accelerated database recovery

, a feature available starting with SQL Server

2019 (15.x) and in Azure SQL Database.

The Log Reader Agent monitors the transaction log of each database configured for

transactional replication, and it copies the transactions marked for replication from the

transaction log into the distribution database. The active log must contain all transactions that

are marked for replication, but that haven't yet been delivered to the distribution database. If

these transactions aren't replicated in a timely manner, they can prevent the truncation of the

log. For more information, see

Transactional Replication

.

The transaction log

Manage the size of the transaction log file

Transaction log backups (SQL Server)

Database checkpoints (SQL Server)

Server configuration: recovery interval (min)

Accelerated database recovery

sys.dm_db_log_info (Transact-SQL)

sys.dm_db_log_space_usage (Transact-SQL)

Understanding Logging and Recovery in SQL Server

Last updated on 11/18/2025

Related content
