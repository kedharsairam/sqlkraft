---
title: "Customize transaction isolation level"
topic: "io-fundamentals"
description: "an application doesn't trap the error, the application can proceed unaware that an individual"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

an application doesn't trap the error, the application can proceed unaware that an individual

statement within a transaction has been canceled but the transaction remains active. Errors can

occur because statements later in the transaction might depend on the statement that was never

executed.

Implementing an error handler that traps error message 1222 allows an application to handle the

timeout situation and take remedial action, such as: automatically resubmitting the statement

that was blocked or rolling back the entire transaction.

To determine the current

setting, execute the

function:

is the default isolation level for the Database Engine. If an application must

operate at a different isolation level, it can use the following methods to set the isolation level:

Run the

SET TRANSACTION ISOLATION LEVEL

statement.

ADO.NET applications that use the

or

namespace can specify an

option by using the

method.

Applications that use ADO can set the

property.

When starting a transaction, applications using OLE DB can call

with

set to the desired transaction isolation

level. When specifying the isolation level in autocommit mode, applications that use OLE DB

can set the

property

to the desired

transaction isolation level.

）

Important

Applications that use explicit transactions and require the transaction to terminate upon

receiving error 1222 must explicitly roll back the transaction as part of error handling.

Without this, other statements can unintentionally execute on the same session while the

transaction remains active, leading to unbounded transaction log growth and data loss if the

transaction is rolled back later.

Applications that use ODBC can set the

attribute by using

.

When the isolation level is specified, the locking behavior for all queries and data manipulation

language (DML) statements in the session operates at that isolation level. The isolation level

remains in effect until the session terminates or until the isolation level is set to another level.

The following example sets the

isolation level:

The isolation level can be overridden for individual query or DML statements, if necessary, by

specifying a table-level hint. Specifying a table-level hint doesn't affect other statements in the

session.

To determine the transaction isolation level currently set, use the

statement as

shown in the following example. The result set might vary from the result set on your system.

Here's the result set.

`LOCK_TIMEOUT`

```sql
@@LOCK_TIMEOUT
```

```sql
READ COMMITTED
```

`Microsoft.Data.SqlClient`

`System.Data.SqlClient`

`IsolationLevel`

`SqlConnection.BeginTransaction`

```sql
Autocommit Isolation Levels
```

```sql
ITransactionLocal::StartTransaction
```

`isoLevel`

`DBPROPSET_SESSION`

`DBPROP_SESS_AUTOCOMMITISOLEVELS`

```sql
SELECT
@@LOCK_TIMEOUT;
GO
```

`SQL_COPT_SS_TXN_ISOLATION`

`SQLSetConnectAttr`

`SERIALIZABLE`

```sql
DBCC USEROPTIONS
```

```sql
USE
AdventureWorks2022;
GO
SET
TRANSACTION
ISOLATION
LEVEL
SERIALIZABLE
;
GO
BEGIN
TRANSACTION
;
SELECT
BusinessEntityID
FROM
HumanResources.Employee;
COMMIT
;
GO
USE
AdventureWorks2022;
GO
SET
TRANSACTION
ISOLATION
LEVEL
REPEATABLE
READ
;
GO
DBCC USEROPTIONS;
GO
Set Option                   Value
---------------------------- -------------------------------------------
textsize                     2147483647 language                     us_english
```
