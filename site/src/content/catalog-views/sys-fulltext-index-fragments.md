---
name: "sys.fulltext_index_fragments"
title: "sys.fulltext_index_fragments"
category: "indexes"
description: "A fulltext index uses internal tables called full-text index fragments to store the inverted index data. This view can be used to query the metadata about these fragments. This view contains a row for each full-text index fragment in every table that contains a full-text index. Object ID of the table that contains the full-text index fragment. fragment"
tags: ["indexes","catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT table_id, status FROM sys.fulltext_index_fragments
              WHERE status=4 OR status=6;
              USE AdventureWorks2022;
              GO
              ALTER FULLTEXT CATALOG ftCatalog REORGANIZE;
              GO
---

## Description

A fulltext index uses internal tables called full-text index fragments to store the inverted index data. This view can be used to query the metadata about these fragments. This view contains a row for each full-text index fragment in every table that contains a full-text index. Object ID of the table that contains the full-text index fragment. fragment_object_id Object ID of the internal table associated with the fragment. Logical ID of the full-text index fragment. This is unique across all fragments for this table. Timestamp associated with the fragment creation. The timestamps of more recent fragments are larger than the timestamps of older Logical size of the fragment in bytes. Number of individual rows in the fragment. Status of the fragment, one of:

## Syntax

```sql
SELECT table_id, status FROM sys.fulltext_index_fragments
WHERE status=4 OR status=6;
USE AdventureWorks2022;
GO
ALTER FULLTEXT CATALOG ftCatalog REORGANIZE;
GO
```

## Permissions

use sys.fulltext_index_fragments to query for the number of queryable fragments (status = 4 or 6) in the full-text index, as follows: If many queryable fragments exist, Microsoft recommends that you reorganize the full-text catalog that contains the full-text index to merge the fragments together. To reorganize a of full-text catalog use ALTER FULLTEXT CATALOG catalog_name REORGANIZE. For example, to reorganize a full-text catalog named in the database, enter: The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. Object Catalog Views (Transact-SQL) Populate Full-Text Indexes See Also SQL sys.fulltext_index_fragments sys.fulltext_index_columns sys.fulltext_index_catalog_usages Object catalog views (Transact-SQL) System catalog views (Transact-SQL) Create and manage full-text indexes DROP FULLTEXT INDEX (Transact-SQL) CREATE FULLTEXT INDEX (Transact-SQL) ALTER FULLTEXT INDEX (Transact-SQL) For the code example that creates this full-text index, see the section of.
## Remarks

A fulltext index uses internal tables called

full-text index fragments

to store the inverted index

data. This view can be used to query the metadata about these fragments. This view contains a

row for each full-text index fragment in every table that contains a full-text index.

Description

Object ID of the table that contains the full-text index fragment.

fragment_object_id

Object ID of the internal table associated with the fragment.

fragment_id

Logical ID of the full-text index fragment. This is unique across all

fragments for this table.

Timestamp associated with the fragment creation. The timestamps of

more recent fragments are larger than the timestamps of older

Logical size of the fragment in bytes.

Number of individual rows in the fragment.

Status of the fragment, one of:

0 = Newly created and not yet used

1 = Being used for insert during fulltext index population or merge

4 = Closed. Ready for query

6 = Being used for merge input and ready for query

8 = Marked for deletion. Will not be used for query and merge source.

A status of 4 or 6 means that the fragment is part of the logical full-

text index and can be queried; that is, it is a

The sys.fulltext_index_fragments catalog view can be used to query the number of fragments

comprising a full-text index. If you are experiencing slow full-text query performance, you can

Expand table

## Examples

### Example 1

```sql
USE
AdventureWorks2025;
GO
SELECT object_id,
property_list_id,
stoplist_id
FROM sys.fulltext_indexes
WHERE object_id = object_id(
'HumanResources.JobCandidate'
);
```
