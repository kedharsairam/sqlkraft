---
title: 'Circular nature of the transaction log'
topic: 'io-fundamentals'
description: 'Each VLF contains one or more'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Each VLF contains one or more

log blocks

. Each log block consists of the log records (aligned at

a 4-byte boundary). A log block is variable in size and is always an integer multiple of 512 bytes

(the minimum sector size SQL Server supports), with a maximum size of 60 KB. A log block is

the basic unit of I/O for transaction logging.

In summary, a log block is a container of log records that's used as the basic unit of transaction

logging when writing log records to disk.

Each log block within a VLF is uniquely addressed by its

block offset

. The first block always has a

block offset that points past the first 8 KB in the VLF.

In general, a VLF is always filled up with log blocks. It's possible that the last log block in a VLF

is empty (for example, doesn't contain any log records). This happens when a log record to be

written doesn't fit into the current log block and also when the space left on the VLF is

insufficient to hold this log record. In this case, an empty log block is created that fills up the

VLF. The log record is inserted into the first block on the next VLF.

The transaction log is a wrap-around file. For example, consider a database with one physical

log file divided into four VLFs. When the database is created, the logical log file begins at the

start of the physical log file. New log records are added at the end of the logical log and

expand toward the end of the physical log. Log truncation frees any virtual logs whose records

all appear in front of the minimum recovery log sequence number (MinLSN). The

MinLSN

is the

log sequence number of the oldest log record that is required for a successful database-wide

rollback. The transaction log in the example database would look similar to the one in the

following diagram.

When the end of the logical log reaches the end of the physical log file, the new log records

wrap around to the start of the physical log file.

### Manage the size of the

### transaction log file
