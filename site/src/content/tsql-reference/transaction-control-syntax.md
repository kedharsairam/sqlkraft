---
name: "Transaction control syntax"
title: "Transaction control syntax"
category: "transactions"
description: ""
tags: ["tsql","transactions"]
pubDate: "2026-05-29"
---

Warehouse in Microsoft Fabric

A transaction is a single unit of work. If a transaction is successful, all of the data modifications

made during the transaction are committed and become a permanent part of the database. If a

transaction encounters errors and must be canceled or rolled back, then all of the data

modifications are erased.

operates in the following transaction modes:

## Description

Each individual statement is a transaction.

explicitly ended with a

or

statement.

transaction is explicitly completed with a

or

statement.

Applicable only to multiple active result sets (MARS), a Transact-SQL explicit or implicit

transaction that starts under a MARS session becomes a batch-scoped transaction. A

batch-scoped transaction that isn't committed or rolled back when a batch completes

is automatically rolled back by SQL Server.

Transactions in Fabric Data

Warehouse

or

Transactions (Azure Synapse Analytics).

The SQL Database Engine provides the following transaction statements:

BEGIN DISTRIBUTED TRANSACTION

ROLLBACK TRANSACTION

BEGIN TRANSACTION

ROLLBACK WORK

COMMIT TRANSACTION

SAVE TRANSACTION

COMMIT WORK

SET IMPLICIT_TRANSACTIONS (Transact-SQL)

@@TRANCOUNT (Transact-SQL)
