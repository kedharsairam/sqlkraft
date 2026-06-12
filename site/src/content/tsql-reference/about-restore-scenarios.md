---
name: "About Restore Scenarios"
title: "About Restore Scenarios"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

For descriptions of the arguments, see

RESTORE Arguments.

supports a variety of restore scenarios:

Complete database restore

Restores the entire database, beginning with a full database backup, which may be

followed by restoring a differential database backup (and log backups). For more

information, see

Complete Database Restores - Simple Recovery Model

or

Complete

Database Restores - Full Recovery Model.

File restore

Restores a file or filegroup in a multi-filegroup database. Under the simple recovery

model, the file must belong to a read-only filegroup. After a full file restore, a differential

file backup can be restored. For more information, see

File Restores - Full Recovery Model

and

File Restores - Simple Recovery Model.

Page restore

Restores individual pages. Page restore is available only under the full and bulk-logged

recovery models. For more information, see

Restore Pages - SQL Server.

Piecemeal restore

Restores the database in stages, beginning with the primary filegroup and one or more

secondary filegroups. A piecemeal restore begins with a RESTORE DATABASE using the

PARTIAL option and specifying one or more secondary filegroups to be restored. For

more information, see

Piecemeal Restores - SQL Server.

Recovery only

Recovers data that is already consistent with the database and needs only to be made

available. For more information, see

Recover a Database Without Restoring Data.

Transaction log restore.

#### Discontinued keyword

#### Replaced by.

#### Example of replacement keyword

### deferred transactions

```sql
[
AFTER
'datetime'
]
}
```
