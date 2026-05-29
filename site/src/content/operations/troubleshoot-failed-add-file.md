---
title: "Troubleshoot failed add-file"
topic: "high-availability"
description: |
  Applies to:
  
  SQL Server
  
  In some Always On availability group deployments, file paths differ between the system that
  
  hosts the primary replica and systems that host a secondary replica. If the file p
tags:
  - "high-availability"
  - "troubleshoot-failed-add-file"
pubDate: 2025-12-01
---

Applies to:

SQL Server

In some Always On availability group deployments, file paths differ between the system that

hosts the primary replica and systems that host a secondary replica. If the file path of an add-

file operation doesn't exist on a secondary replica, the add-file operation will succeed on the

primary database. But the add-file operation will cause the secondary database to be

suspended. This, in turn, causes the secondary replica to enter the

state.

To resolve this problem the database owner must complete the following steps:

1. Remove the secondary database from the availability group. For more information, see

Remove a Secondary Database from an Availability Group (SQL Server)

.

2. On the existing secondary database, restore a full backup of the filegroup that contains

the added file to the secondary database, using WITH

and

(specifying the file path on the server instance that hosts the secondary replica). For more

information, see

Restore a database to a new location (SQL Server)

.

3. Back up the transaction log that contains the add-file operation on the primary database,

and manually restore the log backup on the secondary database using WITH

and

.

4. Prepare the secondary database for re-joining the availability group, by restoring,

, any other outstanding log backups from the primary database.

5. Rejoin the secondary database to the availability group. For more information, see

Join a

secondary database to an Always On availability group

.

７

Note

If possible, the file path (including the drive letter) of a given secondary database should

be identical to the path of the corresponding primary database.

```cmd
NOT SYNCHRONIZING
NORECOVERY
WITH MOVE
NORECOVERY
WITH MOVE
```