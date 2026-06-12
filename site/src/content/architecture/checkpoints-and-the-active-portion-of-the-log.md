---
title: "Checkpoints and the active portion of the log"
topic: "io-fundamentals"
description: "Taking a log backup every 15 to 30 minutes might be enough."
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Taking a log backup every 15 to 30 minutes might be enough. If your business requires that

you minimize work-loss exposure, consider taking log backups more frequently. More frequent

log backups have the added advantage of increasing the frequency of log truncation, resulting

in smaller log files.

A continuous sequence of log backups is called a

log chain. A log chain starts with a full backup

of the database. Usually, a new log chain is only started when the database is backed up for the

first time, or after the recovery model is switched from simple recovery to full or bulk-logged

recovery. Unless you choose to overwrite existing backup sets when creating a full database

backup, the existing log chain remains intact. With the log chain intact, you can restore your

database from any full database backup in the media set, followed by all subsequent log

backups up through your recovery point. The recovery point could be the end of the last log

backup or a specific recovery point in any of the log backups. For more information, see

Transaction log backups (SQL Server).

To restore a database up to the point of failure, the log chain must be intact. That is, an

unbroken sequence of transaction log backups must extend up to the point of failure. Where

this sequence of log must start depends on the type of data backups you're restoring:

database, partial, or file. For a database or partial backup, the sequence of log backups must

extend from the end of a database or partial backup. For a set of file backups, the sequence of

log backups must extend from the start of a full set of file backups. For more information, see

Apply Transaction Log Backups (SQL Server).

Restoring a log backup rolls forward the changes that were recorded in the transaction log to

recreate the exact state of the database at the time the log backup operation started. When

you restore a database, you'll have to restore the log backups that were created after the full

database backup that you restore, or from the start of the first file backup that you restore.

Typically, after you restore the most recent data or differential backup, you must restore a

series of log backups until you reach your recovery point. Then, you recover the database. This

rolls back all transactions that were incomplete when the recovery started and brings the

database online. After the database has been recovered, you can't restore any more backups.

For more information, see

Apply Transaction Log Backups (SQL Server).
