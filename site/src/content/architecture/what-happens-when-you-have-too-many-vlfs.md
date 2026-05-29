---
title: "What happens when you have too many VLFs?"
topic: "query-processing"
description: "is the initial size for the log"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The

size

value, set by the

argument of

is the initial size for the log

file.

The

growth_increment

value (also known as the autogrow value), which the

argument of

sets, is the amount of space added to the file every time

new space is required.

For more information on

and

## arguments of

, see

ALTER

DATABASE (Transact-SQL) File and Filegroup Options

.

During the initial stages of a database recovery process, SQL Server discovers all VLFs in all

transaction log files, and builds a list of these VLFs. This process can take a long time

depending on the number of VLFs present in the specific database. The more VLFs, the longer

the process. A database can end up with large number of VLFs if frequent transaction log

autogrowth or manual growth is encountered in small increments. When the number of VLFs

reaches the range of several hundred thousand, you can encounter some or most of the

following symptoms:

One or more databases take a very long time to finish recovery during SQL Server startup.

Restoring a database takes a very long time to complete.

Attempts to attach a database take a very long time to complete.

When you try to set up database mirroring, you encounter error messages 1413, 1443,

and 1479, indicating a timeout.

You encounter memory-related errors like 701 when you attempt to restore a database.

Transactional replication or change data capture might experience significant latency.

When you examine the SQL Server Error log, you might notice that a significant amount of time

is spent before the

analysis

phase of the database recovery process. For example:

Output



Tip

To determine the optimal VLF distribution for the current transaction log size of all

databases in a given instance, and the required growth increments to achieve the required

size, see this

on GitHub.

```sql
SIZE
```

```sql
ALTER DATABASE
```

```sql
FILEGROWTH
```

```sql
ALTER DATABASE
```

```sql
FILEGROWTH
```

```sql
SIZE
```

```sql
ALTER DATABASE
```

```sql
2022-05-08 14:42:38.65 spid22s Starting up database 'lot_of_vlfs'.
2022-05-08 14:46:04.76 spid22s Analysis of database 'lot_of_vlfs' (16) is 0%
complete (approximately 0 seconds remain). Phase 1 of 3. This is an informational
message only. No user action is required.
```
