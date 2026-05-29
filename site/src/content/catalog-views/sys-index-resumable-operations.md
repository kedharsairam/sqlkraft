---
name: 'sys.index_resumable_operations'
title: 'sys.index_resumable_operations (Transact-'
category: 'indexes'
description: 'The visibility of the metadata in catalog views is limited to securables that a user either owns,'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

List all resumable index creation or rebuild operations that are in the PAUSE state.

SQL

ALTER INDEX

CREATE INDEX

Catalog views

Object catalog views

sys.indexes

sys.index_columns

sys.xml_indexes

sys.objects

sys.key_constraints

sys.filegroups

sys.partition_schemes

Querying the SQL Server System Catalog FAQ

Last updated on 11/18/2025

See Also

```sql
SELECT
*
FROM
sys.index_resumable_operations
WHERE
STATE = 1;
```
