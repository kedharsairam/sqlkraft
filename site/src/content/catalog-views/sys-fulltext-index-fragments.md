---
name: 'sys.fulltext_index_fragments'
title: 'sys.fulltext_index_fragments'
category: 'indexes'
description: 'use sys.fulltext_index_fragments to query for the number of queryable fragments (status = 4 or'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

use sys.fulltext_index_fragments to query for the number of queryable fragments (status = 4 or

6) in the full-text index, as follows:

If many queryable fragments exist, Microsoft recommends that you reorganize the full-text

catalog that contains the full-text index to merge the fragments together. To reorganize a of

full-text catalog use

ALTER FULLTEXT CATALOG

catalog_name

REORGANIZE. For example, to

reorganize a full-text catalog named

in the

database, enter:

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission.

Object Catalog Views (Transact-SQL)

Populate Full-Text Indexes

See Also

```sql
ftCatalog
```

```sql
AdventureWorks2022
```

```sql
SELECT table_id, status FROM sys.fulltext_index_fragments
WHERE status=4 OR status=6;
USE AdventureWorks2022;
GO
ALTER FULLTEXT CATALOG ftCatalog REORGANIZE;
GO
```
