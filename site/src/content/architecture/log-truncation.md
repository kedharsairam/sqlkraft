---
title: "Log truncation"
topic: "io-fundamentals"
description: "This cycle repeats endlessly, as long as the end of the logical log never reaches the beginning"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

This cycle repeats endlessly, as long as the end of the logical log never reaches the beginning

of the logical log. If the old log records are truncated frequently enough to always leave

sufficient room for all the new log records created through the next checkpoint, the log never

fills. However, if the end of the logical log does reach the start of the logical log, one of two

things occurs:

If the

setting is enabled for the log and space is available on the disk, the file

is extended by the amount specified in the

growth_increment

parameter, and the new log

records are added to the extension. For more information about the

setting,

see

ALTER DATABASE (Transact-SQL) File and Filegroup Options.

If the

setting isn't enabled, or the disk that is holding the log file has less free

space than the amount specified in

growth_increment

, a 9002 error is generated. For more

information, see

Troubleshoot a full transaction log (SQL Server Error 9002).

If the log contains multiple physical log files, the logical log moves through all the physical log

files before it wraps back to the start of the first physical log file.

Log truncation is essential to keep the log from filling. Log truncation deletes inactive virtual

log files from the logical transaction log of a SQL Server database, freeing space in the logical

log for reuse by the physical transaction log. If a transaction log is never truncated, it will

eventually fill all the disk space that is allocated to its physical log files. However, before the log

can be truncated, a checkpoint operation must occur. A checkpoint writes the current in-

memory modified pages (known as

dirty pages

) and transaction log information from memory

to disk. When the checkpoint is performed, the inactive portion of the transaction log is

marked as reusable. Thereafter, a log truncation can free the inactive portion. For more

information about checkpoints, see

Database checkpoints (SQL Server).

The following diagrams show a transaction log before and after truncation. The first diagram

shows a transaction log that has never been truncated. Currently, four virtual log files are in use

by the logical log. The logical log starts at the front of the first virtual log file and ends at virtual

log 4. The MinLSN record is in virtual log 3. Virtual log 1 and virtual log 2 contain only inactive

log records. These records can be truncated. Virtual log 5 is still unused and isn't part of the

current logical log.

）

Important

For more information about transaction log size management, see.

`FILEGROWTH`

`FILEGROWTH`

`FILEGROWTH`
