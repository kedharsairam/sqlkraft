---
name: "Transaction control syntax"
title: "Transaction control syntax"
category: "transactions"
description: "Azure SQL Managed Instance"
tags: ["tsql", "transactions"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

A transaction is a single unit of work. If a transaction is successful, all of the data modifications

made during the transaction are committed and become a permanent part of the database. If a

transaction encounters errors and must be canceled or rolled back, then all of the data

modifications are erased.

SQL Server operates in the following transaction modes:

## Description

Each individual statement is a transaction.

Each transaction is explicitly started with the

statement and

explicitly ended with a

or

statement.

A new transaction is implicitly started when the prior transaction completes, but each

transaction is explicitly completed with a

or

statement.

Applicable only to multiple active result sets (MARS), a Transact-SQL explicit or implicit

transaction that starts under a MARS session becomes a batch-scoped transaction. A

batch-scoped transaction that isn't committed or rolled back when a batch completes

is automatically rolled back by SQL Server.

For special considerations related to data warehouse products, see

Transactions in Fabric Data

Warehouse

or

Transactions (Azure Synapse Analytics)

.

The SQL Database Engine provides the following transaction statements:

BEGIN DISTRIBUTED TRANSACTION

ROLLBACK TRANSACTION

BEGIN TRANSACTION

ROLLBACK WORK

COMMIT TRANSACTION

SAVE TRANSACTION

COMMIT WORK

ﾉ

Expand table

SET IMPLICIT_TRANSACTIONS (Transact-SQL)

@@TRANCOUNT (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
BEGIN TRANSACTION
```

```sql
COMMIT
```

```sql
ROLLBACK
```

```sql
COMMIT
```

```sql
ROLLBACK
```
