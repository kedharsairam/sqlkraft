---
title: "Control transactions"
topic: "io-fundamentals"
description: "that leave the data in a consistent state relative to the organization's business rules. The"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

that leave the data in a consistent state relative to the organization's business rules. The

application performs these modifications in a single transaction so that the Database Engine can

enforce the integrity of the transaction.

It's the responsibility of an enterprise database system, such as an instance of the Database

Engine, to provide mechanisms ensuring the integrity of each transaction. The Database Engine

provides:

Locking facilities that preserve transaction isolation.

Logging facilities to ensure transaction durability. For fully durable transactions the log

record is hardened to disk before the transactions commits. Thus, even if the server

hardware, operating system, or the instance of the Database Engine itself fails, the instance

uses the transaction logs upon restart to automatically roll back any incomplete transactions

to the point of the system failure. Delayed durable transactions commit before the

transaction log record is hardened to disk. Such transactions might be lost if there's a

system failure before the log record is hardened to disk. For more information on delayed

transaction durability, see the article

Control Transaction Durability

.

Transaction management features that enforce transaction atomicity and consistency. After

a transaction has started, it must be successfully completed (committed), or the Database

Engine undoes all of the data modifications made by the transaction since the transaction

started. This operation is referred to as rolling back a transaction because it returns the data

to the state it was prior to those changes.

Applications control transactions mainly by specifying when a transaction starts and ends. This

can be specified by using either Transact-SQL statements or database application programming

interface (API) functions. The system must also be able to correctly handle errors that terminate a

transaction before it completes. For more information, see

Transactions

,

Performing Transactions

in ODBC

, and

Transactions in SQL Server Native Client

.

By default, transactions are managed at the connection level. When a transaction is started on a

connection, all Transact-SQL statements executed on that connection are part of the transaction

until the transaction ends. However, under a multiple active result set (MARS) session, a Transact-

SQL explicit or implicit transaction becomes a batch-scoped transaction that is managed at the

batch level. When the batch completes, if the batch-scoped transaction isn't committed or rolled

back, it's automatically rolled back by the Database Engine. For more information, see

Using

Multiple Active Result Sets (MARS)

.

### Explicit transactions

### Autocommit Transactions
