---
name: "Progress reporting for DBCC commands"
title: "Progress reporting for DBCC commands"
category: "statements"
description: "Sometimes an internal database snapshot isn't required or can't be created. When this occurs,"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Sometimes an internal database snapshot isn't required or can't be created. When this occurs,

the DBCC command executes against the actual database. If the database is online, the DBCC

command uses table-locking to ensure the consistency of the objects that it is checking. This

behavior is the same as if the

option were specified.

An internal database snapshot isn't created when a DBCC command is executed:

Against the

database, and the instance of SQL Server is running in single-user

mode.

Against a database other than

, but the database has been put in single-user

mode by using the

statement.

Against a read-only database.

Against a database that has been set in emergency mode by using the

statement.

Against. In this case, a database snapshot can't be created because of internal

restrictions.

Using the

option. In this case, DBCC honors the request by not creating a

database snapshot.

The DBCC commands use table locks instead of the internal database snapshots when the

command is executed against the following:

A read-only filegroup

A FAT file system

A volume that doesn't support

named streams

A volume that doesn't support

alternate streams

７

Note

Trying to run

, or the equivalent part of

, by using the

option requires a database exclusive (

) lock. This database lock cannot be set on

or

and will probably fail on all other databases.

７

Note

fails when it is run against

if an internal database snapshot cannot

be created.

#### Execution

#### phase

#### Progress reporting

#### granularity

The

catalog view contains information about the progress and the

current phase of execution of the

,

, and

commands.

The

column indicates the percentage complete of the command, and the

column reports the current phase of the execution of the command.

The definition of a unit of progress depends on the current phase of execution of the DBCC

command. Sometimes progress is reported at the granularity of a database page, in other

phases it is reported at the granularity of a single database or allocation repair. The following

table describes each phase of execution, and the granularity at which the command reports

progress.

## Description

database is checked during this phase.

database page level.

The progress reporting

are checked.

,

repaired.

individual repair level.

completed.

Allocation structures in the database are checked during

this phase.

Note:

performs the same checks.

Progress isn't reported

,

repaired.

Progress isn't reported.

Database system tables are checked during this phase.

database page level.

The progress reporting

#### Execution

#### Progress reporting

#### granularity

```sql
WITH TABLOCK
```

`master`

`master`

```sql
ALTER DATABASE
```

```sql
ALTER DATABASE
```

`tempdb`

```sql
WITH TABLOCK
```

```sql
DBCC CHECKALLOC
```

```sql
DBCC CHECKDB
```

```sql
WITH
TABLOCK
```

```sql
X
```

`tempdb`

`master`

```sql
DBCC CHECKDB
```

`master`

`sys.dm_exec_requests`

```sql
DBCC CHECKDB
```

`CHECKFILEGROUP`

`CHECKTABLE`

`percent_complete`

`command`

```sql
DBCC TABLE
CHECK
```

```sql
DBCC TABLE
REPAIR
```

`REPAIR_FAST`

`REPAIR_REBUILD`

`REPAIR_ALLOW_DATA_LOSS`

```sql
DBCC ALLOC
CHECK
```

```sql
DBCC CHECKALLOC
```

```sql
DBCC ALLOC
REPAIR
```

`REPAIR_FAST`

`REPAIR_REBUILD`

`REPAIR_ALLOW_DATA_LOSS`

```sql
DBCC SYS
CHECK
```
