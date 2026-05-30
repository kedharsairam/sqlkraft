---
name: "Additional considerations about BACKUP options"
title: "Additional considerations about BACKUP options"
category: "statements"
description: "To restore a database and, optionally, recover it to bring it online, or to restore a file or"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Interaction of SKIP, NOSKIP, INIT, and NOINIT

To restore a database and, optionally, recover it to bring it online, or to restore a file or

filegroup, use either the Transact-SQL

RESTORE

statement or the SQL Server Management

Studio

tasks. For more information, see

Restore and recovery overview (SQL Server)

.

This table describes interactions between the {

|

} and {

|

} options.

If the volume contains a valid media header,

verifies that the media name matches the given

, if any. If it matches, appends the

backup set, preserving all existing backup sets.

If the volume doesn't contain a valid media

header, an error occurs.

If the volume contains a valid media

header, performs the following checks:

If

was specified, verifies

that the given media name matches

the media header's media name.

Verifies that there are no unexpired

backup sets already on the media. If

there are, terminates the backup.

If these checks pass, overwrites any

backup sets on the media, preserving only

the media header.

If the volume doesn't contain a valid

media header, generates one with using

specified

and

, if any.

If the volume contains a valid media header,

appends the backup set, preserving all existing

backup sets.

If the volume contains a valid media

header, overwrites any backup sets on the

media, preserving only the media header.

If the media is empty, generates a media

７

Note

If the tape media is empty or the disk backup file doesn't exist, all these interactions write

a media header and proceed. If the media isn't empty and lacks a valid media header,

these operations give feedback stating that this isn't valid MTF media, and they terminate

the backup operation.



Expand table

1

2

#### Skip

#### option

### larger than 65536 (64 KB)

```sql
NOINIT
```

```sql
INIT
```

```sql
NOSKIP
```

```sql
SKIP
```

```sql
NOINIT
INIT
NOSKIP
```

```sql
MEDIANAME
```

```sql
MEDIANAME
```

```sql
MEDIANAME
```

```sql
MEDIADESCRIPTION
```

```sql
SKIP
```
