---
name: "Transaction isolation levels"
title: "Transaction isolation levels"
category: "transactions"
description: ""
tags: ["tsql", "transactions"]
pubDate: 2026-05-29
---

#### Isolation level

#### Supported

#### Honored

07/16/2025

SQL Server

Azure SQL Managed Instance

doesn't guarantee that lock hints will be honored in queries that access metadata

through catalog views, compatibility views, information schema views, metadata-emitting built-

in functions.

Internally, the SQL Server Database Engine only honors the

isolation level for

metadata access. If a transaction has an isolation level that is, for example,

and

within the transaction, an attempt is made to access metadata by using catalog views or

metadata-emitting built-in functions, those queries will run until they are completed as. However, under snapshot isolation, access to metadata might fail because of

concurrent DDL operations. This is because metadata isn't versioned. Therefore, accessing the

following under snapshot isolation might fail:

Catalog views

Compatibility views

Information schema views

Metadata-emitting built-in functions

group of stored procedures

Native Client catalog procedures

Dynamic management views and functions

For more information about isolation levels, see

SET TRANSACTION ISOLATION LEVEL.

The following table provides a summary of metadata access under various isolation levels.

No

Not guaranteed

Yes

Yes

No

No

No

No

No

No

Expand table

```sql
READ COMMITTED
```

`SERIALIZABLE`

```sql
READ
COMMITTED
```

`sp_help`

```sql
READ UNCOMMITTED
```

```sql
READ COMMITTED
```

```sql
REPEATABLE READ
```

```sql
SNAPSHOT ISOLATION
```

`SERIALIZABLE`
