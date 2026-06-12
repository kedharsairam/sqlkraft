---
name: "How DBCC SHRINKDATABASE works"
title: "How DBCC SHRINKDATABASE works"
category: "statements"
description: "size explicitly set by using a file size changing operation."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

size explicitly set by using a file size changing operation. Operations like

or

are examples of file-size changing operations.

Consider a database is originally created with a size of 10 MB in size. Then, it grows to 100 MB.

The smallest the database can be reduced to is 10 MB, even if all the data in the database has

been deleted.

Specify either the

option or the

option when you run. If you don't, the result is the same as if you run a

operation with

followed by running a

operation with.

The shrunk database doesn't have to be in single user mode. Other users can be working in the

database when it's shrunk, including system databases.

You can't shrink a database while the database is being backed up. Conversely, you can't back

up a database while a shrink operation on the database is in process.

When specified with WAIT_AT_LOW_PRIORITY, the shrink operation's Sch-M lock request waits

with low priority when executing the command for one minute. If the operation is blocked for

the duration, the specified ABORT_AFTER_WAIT action will be executed.

In Azure Synapse SQL pools, running a shrink command is not recommended as this is an I/O

intensive operation and can take your dedicated SQL pool (formerly SQL DW) offline. In

addition, there will be costing implications to your data warehouse snapshots after running this

command.

SQL Server, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse

Analytics dedicated SQL pool

Currently, columns using LOB data types (

,

, and

) in compressed columnstore segments are not affected by

and.

shrinks data files on a per-file basis, but shrinks log files as if all the log

files existed in one contiguous log pool. Files are always shrunk from the end.

## Understand concurrency issues with DBCC SHRINKDATABASE

Assume you have a couple of log files, a data file, and a database named. The data and

log files are 10 MB each and the data file contains 6 MB of data. The Database Engine

calculates a target size for each file. This value is the size to which the file is to be shrunk. When

is specified with

target_percent

, the Database Engine calculates target size

to be the

target_percent

amount of space free in the file after shrinking.

For example, if you specify a

target_percent

of 25 for shrinking

, the Database Engine

calculates the target size for the data file to be 8 MB (6 MB of data plus 2 MB of free space). As

such, the Database Engine moves any data from the data file's last 2 MB to any free space in

the data file's first 8 MB and then shrinks the file.

Assume the data file of

contains 7 MB of data. Specifying a

target_percent

of 30 allows for

this data file to be shrunk to the free percentage of 30. However, specifying a

target_percent

of

40 doesn't shrink the data file because not enough free space can be created in the current

total size of the data file.

You can think of this issue another way: 40 percent wanted free space + 70 percent full data file

(7 MB out of 10 MB) is more than 100 percent. Any

target_percent

greater than 30 won't shrink

the data file. It won't shrink because the percentage free you want plus the current percentage

that the data file occupies is over 100 percent.

For log files, the Database Engine uses

target_percent

to calculate the target size for the whole

log. That's why

target_percent

is the amount of free space in the log after the shrink operation.

Target size for the whole log is then translated to a target size for each log file.

tries to shrink each physical log file to its target size immediately. Let's

say no part of the logical log stays in the virtual logs beyond the target size of the log file. Then

the file is successfully truncated and

finishes without any messages.

However, if part of the logical log stays in the virtual logs beyond the target size, the Database

Engine frees as much space as possible, and then issues an informational message. The

message describes what actions are required to move the logical log out of the virtual logs at

the end of the file. After the actions are run,

can be used to free the

remaining space.

A log file can only be shrunk to a virtual log file boundary. That's why shrinking a log file to a

size smaller than the size of a virtual log file might not be possible. It might not be possible

even if it isn't being used. The size of the virtual log file is chosen dynamically by the Database

Engine when log files are created or extended.

```sql
DBCC SHRINKFILE
```

```sql
ALTER DATABASE
```

`NOTRUNCATE`

`TRUNCATEONLY`

```sql
DBCC
SHRINKDATABASE
```

```sql
DBCC SHRINKDATABASE
```

`NOTRUNCATE`

```sql
DBCC SHRINKDATABASE
```

`TRUNCATEONLY`

```sql
DBCC
SHRINKDATABASE
```

```sql
DBCC SHRINKFILE
```

```sql
DBCC SHRINKDATABASE
```

`mydb`

```sql
DBCC SHRINKDATABASE
```

`mydb`

`mydb`

```sql
DBCC SHRINKDATABASE
```

```sql
DBCC SHRINKDATABASE
```

```sql
DBCC SHRINKDATABASE
```
