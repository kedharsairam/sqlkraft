---
name: 'sys.hash_indexes'
title: 'sys.hash_indexes'
category: 'indexes'
description: 'SQL Server 2014 (12.x) and later'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server 2014 (12.x) and later

Azure SQL Database

Azure SQL

Managed Instance

Shows the current hash indexes and the hash index properties. Hash indexes are supported

only on

In-Memory OLTP (In-Memory Optimization)

.

The sys.hash_indexes view contains the same columns as the sys.indexes view and an additional

column named

. For more information about the other columns in the

sys.hash_indexes view, see

sys.indexes (Transact-SQL)

.


## Description
Inherits columns from

sys.indexes (Transact-SQL)

.

Count of hash buckets for hash indexes.

For more information about the bucket_count value, including guidelines

for setting the value, see

CREATE TABLE (Transact-SQL)

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission.. For more information, see

Metadata

Visibility Configuration

.

ﾉ

Expand table

See Also

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

```sql
SELECT object_name([object_id]) AS 'table_name', [object_id],
[name] AS 'index_name', [type_desc], [bucket_count]
FROM sys.hash_indexes
WHERE OBJECT_NAME([object_id]) = 'T1';
```
