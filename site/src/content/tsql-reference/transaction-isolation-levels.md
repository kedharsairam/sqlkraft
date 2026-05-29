---
name: 'Transaction isolation levels'
title: 'Transaction isolation levels'
category: 'transactions'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "transactions"]
pubDate: 2026-05-29
---

#### Isolation level

#### Supported

#### Honored

07/16/2025

Applies to:

SQL Server

Azure SQL Managed Instance

SQL Server doesn't guarantee that lock hints will be honored in queries that access metadata

through catalog views, compatibility views, information schema views, metadata-emitting built-

in functions.

Internally, the SQL Server Database Engine only honors the

isolation level for

metadata access. If a transaction has an isolation level that is, for example,

and

within the transaction, an attempt is made to access metadata by using catalog views or

metadata-emitting built-in functions, those queries will run until they are completed as

. However, under snapshot isolation, access to metadata might fail because of

concurrent DDL operations. This is because metadata isn't versioned. Therefore, accessing the

following under snapshot isolation might fail:

Catalog views

Compatibility views

Information schema views

Metadata-emitting built-in functions

group of stored procedures

SQL Server Native Client catalog procedures

Dynamic management views and functions

For more information about isolation levels, see

SET TRANSACTION ISOLATION LEVEL

.

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

ﾉ

Expand table

```sql
READ COMMITTED
```

```sql
SERIALIZABLE
```

```sql
READ
COMMITTED
```

```sql
sp_help
```

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

```sql
SERIALIZABLE
```
