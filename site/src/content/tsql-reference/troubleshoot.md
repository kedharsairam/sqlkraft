---
name: "Troubleshoot"
title: "Troubleshoot"
category: "statements"
description: "Consider the following information when you plan to shrink a file:"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## The file doesn't shrink

Consider the following information when you plan to shrink a file:

A shrink operation is most effective after an operation that creates a large amount of

unused space, such as a truncate table or a drop table operation.

Most databases require some free space to be available for regular day-to-day

operations. If you shrink a database file repeatedly and notice that the database size

grows again, this indicates that the free space is required for regular operations. In these

cases, repeatedly shrinking the database file is a wasted operation. Autogrow events

necessary to grow the database file a hinder performance.

A shrink operation doesn't preserve the fragmentation state of indexes in the database,

and generally increases fragmentation to a degree. This fragmentation is another reason

not to repeatedly shrink the database.

Shrink multiple files in the same database sequentially instead of concurrently.

Contention on system tables can cause blocking and lead to delays.

This section describes how to diagnose and correct issues that can occur when running the

command.

If the file size doesn't change after an error-less shrink operation, try the following to verify that

the file has adequate free space:

Run the following query.

SQL

Run the

DBCC SQLPERF

command to return the space used in the transaction log.

The shrink operation can't reduce the file size any further if there's insufficient free space

available.

```sql
DBCC SHRINKFILE
```

```sql
SELECT
name
,
size
/ 128.0 -
CAST
(FILEPROPERTY(
name
,
'SpaceUsed'
)
AS
INT
) / 128.0
AS
AvailableSpaceInMB
FROM
sys.database_files;
```
