---
name: "Revert a database to a database snapshot"
title: "Revert a database to a database snapshot"
category: "hints"
description: "Restoring over a database using the full or bulk-logged recovery model where a tail-log"
tags: ["tsql","hints"]
pubDate: 2026-05-29
---

## Restrictions on reverting

Restoring over a database using the full or bulk-logged recovery model where a tail-log

backup has not been taken and the

option is not used.

With the REPLACE option, you can lose committed work, because the log written most

recently has not been backed up.

Overwriting existing files.

For example, a mistake could allow overwriting files of the wrong type, such as.xls files, or

that are being used by another database that is not online. Arbitrary data loss is possible

if existing files are overwritten, although the restored database is complete.

Undoing the effects of a restore is not possible; however, you can negate the effects of the

data copy and rollforward by starting over on a per-file basis. To start over, restore the desired

file and perform the rollforward again. For example, if you accidentally restored too many log

backups and overshot your intended stopping point, you would have to restart the sequence.

A restore sequence can be aborted and restarted by restoring the entire contents of the

affected files.

A

revert database operation

(specified using the DATABASE_SNAPSHOT option) takes a full

source database back in time by reverting it to the time of a database snapshot, that is,

overwriting the source database with data from the point in time maintained in the specified

database snapshot. Only the snapshot to which you are reverting can currently exist. The revert

operation then rebuilds the log (therefore, you cannot later roll forward a reverted database to

the point of user error).

Data loss is confined to updates to the database since the snapshot's creation. The metadata of

a reverted database is the same as the metadata at the time of snapshot creation. However,

reverting to a snapshot drops all the full-text catalogs.

Reverting from a database snapshot is not intended for media recovery. Unlike a regular

backup set, the database snapshot is an incomplete copy of the database files. If either the

database or the database snapshot is corrupted, reverting from a snapshot is likely to be

impossible. Furthermore, even when possible, reverting in the event of corruption is unlikely to

correct the problem.

`STOPAT`
