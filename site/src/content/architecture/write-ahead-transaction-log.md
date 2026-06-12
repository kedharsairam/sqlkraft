---
title: "Write-ahead transaction log"
topic: "io-fundamentals"
description: "The second diagram shows how the log appears after being truncated. Virtual log 1 and virtual"
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

The second diagram shows how the log appears after being truncated. Virtual log 1 and virtual

log 2 have been freed for reuse. The logical log now starts at the beginning of virtual log 3.

Virtual log 5 is still unused, and it isn't part of the current logical log.

Log truncation occurs automatically after the following events, except when delayed for some

reason:

Under the simple recovery model, after a checkpoint.

Under the full recovery model or bulk-logged recovery model, after a log backup, if a

checkpoint has occurred since the previous backup.

Log truncation can be delayed by various factors. In the event of a long delay in log truncation,

the transaction log can fill up. For information, see

Factors that can delay log truncation

and

Troubleshoot a full transaction log (SQL Server Error 9002).

This section describes the role of the write-ahead transaction log in recording data

modifications to disk. SQL Server uses a write-ahead logging (WAL) algorithm, which

guarantees that no data modifications are written to disk before the associated log record is

written to disk. This maintains the ACID properties for a transaction.

For more information about WAL, see

I/O fundamentals.

To understand how write-ahead logging works in relation to the transaction log, it's important

for you to know how modified data is written to disk. SQL Server maintains a buffer cache (also

called a buffer pool) into which it reads data pages when data must be retrieved. When a page

is modified in the buffer cache, it isn't immediately written back to disk; instead, the page is

marked as

dirty. A data page can have more than one logical write made before it's physically

written to disk. For each logical write, a transaction log record is inserted in the log cache that

records the modification. The log records must be written to disk before the associated dirty

page is removed from the buffer cache and written to disk. The checkpoint process periodically
