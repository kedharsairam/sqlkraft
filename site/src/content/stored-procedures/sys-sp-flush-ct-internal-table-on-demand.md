---
name: 'sys.sp_flush_CT_internal_table_on_demand'
title: 'sys.sp_flush_CT_internal_table_on_demand'
category: 'general'
description: 'Azure SQL Managed Instance'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

must be run in the context of the

system

database. Collection items can't be deleted from system collection sets.

The collection set that contains the collection item is stopped and restarted during this

operation.

Requires membership in the

(with EXECUTE permission) fixed database role to

execute this procedure.

The following example deletes a collection item named

.

SQL

Data collection

sp_syscollector_create_collection_item (Transact-SQL)

Data collector stored procedures (Transact-SQL)

syscollector_collection_items (Transact-SQL)

Related content

```sql
sp_syscollector_delete_collection_item
```

```sql
msdb
```

```sql
MyCollectionItem1
```

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_delete_collection_item @
name
=
'MyCollectionItem1'
;
```
