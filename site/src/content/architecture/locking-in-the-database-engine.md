---
title: "Locking in the Database Engine"
topic: "locking"
description: ""
tags: ["locking","architecture"]
pubDate: 2026-05-29
---

For more information about the specific types of locking or row versioning controlled by each

transaction isolation level, see

SET TRANSACTION ISOLATION LEVEL (Transact-SQL).

Transaction isolation levels can be set using Transact-SQL or through a database API.

Transact-SQL scripts use the

statement.

ADO applications set the

property of the

object to

,

,

, or.

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

or.

When starting a transaction, applications using OLE DB call

with

set to

,

,

,

, or.

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

, or.

ODBC applications call

with

set to

and

set to

,

,

, or.

For snapshot transactions, applications call

with Attribute set to

and

set to. A snapshot transaction can

be retrieved using either

or.

```sql
SET TRANSACTION ISOLATION LEVEL
```

`IsolationLevel`

`Connection`

`adXactReadUncommitted`

`adXactReadCommitted`

`adXactRepeatableRead`

`adXactReadSerializable`

`Microsoft.Data.SqlClient`

`System.Data.SqlClient`

`SqlConnection.BeginTransaction`

`IsolationLevel`

`Unspecified`

`Chaos`

`ReadUncommitted`

`ReadCommitted`

`RepeatableRead`

`Serializable`

`Snapshot`

```sql
ITransactionLocal::StartTransaction
```

`isoLevel`

`ISOLATIONLEVEL_READUNCOMMITTED`

`ISOLATIONLEVEL_READCOMMITTED`

`ISOLATIONLEVEL_REPEATABLEREAD`

`ISOLATIONLEVEL_SNAPSHOT`

`ISOLATIONLEVEL_SERIALIZABLE`

`DBPROPSET_SESSION`

`DBPROP_SESS_AUTOCOMMITISOLEVELS`

`DBPROPVAL_TI_CHAOS`

`DBPROPVAL_TI_READUNCOMMITTED`

`DBPROPVAL_TI_BROWSE`

`DBPROPVAL_TI_CURSORSTABILITY`

`DBPROPVAL_TI_READCOMMITTED`

`DBPROPVAL_TI_REPEATABLEREAD`

`DBPROPVAL_TI_SERIALIZABLE`

`DBPROPVAL_TI_ISOLATED`

`DBPROPVAL_TI_SNAPSHOT`

`SQLSetConnectAttr`

`Attribute`

`SQL_ATTR_TXN_ISOLATION`

`ValuePtr`

`SQL_TXN_READ_UNCOMMITTED`

`SQL_TXN_READ_COMMITTED`

`SQL_TXN_REPEATABLE_READ`

`SQL_TXN_SERIALIZABLE`

`SQLSetConnectAttr`

`SQL_COPT_SS_TXN_ISOLATION`

`ValuePtr`

`SQL_TXN_SS_SNAPSHOT`

`SQL_COPT_SS_TXN_ISOLATION`

`SQL_ATTR_TXN_ISOLATION`
