---
title: "Backup frequency and business requirements"
topic: "query-processing"
description: "scans the buffer cache for buffers with pages from a specified database and writes all dirty"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

scans the buffer cache for buffers with pages from a specified database and writes all dirty

pages to disk. Checkpoints save time during a later recovery by creating a point at which all

dirty pages are guaranteed to have been written to disk.

Writing a modified data page from the buffer cache to disk is called flushing the page. SQL

Server has logic that prevents a dirty page from being flushed before the associated log record

is written. Log records are written to disk when the log buffers are flushed. This happens

whenever a transaction commits or the log buffers become full.

This section presents concepts about how to back up and restore (apply) transaction logs.

Under the full and bulk-logged recovery models, taking routine backups of transaction logs

(

log backups

) is necessary for recovering data. You can back up the log while any full backup is

running. For more information about recovery models, see

Back up and restore of SQL Server

databases

.

Before you can create the first log backup, you must create a full backup, such as a database

backup or the first in a set of file backups. Restoring a database by using only file backups can

become complex. Therefore, we recommend that you start with a full database backup when

you can. Thereafter, backing up the transaction log regularly is necessary. This not only

minimizes work-loss exposure but also enables truncation of the transaction log. Typically, the

transaction log is truncated after every conventional log backup.

To limit the number of log backups that you need to restore, it's essential to routinely back up

your data. For example, you might schedule a weekly full database backup and daily differential

database backups.

Think about the required

RTO

and

RPO

when implementing your recovery strategy, and

specifically the full and differential database backup cadence.

For more information about transaction log backups, see

Transaction log backups (SQL Server)

.

You should take frequent enough log backups to support your business requirements,

specifically your tolerance for work loss such as might be caused by a damaged log storage.

The appropriate frequency for taking log backups depends on your tolerance for work-loss

exposure balanced by how many log backups you can store, manage, and, potentially, restore.

Think about the required recovery time objective (

RTO

) and recovery point objective (

RPO

)

when implementing your recovery strategy, and specifically the log backup cadence.
