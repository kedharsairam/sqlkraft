---
title: "Disk space requirements"
topic: "filestream"
description: "Disk space is an important consideration when you create, rebuild, or drop indexes. Inadequat"
tags: ["filestream","disk-space-requirements"]
pubDate: "2025-12-01"
---

Disk space is an important consideration when you create, rebuild, or drop indexes. Inadequate

disk space can degrade performance or even cause the index operation to fail. This article

provides general information that can help you determine the amount of disk space required

for index data definition language (DDL) operations.

The following index operations require no additional disk space:

; however, log space is required.

when you're dropping a nonclustered index.

when you're dropping a clustered index offline without specifying the

clause and nonclustered indexes don't exist.

(

or

constraints)

All other index DDL operations require additional temporary disk space to use during the

operation, and permanent disk space to store the new index structure or structures.

When a new index structure is created, disk space for both the old (source) and new (target)

structures is required in their appropriate files and filegroups. The old structure isn't

deallocated until the index creation transaction commits.

The following index DDL operations create new index structures and require additional disk

space:

(

or

)

```sql
ALTER INDEX REORGANIZE
DROP INDEX
DROP INDEX
MOVE
TO
CREATE TABLE
PRIMARY KEY
UNIQUE
CREATE INDEX
CREATE INDEX WITH DROP_EXISTING
ALTER INDEX REBUILD
ALTER TABLE ADD CONSTRAINT
PRIMARY KEY
UNIQUE
```
