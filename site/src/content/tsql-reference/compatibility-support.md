---
name: "Compatibility support"
title: "Compatibility support"
category: "statements"
description: "RESTORE LOG can include a file list to allow for creation of files during rollforward."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

DBO_ONLY

RESTRICTED_USER

RESTORE LOG can include a file list to allow for creation of files during rollforward. This is used

when the log backup contains log records written when a file was added to the database.

Rollback is controlled by the RESTORE statement through the [ RECOVERY | NORECOVERY ]

options:

NORECOVERY specifies that rollback doesn't occur. This allows rollforward to continue

with the next statement in the sequence.

In this case, the restore sequence can restore other backups and roll them forward.

RECOVERY (the default) indicates that rollback should be performed after rollforward is

completed for the current backup. No further backups can be restored. Select this option

once you have restored all of the necessary backups.

Recovering the database requires that the entire set of data being restored (the

rollforward set

) is consistent with the database. If the rollforward set has not been rolled

forward far enough to be consistent with the database and RECOVERY is specified, the

Database Engine issues an error. For more information about the recovery process, see

Restore and Recovery Overview (SQL Server)

.

７

Note

For a database using the full or bulk-logged recovery model, in most cases you must back

up the tail of the log before restoring the database. Restoring a database without first

backing up the tail of the log results in an error, unless the RESTORE DATABASE statement

contains either the WITH REPLACE or the WITH STOPAT clause, which must specify a time

or transaction that occurred after the end of the data backup. For more information about

tail-log backups, see

.

### upgrade_option

### upgrade_option

### upgrade_option

### upgrade_option

### OPEN MASTER KEY

### ALTER MASTER KEY REGENERATE

```sql
RESTORE DATABASE ... WITH RESTRICTED_USER
```
