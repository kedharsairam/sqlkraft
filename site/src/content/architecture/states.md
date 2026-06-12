---
title: "States"
topic: "collation"
description: "A database is always in one specif"
tags: ["collation","states"]
pubDate: "2025-12-01"
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

A database is always in one specific state. For example, these states include

,

, or. To verify the current state of a database, select the

column in the

sys.databases

catalog view or the

property in the

DATABASEPROPERTYEX

function.

The following table defines the database states.

Database is available for access. The primary filegroup is online, although the undo phase

of recovery might not have been completed.

Database is unavailable. A database becomes offline by explicit user action and remains

offline until further user action is taken. For example, the database might be taken offline

in order to move a file to a new disk. The database is then brought back online after the

move has been completed.

One or more files of the primary filegroup are being restored, or one or more secondary

files are being restored offline. The database is unavailable.

Database is being recovered. The recovering process is a transient state; the database

automatically becomes online if the recovery succeeds. If the recovery fails, the database

becomes suspect. The database is unavailable.

has encountered a resource-related error during recovery. The database isn't

damaged, but files might be missing or system resource limitations might be preventing it

from starting. The database is unavailable. Further action by the user is required to resolve

the error and let the recovery process be completed.

At least the primary filegroup is suspect and might be damaged. The database can't be

recovered during startup of SQL Server. The database is unavailable. Further action by the

user is required to resolve the problem.

User has changed the database and sets the status to. The database is in single-

user mode and might be repaired or restored. The database is marked

, logging

is disabled, and access is limited to members of the

fixed server role.

is primarily used for troubleshooting purposes. For example, a database marked as suspect

can be set to the

state. This could permit the system administrator read-only

ﾉ

Expand table

```sql
ONLINE
OFFLINE
SUSPECT state_desc
ONLINE
OFFLINE
RESTORING
RECOVERING
RECOVERY
PENDING
SUSPECT
EMERGENCY
EMERGENCY
READ_ONLY
EMERGENCY
EMERGENCY
```
