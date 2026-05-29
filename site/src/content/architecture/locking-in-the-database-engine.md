---
title: "Locking in the Database Engine"
topic: "locking"
description: "For more information about the specific types of locking or row versioning controlled by each"
tags: ["locking", "architecture"]
pubDate: 2026-05-29
---

For more information about the specific types of locking or row versioning controlled by each

transaction isolation level, see

SET TRANSACTION ISOLATION LEVEL (Transact-SQL)

.

Transaction isolation levels can be set using Transact-SQL or through a database API.

Transact-SQL scripts use the

statement.

ADO applications set the

property of the

object to

,

,

, or

.

ADO.NET applications using the

or

managed

namespace can call the

method and set the

option to

,

,

,

,

,

,

or

.

When starting a transaction, applications using OLE DB call

with

set to

,

,

,

, or

.

When specifying the transaction isolation level in autocommit mode, OLE DB applications can set

the

property

to

,

,

,

,

,

,

,

, or

.

ODBC applications call

with

set to

and

set to

,

,

, or

.

For snapshot transactions, applications call

with Attribute set to

and

set to

. A snapshot transaction can

be retrieved using either

or

.

```sql
SET TRANSACTION ISOLATION LEVEL
```

```sql
IsolationLevel
```

```sql
Connection
```

```sql
adXactReadUncommitted
```

```sql
adXactReadCommitted
```

```sql
adXactRepeatableRead
```

```sql
adXactReadSerializable
```

```sql
Microsoft.Data.SqlClient
```

```sql
System.Data.SqlClient
```

```sql
SqlConnection.BeginTransaction
```

```sql
IsolationLevel
```

```sql
Unspecified
```

```sql
Chaos
```

```sql
ReadUncommitted
```

```sql
ReadCommitted
```

```sql
RepeatableRead
```

```sql
Serializable
```

```sql
Snapshot
```

```sql
ITransactionLocal::StartTransaction
```

```sql
isoLevel
```

```sql
ISOLATIONLEVEL_READUNCOMMITTED
```

```sql
ISOLATIONLEVEL_READCOMMITTED
```

```sql
ISOLATIONLEVEL_REPEATABLEREAD
```

```sql
ISOLATIONLEVEL_SNAPSHOT
```

```sql
ISOLATIONLEVEL_SERIALIZABLE
```

```sql
DBPROPSET_SESSION
```

```sql
DBPROP_SESS_AUTOCOMMITISOLEVELS
```

```sql
DBPROPVAL_TI_CHAOS
```

```sql
DBPROPVAL_TI_READUNCOMMITTED
```

```sql
DBPROPVAL_TI_BROWSE
```

```sql
DBPROPVAL_TI_CURSORSTABILITY
```

```sql
DBPROPVAL_TI_READCOMMITTED
```

```sql
DBPROPVAL_TI_REPEATABLEREAD
```

```sql
DBPROPVAL_TI_SERIALIZABLE
```

```sql
DBPROPVAL_TI_ISOLATED
```

```sql
DBPROPVAL_TI_SNAPSHOT
```

```sql
SQLSetConnectAttr
```

```sql
Attribute
```

```sql
SQL_ATTR_TXN_ISOLATION
```

```sql
ValuePtr
```

```sql
SQL_TXN_READ_UNCOMMITTED
```

```sql
SQL_TXN_READ_COMMITTED
```

```sql
SQL_TXN_REPEATABLE_READ
```

```sql
SQL_TXN_SERIALIZABLE
```

```sql
SQLSetConnectAttr
```

```sql
SQL_COPT_SS_TXN_ISOLATION
```

```sql
ValuePtr
```

```sql
SQL_TXN_SS_SNAPSHOT
```

```sql
SQL_COPT_SS_TXN_ISOLATION
```

```sql
SQL_ATTR_TXN_ISOLATION
```
