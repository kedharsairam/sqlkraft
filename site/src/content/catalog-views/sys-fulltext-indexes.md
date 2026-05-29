---
name: 'sys.fulltext_indexes'
title: 'sys.fulltext_indexes'
category: 'indexes'
description: '= Update crawl, based on notifications'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

## Description
= Update crawl, based on notifications

= Full crawl is paused.


## Description of the current or last crawl type.
Start of the current or last crawl.

= None.

End of the current or last crawl.

= None.

Timestamp value to use for the next incremental crawl.

= None.

ID of the

stoplist

that is associated with this full-text index.

Filegroup where this full-text index resides.

ID of the search property list that is associated with this

full-text index.

indicates that no search property list is

associated with the full-text index. To obtain more

information about this search property list, use the

sys.registered_search_property_lists

catalog view.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission.

The following example uses a full-text index on the

table of the

sample database. The example returns the object ID of the table, the

search property list ID, and the stoplist ID of the stoplist used by the full-text index.

７

Note

SQL

sys.fulltext_index_fragments

sys.fulltext_index_columns

sys.fulltext_index_catalog_usages

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

Create and manage full-text indexes

DROP FULLTEXT INDEX (Transact-SQL)

CREATE FULLTEXT INDEX (Transact-SQL)

ALTER FULLTEXT INDEX (Transact-SQL)

Last updated on 12/02/2025

For the code example that creates this full-text index, see the

section of

.

Related content

```sql
U
```

```sql
P
```

```sql
crawl_type_desc
```

```sql
FULL_CRAWL
INCREMENTAL_CRAWL
UPDATE_CRAWL
PAUSED_FULL_CRAWL
crawl_start_date
```

```sql
NULL
```

```sql
crawl_end_date
```

```sql
NULL
```

```sql
incremental_timestamp
```

```sql
NULL
```

```sql
stoplist_id
```

```sql
data_space_id
```

```sql
property_list_id
```

```sql
NULL
```

```sql
HumanResources.JobCandidate
```

```sql
AdventureWorks2025
```

```sql
USE
AdventureWorks2025;
GO
SELECT
object_id,
property_list_id,
stoplist_id
FROM
sys.fulltext_indexes
WHERE
object_id = object_id(
'HumanResources.JobCandidate'
);
```
