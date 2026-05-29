---
name: 'sys.sp_xtp_unbind_db_resource_pool'
title: 'sys.sp_xtp_unbind_db_resource_pool'
category: 'general'
description: 'This system procedure removes an existing binding between a database and a resource pool'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

The following code unbinds the database

from the In-Memory OLTP resource pool

it's bound to. If

isn't currently bound to a In-Memory OLTP resource pool, a

message is given. The database must be restarted for the unbinding to take effect.

SQL

The database specified by

@database_name

must have a binding to an In-Memory OLTP

resource pool.

Requires CONTROL SERVER permission.

Bind a Database with Memory-Optimized Tables to a Resource Pool

sys.sp_xtp_bind_db_resource_pool (Transact-SQL)

Related content

```sql
Hekaton_DB
```

```sql
Hekaton_DB
```

```sql
Msg 41374, Level 16, State 1, Procedure sp_xtp_unbind_db_resource_pool_internal,
Line 140.
Database 'Hekaton_DB' does not have a binding to a resource pool.
```

```sql
EXECUTE
sys.sp_xtp_unbind_db_resource_pool N
'Hekaton_DB'
;
```
