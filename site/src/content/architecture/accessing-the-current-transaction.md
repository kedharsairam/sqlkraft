---
title: "Accessing the Current Transaction"
topic: "clr-integration"
description: ""
tags: ["clr-integration","accessing-the-current-transaction"]
pubDate: 2025-12-01
---

If a transaction is active at the point at which common language runtime (CLR) code running

on SQL Server is entered, the transaction is exposed through the

class. The

property is used to access

the current transaction. In most cases, it's not necessary to access the transaction explicitly. For

database connections, ADO.NET checks

automatically when the

method is called, and transparently enlists the connection in that transaction

(unless the

keyword is set to false in the connection string).

You might want to use the

object directly in the following scenarios:

If you want to enlist a resource that doesn't do automatic enlistment, or that for some

reason wasn't enlisted during initialization.

If you want to explicitly enlist a resource in the transaction.

If you want to terminate the external transaction from within your stored procedure or

function. In this case, you use

TransactionScope. For example, the following code rolls

back the current transaction:

C#

The rest of this article describes other ways to cancel an external transaction.

You can cancel external transactions from a managed procedure or function in the following

ways:

The managed procedure or function can return a value by using an output parameter.

The calling Transact-SQL procedure can check the returned value and, if appropriate,

execute.

The managed procedure or function can throw a custom exception. The calling Transact-

SQL procedure can catch the exception thrown by the managed procedure or function in

a try/catch block and execute.

```sql
System.Transactions.Transaction
Transaction.Current
Transaction.Current
Connection.Open
Enlist
Transaction
ROLLBACK TRANSACTION
ROLLBACK TRANSACTION using (TransactionScope transactionScope =
new
TransactionScope(TransactionScopeOptions.Required)) { }
```
