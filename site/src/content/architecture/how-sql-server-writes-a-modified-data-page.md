---
title: "How SQL Server writes a modified data page"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

The I/O from an instance of the Database Engine includes logical and physical writes. A logical

write occurs when data is modified in a page in the buffer cache. A physical write occurs when

the page is written from the

buffer cache

to disk.

When a page is modified in the buffer cache, it isn't immediately written back to disk; instead,

the page is marked as dirty. This means that a page can have more than one logical write made

before it's physically written to disk. For each logical write, a transaction log record is inserted

in the log cache that records the modification. The log records must be written to disk before

the associated dirty page is removed from the buffer cache and written to disk.

uses a technique known as write-ahead logging (WAL) that prevents writing a dirty

page before the associated log record is written to disk. This is essential to the correct working

of the recovery manager. For more information, see

Write-ahead transaction log.

The following illustration shows the process for writing a modified data page.

When the buffer manager writes a page, it searches for adjacent dirty pages that can be

included in a single gather-write operation. Adjacent pages have consecutive page IDs and are

from the same file; the pages don't have to be contiguous in memory. The search continues

both forward and backward until one of the following events occurs:

A clean page is found.

32 pages have been found.

A dirty page is found whose log sequence number (LSN) hasn't yet been flushed in the

log.

A page is found that can't be immediately latched.

In this way, the entire set of pages can be written to disk with a single gather-write operation.
