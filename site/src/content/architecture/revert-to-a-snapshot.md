---
title: "Revert to a Snapshot"
topic: "collation"
description: ""
tags: ["collation","revert-to-a-snapshot"]
pubDate: "2025-12-01"
---

If data in an online database becomes damaged, in some cases, reverting the database to a

database snapshot that predates the damage might be an appropriate alternative to restoring

the database from a backup. For example, reverting a database might be useful for reverse a

recent serious user error, such as a dropped table. However, all changes made after the

snapshot was created are lost.

Limitations and Restrictions

Security

Transact-SQL

Reverting is unsupported under the following conditions:

There are multiple snapshots for the database. For reverting, there must only be one

snapshot for the database, to which you plan to revert.

Any read-only or compressed filegroups exist in the database.

Any files are now offline but were online when the snapshot was created.

Before reverting a database, consider the following limitations:

Reverting is not intended for media recovery. A database snapshot is an incomplete copy

of the database files, so if either the database or the database snapshot is corrupted,

reverting from a snapshot is likely to be impossible. Furthermore, even when it is possible,

reverting in the event of corruption is unlikely to correct the problem. Therefore, taking

regular backups and testing your restore plan are essential to protect a database. For

more information, see

Back Up and Restore of SQL Server Databases.

７

Note
