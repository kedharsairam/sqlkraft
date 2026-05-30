---
name: "Resolve errors in database emergency mode"
title: "Resolve errors in database emergency mode"
category: "predicates"
description: "detects a corruption error. When the"
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

A stack dump (

,

,

) is created in the

SQL Server

directory whenever

detects a corruption error. When the

Feature

Usage

data collection and

Error Reporting

features are enabled for the instance of SQL Server,

the file is automatically forwarded to Microsoft. The collected data is used to improve SQL

Server functionality. The dump file contains the results of the

command and

additional diagnostic output. Access is limited to the SQL Server service account and members

of the sysadmin role. By default, the sysadmin role contains all members of the Windows

group and the local administrator's group. The DBCC command

doesn't fail if the data collection process fails.

If any errors are reported by

, we recommend restoring the database from the

database backup, instead of running

with one of the

options. If no

backup exists, running repair corrects the errors reported. The repair option to use is specified

at the end of the list of reported errors. However, correcting the errors by using the

option might require deleting some pages, and therefore some data.

Under some circumstances, values might be entered into the database that aren't valid or out-

of-range based on the data type of the column.

can detect column values that

aren't valid for all column data types. Therefore, running

with the

option on databases that have been upgraded from earlier versions of SQL Server might reveal

preexisting column-value errors. Because SQL Server can't automatically repair these errors, the

column value must be manually updated. If

detects such an error,

## returns a

warning, the error number 2570, and information to identify the affected row and manually

correct the error.

The repair can be performed under a user transaction to let the user roll back the changes that

were made. If repairs are rolled back, the database still contains errors and must be restored

from a backup. After repairs are completed, back up the database.

When a database has been set to emergency mode by using the

ALTER DATABASE

statement,

can perform some special repairs on the database if the

option is specified. These repairs might allow for ordinarily unrecoverable databases to be

brought back online in a physically consistent state. These repairs should be used as a last

resort and only when you can't restore the database from a backup. When the database is set

to emergency mode, the database is marked READ_ONLY, logging is disabled, and access is

limited to members of the

fixed server role.

### Data loss warning with REPAIR_ALLOW_DATA_LOSS

## Data loss warning with REPAIR_ALLOW_DATA_LOSS

When the database is in emergency mode and

with the

clause is run, the following actions are taken:

uses pages that have been marked inaccessible because of I/O or checksum

errors, as if the errors haven't occurred. Doing this increases the chances for data recovery

from the database.

attempts to recover the database using regular log-based recovery

techniques.

If database recovery is unsuccessful because of transaction log corruption, the transaction

log is rebuilt. Rebuilding the transaction log might result in the loss of transactional

consistency.

If the

command succeeds, the database is in a physically consistent state, and the

database status is set to ONLINE. However, the database might contain one or more

transactional inconsistencies. We recommend that you run

DBCC CHECKCONSTRAINTS

to

identify any business logic flaws and immediately back up the database.

If the

command fails, the database can't be repaired.

The

option is a supported feature of SQL Server. However, it might not

always be the best option for bringing a database to a physically consistent state. If successful,

the

option can result in some data loss.

In fact, it can result in more data lost than if a user were to restore the database from the last

known good backup. Microsoft always recommends a user restore from the last known good

backup as the primary method to recover from errors reported by

.

７

Note

You can't run the

command in emergency mode inside a user transaction

and roll back the transaction after execution.

２

Warning

The

option can result in more data loss than if you restore from a

last known good backup. See

### not

### last resort

### not

```sql
SQLDump<nnnn>.txt
```

```sql
SQLDump<nnnn>.log
```

```sql
SQLDump<nnnn>.mdmp
```

```sql
LOG
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
BUILTIN\Administrators
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
REPAIR_*
```

```sql
REPAIR_ALLOW_DATA_LOSS
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DATA_PURITY
```

```sql
CHECKDB
```

```sql
CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
REPAIR_ALLOW_DATA_LOSS
```

```sql
DBCC CHECKDB
```

```sql
REPAIR_ALLOW_DATA_LOSS
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
REPAIR_ALLOW_DATA_LOSS
```

```sql
REPAIR_ALLOW_DATA_LOSS
```

```sql
DBCC CHECKDB
```

```sql
DBCC CHECKDB
```

```sql
REPAIR_ALLOW_DATA_LOSS
```
