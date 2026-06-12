---
title: "Checkpoint process"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Just before a page is written, the form of page protection specified in the database is added to

the page.

If torn page protection is added, the page must be latched exclusively (EX) for the I/O.

This is because the torn page protection modifies the page, making it unsuitable for any

other thread to read.

If checksum page protection is added, or the database uses no page protection, the page

is latched with an update (UP) latch for the I/O. This latch prevents anyone else from

modifying the page during the write, but still allows readers to use it.

For more information about disk I/O page protection options, see

Buffer management.

A dirty page is written to disk in one of three ways:

Lazy writing

Eager writing

Checkpoint

The lazy writing, eager writing, and checkpoint processes don't wait for the I/O operation to

complete. They always use asynchronous (or overlapped) I/O and continue with other work,

checking for I/O success later. This allows SQL Server to maximize both CPU and I/O resources

for the appropriate tasks.

The lazy writer is a system process that keeps free buffers available by removing infrequently

used pages from the buffer cache. Dirty pages are first written to disk.

The eager write process writes dirty data pages associated with minimally logged operations

such as bulk insert and select into. This process allows creating and writing new pages to take

place in parallel. That is, the calling operation doesn't have to wait until the entire operation

finishes before writing the pages to disk.

The checkpoint process periodically scans the buffer cache for buffers with pages from a

specified database and writes all dirty pages to disk. Checkpoints save time during a later

recovery by creating a point at which all dirty pages are guaranteed to have been written to

disk.

The user might request a checkpoint operation by using the

command, or the

Database Engine might generate automatic checkpoints based on the amount of log space

used and time elapsed since the last checkpoint. In addition, a checkpoint is generated when

certain activities occur. For example, when a data or log file is added or removed from a

database, or when the instance of SQL Server is stopped.

For more information, see

Checkpoints and the active portion of the log.

Pages and extents architecture guide

Read data pages in the Database Engine
