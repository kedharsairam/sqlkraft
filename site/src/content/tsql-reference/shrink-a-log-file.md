---
name: "Shrink a log file"
title: "Shrink a log file"
category: "statements"
description: "Currently, LOB column types ("
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Currently, LOB column types (

,

, and

) in

compressed columnstore segments are not affected by

and.

The shrink database and shrink file commands can lead to concurrency issues, especially with

active maintenance such as rebuilding indexes, or on busy OLTP environments. When your

application executes queries against database tables, these queries will acquire and maintain a

schema stability lock (Sch-S) until the queries complete their operations. When attempting to

reclaim space during regular usage, shrink database and shrink file operations currently require

a schema modify lock (Sch-M) when moving or deleting Index Allocation Map (IAM) pages,

blocking the Sch-S locks needed by user queries. As a result, long-running queries will block a

shrink operation until the queries complete. This means that any new queries requiring Sch-S

locks are also queued behind the waiting shrink operation and will also be blocked, further

exacerbating this concurrency issue. This can significantly impact application query

performance and will also cause difficulties completing the necessary maintenance to shrink

database files. Introduced in SQL Server 2022 (16.x), the shrink wait at low priority feature

addresses this problem by taking a schema modify lock in

mode. For

more information, see

WAIT_AT_LOW_PRIORITY with shrink operations.

For more information on Sch-S and Sch-M locks, see

Transaction locking and row versioning

guide.

For log files, the Database Engine uses

target_size

to calculate the whole log's target size.

Therefore,

target_size

is the log's free space after the shrink operation. The whole log's target

size is then translated to each log file's target size.

tries to shrink each

physical log file to its target size immediately. However, if part of the logical log resides in the

virtual logs beyond the target size, the Database Engine frees as much space as possible, and

then issues an informational message. The message describes what actions are required to

move the logical log out of the virtual logs at the end of the file. After the actions are

performed,

can be used to free the remaining space.

Because a log file can only be shrunk to a virtual log file boundary, shrinking a log file to a size

smaller than the size of a virtual log file might not be possible, even if it isn't being used. The

Database Engine dynamically chooses the virtual file log size when log files are created or

extended.

```sql
DBCC SHRINKDATABASE
```

```sql
DBCC
SHRINKFILE
```

`WAIT_AT_LOW_PRIORITY`

```sql
DBCC SHRINKFILE
```

```sql
DBCC SHRINKFILE
```
