---
title: "Create, Alter, & Drop Secondary Indexes"
topic: "xml-data"
description: ""
tags: ["xml-data","create-alter-drop-secondary-indexes"]
pubDate: 2025-12-01
---

Describes how to create a new secondary selective XML index, or alter or drop an existing

secondary selective XML index.

You can create a secondary selective XML index using Transact-SQL by calling the CREATE XML

INDEX statement. For more information, see

CREATE XML INDEX (Selective XML Indexes).

The following example creates a secondary selective XML index on the path. The

path to index is identified by the name that was given to it when it was created with the

CREATE SELECTIVE XML INDEX statement. For more information, see

CREATE SELECTIVE XML

INDEX (Transact-SQL).

The ALTER statement isn't supported for secondary selective XML indexes. To change a

secondary selective XML index, drop the existing index and recreate it.

1. Drop the existing secondary selective XML index by calling the DROP INDEX statement.

For more information, see

DROP INDEX (Selective XML Indexes).

2. Recreate the index with the desired options by calling the CREATE XML INDEX statement.

For more information, see

CREATE XML INDEX (Selective XML Indexes).

The following example changes a secondary selective XML index by dropping it and recreating

it.

```sql
'pathabc'
CREATE
XML
INDEX filt_sxi_index_c
ON
Tbl(xmlcol)
USING
XML
INDEX sxi_index
FOR (
pathabc
);
```
