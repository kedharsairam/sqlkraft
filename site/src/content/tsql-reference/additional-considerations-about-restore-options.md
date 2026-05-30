---
name: "Additional Considerations About RESTORE Options"
title: "Additional Considerations About RESTORE Options"
category: "statements"
description: "Under the full or bulk-logged recovery model, restoring log backups is required to reach"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Discontinued RESTORE Keywords

Under the full or bulk-logged recovery model, restoring log backups is required to reach

the desired recovery point. For more information about restoring log backups, see

Apply

Transaction Log Backups - SQL Server

.

Prepare an availability database for an Always On availability group

For more information, see

Manually Prepare a Secondary Database for an Availability

Group - SQL Server

.

Prepare a mirror database for database mirroring

For more information, see

Prepare a Mirror Database for Mirroring - SQL Server

.

Online Restore

Where online restore is supported, if the database is online, file restores and page restores are

automatically online restores and, also, restores of secondary filegroup after the initial stage of

a piecemeal restore.

For more information, see

Online Restore

.

The following keywords were discontinued in SQL Server 2008 (10.0.x):

LOAD

RESTORE

TRANSACTION

LOG

７

Note

Online restore is allowed only in Enterprise edition of SQL Server.

７

Note

Online restores can involve

.



Expand table

#### Discontinued keyword

#### Replaced by...

#### Example of replacement keyword

## RESTORE LOG

### Tail-Log Backups

## Comparison of RECOVERY and NORECOVERY

```sql
RESTORE DATABASE
```

```sql
RESTORE LOG
```
