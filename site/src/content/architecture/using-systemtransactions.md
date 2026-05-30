---
title: "Using System.Transactions"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  The

  namespace provides a transaction framework that is fully integrated

  with ADO.NET and SQL Server common language runtime (CLR) integration. The

  c
tags:
  - "clr-integration"
  - "using-systemtransactions"
pubDate: 2025-12-01
---

Article

•

12/30/2024

Applies to:

SQL Server

The

namespace provides a transaction framework that is fully integrated

with ADO.NET and SQL Server common language runtime (CLR) integration. The

class makes a code block transactional by implicitly

enlisting connections in a distributed transaction. You must call the

method at the

end of the code block marked by the

. The

method is invoked when

program execution leaves a code block, causing the transaction to be

discontinued

if the

method isn't called. If an exception was thrown that causes the code to leave scope,

the transaction is considered to be discontinued.

We recommend that you employ a

block to ensure that the

method is called on

the

object when the

block is exited. Failure to commit or roll back

pending transactions can seriously degrade performance because the default time-out for the

is one minute. If you don't use a

statement, you must perform all work

in a

block and explicitly call the

method in the

block.

If an exception occurs within the

, the transaction is marked as inconsistent

and is abandoned. It rolls back when the

is disposed. If no exception occurs,

participating transactions commit.

should be used only when local and remote data sources or external

resource managers are being accessed, because

always causes transactions

to promote, even if it's being used only within a context connection.

The

class creates a transaction with a

of

by default. Depending on

your application, you might want to consider lowering the isolation level to avoid high

contention in your application.

７

Note

We recommend that you perform only updates, inserts, and deletes within distributed

transactions against remote servers because they consume significant database resources.

If the operation is going to be performed on the local server, a distributed transaction isn't

necessary and a local transaction will suffice.

statements might lock database

resources unnecessarily, and in some scenarios it might be necessary to use transactions

```sql
System.Transactions
System.Transactions.TransactionScope
Complete
TransactionScope
Dispose
Complete
using
Dispose
TransactionScope
using
TransactionScope
using
Try
Dispose
Finally
TransactionScope
TransactionScope
TransactionScope
TransactionScope
TransactionScope
System.Transactions.Transaction.IsolationLevel
Serializable
SELECT
```
