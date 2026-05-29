---
name: 'sys.dm_tran_transactions_snapshot'
title: 'sys.dm_tran_transactions_snapshot'
category: 'io'
description: 'Transaction sequence number (XSN) of a snapshot transaction. Snapshot ID for each Transact-SQL statement started under read- committed using row versioning. This value is used to generate a transactionally consistent view of the database supporting each query that is being run under read-committed using row Transaction sequence number of a transaction that was active when the snapshot transaction '
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: 'transaction_sequence_num'
---

## Description

Transaction sequence number (XSN) of a snapshot transaction. Snapshot ID for each Transact-SQL statement started under read- committed using row versioning. This value is used to generate a transactionally consistent view of the database supporting each query that is being run under read-committed using row Transaction sequence number of a transaction that was active when the snapshot transaction started. On SQL Server and SQL Managed Instance, requires On SQL Database service objectives, and for databases in Microsoft Entra admin account, or membership in the is required. On all other SQL Database service objectives, permission on the database, or membership in the server role is required. Requires VIEW SERVER PERFORMANCE STATE permission on the server. When a snapshot transaction starts, the Database Engine records all of the transactions that are

## Syntax

```sql
transaction_sequence_num
```

## Remarks

Transaction sequence number (XSN) of a snapshot transaction.

Snapshot ID for each Transact-SQL statement started under read-

committed using row versioning. This value is used to generate a

transactionally consistent view of the database supporting each

query that is being run under read-committed using row

versioning.

Transaction sequence number of a transaction that was active

when the snapshot transaction started.

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

service objectives, and for databases in

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

When a snapshot transaction starts, the Database Engine records all of the transactions that are

active at that time.

reports this information for all currently

active snapshot transactions.

Each transaction is identified by a transaction sequence number that is assigned when the

transaction begins. Transactions start at the time a BEGIN TRANSACTION or BEGIN WORK

statement is executed. However, the Database Engine assigns the transaction sequence

number with the execution of the first Transact-SQL statement that accesses data after the
