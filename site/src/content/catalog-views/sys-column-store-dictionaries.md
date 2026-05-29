---
name: 'sys.column_store_dictionaries'
title: 'sys.column_store_dictionaries (Transact-'
category: 'objects'
description: 'Indicates the partition ID. Is unique within a database.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
Indicates the partition ID. Is unique within a database.

Requires

permission on the table. The following columns return null unless

the user also has

permission: last_id, entry_count, data_ptr.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.columns (Transact-SQL)

sys.all_columns (Transact-SQL)

sys.computed_columns (Transact-SQL)

Columnstore Indexes Guide

Columnstore Indexes Guide

sys.column_store_segments (Transact-SQL)

See Also

```sql
VIEW DEFINITION
```

```sql
SELECT
```
