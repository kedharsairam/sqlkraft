---
name: "About working with SQL Server backups"
title: "About working with SQL Server backups"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

STANDBY =

standby_file_name

Backs up the tail of the log and leaves the database in a read-only and

state. The

clause writes standby data (performing rollback, but with the option of further

restores). Using the

option is equivalent to

followed

by a.

Using standby mode requires a standby file, specified by

standby_file_name

, whose

location is stored in the log of the database. If the specified file already exists, the

Database Engine overwrites it; if the file doesn't exist, the Database Engine creates it. The

standby file becomes part of the database.

This file holds the rolled back changes, which must be reversed if

operations

are to be subsequently applied. There must be enough disk space for the standby file to

grow so that it can contain all the distinct pages from the database that were modified by

rolling back uncommitted transactions.

Specifies that the transaction log shouldn't be not truncated and causes the Database Engine

to attempt the backup regardless of the state of the database. Thus, a backup taken with

might have incomplete metadata. This option allows backing up the transaction

log in situations where the database is damaged.

The

option of

is equivalent to specifying both

and.

Without the

option, the database must be in the

state. If the database is in

the SUSPENDED state, you might be able to create a backup by specifying. But if

the database is in the

or

state,

isn't allowed even with.

For information about database states, see

Database states.

This section introduces the following essential backup concepts:

Backup Types

Transaction Log Truncation

Formatting Backup Media

Working with Backup

Devices and Media Sets

Restoring SQL Server Backups

７

Note

#### Scope of

#### backup

#### Backup types

### Backup overview (SQL Server)

## Backup types

The supported backup types depend on the recovery model of the database, as follows

All recovery models support full and differential backups of data.

Whole

database

Database backups

cover the whole database.

Optionally, each database backup can serve as the base of a series of one or more

differential database backups.

Partial

database

Partial backups

cover read/-write filegroups and, possibly, one or more read-only

files or filegroups.

Optionally, each partial backup can serve as the base of a series of one or more

differential partial backups.

File or

filegroup

File backups

cover one or more files or filegroups, and are relevant only for

databases that contain multiple filegroups. Under the simple recovery model, file

backups are essentially restricted to read-only secondary filegroups.

Optionally, each file backup can serve as the base of a series of one or more

differential file backups.

Under the full recovery model or bulk-logged recovery model, conventional backups also

include sequential

transaction log backups

(or

log backups

), which are required. Each log

backup covers the portion of the transaction log that was active when the backup was

created, and it includes all log records not backed up in a previous log backup.

To minimize work-loss exposure, at the cost of administrative overhead, you should

schedule frequent log backups. Scheduling differential backups between full backups can

reduce restore time by reducing the number of log backups you have to restore after

restoring the data.

We recommend that you put log backups on a separate volume than the database

backups.

For an introduction to backup in SQL Server, see.

Expand table

７

Note

## Transaction log truncation

### View or change the recovery model of a database (SQL Server)

## Format backup media

## Work with backup devices and media sets

## Backup devices in a striped media set (a stripe set)

A

copy-only backup

is a special-purpose full backup or log backup that is independent of

the normal sequence of conventional backups. To create a copy-only backup, specify the

option in your

statement. For more information, see

Copy-only

backups.

To avoid filling up the transaction log of a database, routine backups are essential. Under the

simple recovery model, log truncation occurs automatically after you back up the database,

and under the full recovery model, after you back up the transaction log. However, sometimes

the truncation process can be delayed. For information about factors that can delay log

truncation, see

The transaction log.

Backup media is formatted by a

statement if and only if any of the following is true:

The

option is specified.

The media is empty.

The operation is writing a continuation tape.

A

stripe set

is a set of disk files on which data is divided into blocks and distributed in a fixed

order. The number of backup devices used in a stripe set must stay the same (unless the media

is reinitialized with

).

Before you can create the first log backup, you must create a full backup.

７

Note

The

and

options have been discontinued. If

you're using the full or bulk-logged recovery model recovery and you must remove the

log backup chain from a database, switch to the simple recovery model. For more

information, see.

## Work with a mirrored media set

The following example writes a backup of the

database to a new striped

media set that uses three disk files.

After a backup device is defined as part of a stripe set, it can't be used for a single-device

backup unless FORMAT is specified. Similarly, a backup device that contains nonstriped

backups can't be used in a stripe set unless FORMAT is specified. To split a striped backup set,

use FORMAT.

If both

or

aren't specified when a media header is written, the

media header field corresponding to the blank item is empty.

Typically, backups are unmirrored, and

statements simply include a

clause. However,

a total of four mirrors is possible per media set. For a mirrored media set, the backup operation

writes to multiple groups of backup devices. Each group of backup devices comprises a single

mirror within the mirrored media set. Every mirror must use the same quantity and type of

physical backup devices, which must all have the same properties.

To back up to a mirrored media set, all of the mirrors must be present. To back up to a

mirrored media set, specify the

clause to specify the first mirror, and specify a

clause for each additional mirror.

For a mirrored media set, each

clause must list the same number and type of

devices as the

clause. The following example writes to a mirrored media set that contains

two mirrors and uses three devices per mirror:

#### Mirror

#### Media family 1

#### Media family 2

#### Media family 3

## Restore SQL Server backups

Each backup device specified in the

clause of a

statement corresponds to a media

family. For example, if the

clause lists three devices,

writes data to three media

families. In a mirrored media set, every mirror must contain a copy of every media family. This

is why the number of devices must be identical in every mirror.

When multiple devices are listed for each mirror, the order of the devices determines which

media family is written to a particular device. For example, in each of the device lists, the

second device corresponds to the second media family. For the devices in the previous

example, the correspondence between devices and media families is shown in the following

table.

0

1

A media family must always be backed up onto the same device within a specific mirror.

Therefore, each time you use an existing media set, list the devices of each mirror in the same

order as they were specified when the media set was created.

For more information about mirrored media sets, see

Mirrored Backup Media Sets (SQL Server).

For more information about media sets and media families in general, see

Media sets, media

families, and backup sets (SQL Server).

）

Important

This example is designed to allow you to test it on your local system. In practice, backing

up to multiple devices on the same drive would hurt performance and would eliminate the

redundancy for which mirrored media sets are designed.

Media families in mirrored media sets

Expand table

### Restore

#### Skip

#### option

`STANDBY`

`STANDBY`

`STANDBY`

```sql
BACKUP LOG WITH NORECOVERY
```

```sql
RESTORE WITH STANDBY
```

```sql
RESTORE LOG
```

`NO_TRUNCATE`

`NO_TRUNCATE`

```sql
BACKUP LOG
```

`COPY_ONLY`

`CONTINUE_AFTER_ERROR`

`NO_TRUNCATE`

`ONLINE`

`NO_TRUNCATE`

`OFFLINE`

`EMERGENCY`

`BACKUP`

`NO_TRUNCATE`

`COPY_ONLY`

`BACKUP`

`BACKUP`

`FORMAT`

`FORMAT`

```sql
BACKUP LOG WITH NO_LOG
```

```sql
WITH TRUNCATE_ONLY
```

`AdventureWorks2025`

`MEDIANAME`

`MEDIADESCRIPTION`

`BACKUP`

`TO`

`TO`

```sql
MIRROR TO
```

```sql
MIRROR TO
```

`TO`

```sql
BACKUP
DATABASE
AdventureWorks2022
TO
DISK =
'X:\SQLServerBackups\AdventureWorks1.bak'
,
DISK =
'Y:\SQLServerBackups\AdventureWorks2.bak'
,
DISK =
'Z:\SQLServerBackups\AdventureWorks3.bak'
WITH
FORMAT
,
MEDIANAME =
'AdventureWorksStripedSet0'
,
MEDIADESCRIPTION =
'Striped media set for AdventureWorks2022 database'
;
GO
```

```sql
BACKUP
DATABASE
AdventureWorks2022
TO
DISK =
'X:\SQLServerBackups\AdventureWorks1a.bak'
,
DISK =
'Y:\SQLServerBackups\AdventureWorks2a.bak'
,
DISK =
'Z:\SQLServerBackups\AdventureWorks3a.bak'
MIRROR
TO
DISK =
'X:\SQLServerBackups\AdventureWorks1b.bak'
,
```

`TO`

`BACKUP`

`TO`

`BACKUP`

```sql
Z:\AdventureWorks1a.bak
Z:\AdventureWorks2a.bak
Z:\AdventureWorks3a.bak
```

```sql
Z:\AdventureWorks1b.bak
Z:\AdventureWorks2b.bak
Z:\AdventureWorks3b.bak
```

```sql
DISK =
'Y:\SQLServerBackups\AdventureWorks2b.bak'
,
DISK =
'Z:\SQLServerBackups\AdventureWorks3b.bak'
;
GO
```
