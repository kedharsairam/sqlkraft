---
title: "Transaction Promotion"
topic: "clr-integration"
description: "Transaction promotion describes a lightweight, local transaction that can be automatically promoted to a fully distributable transaction as needed."
tags: ["clr-integration","transaction-promotion"]
pubDate: "2025-12-01"
---

Transaction

promotion

describes a lightweight, local transaction that can be automatically

promoted to a fully distributable transaction as needed. When a managed stored procedure is

invoked within a database transaction on the server, the common language runtime (CLR) code

is run in the context of a local transaction. If you open a connection to a remote server within a

database transaction, the connection to the remote server is

enlisted

into the distributed

transaction, and the local transaction is automatically promoted to a distributed transaction.

So, transaction promotion minimizes the overhead of distributed transactions by deferring the

creation of a distributed transaction until it's needed. Transaction promotion is automatic if it

was enabled using the

keyword, and doesn't require intervention from the developer.

The.NET Framework Data Provider for SQL Server provides support for transaction promotion,

handled through the classes in the.NET Framework

namespace.

The

property of a

object supports the

keyword, which

indicates whether

detects transactional contexts and automatically

enlists the connection in a distributed transaction. If this keyword is set to true (the default), the

connection is automatically enlisted in the current transaction context of the opening thread. If

this keyword is set to false, the

connection doesn't interact with a distributed

transaction. If

isn't specified in the connection string, the connection is automatically

enlisted in a distributed transaction if one is detected at the time the connection is opened.

Distributed transactions typically consume significant system resources. Microsoft Distributed

Transaction Coordinator (MS DTC) manages such transactions, and integrates all of the

resource managers accessed in these transactions. Transaction promotion, on the other hand, is

a special form of a

transaction that effectively delegates the work to a

simple SQL Server transaction.

,

, and SQL Server

coordinate the work involved in handling the transaction, promoting it to a full distributed

transaction as needed.

The benefit of using transaction promotion is that when a connection is opened with an active

transaction, and no other connections are opened, the transaction commits

```sql
Enlist
System.Data.SqlClient
ConnectionString
SqlConnection
Enlist
System.Data.SqlClient
SqlClient
Enlist
System.Transactions
System.Transactions
System.Data.SqlClient
TransactionScope
```
