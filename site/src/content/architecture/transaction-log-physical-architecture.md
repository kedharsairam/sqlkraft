---
title: "Transaction log physical architecture"
topic: "io-fundamentals"
description: "To roll forward the logical operation, the operation is performed again."
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

To roll forward the logical operation, the operation is performed again.

To roll back the logical operation, the reverse logical operation is performed.

Before and after image logged

To roll forward the operation, the after image is applied.

To roll back the operation, the before image is applied.

Many types of operations are recorded in the transaction log. These operations include:

The start and end of each transaction.

Every data modification (insert, update, or delete). Modifications include changes by

system stored procedures or data definition language (DDL) statements to any table,

including system tables.

Every extent and page allocation or deallocation.

Creating or dropping a table or index.

Rollback operations are also logged. Each transaction reserves space in the transaction log to

make sure that enough log space exists to support a rollback that is caused by either an

explicit rollback statement, or if an error is encountered. The amount of space reserved

depends on the operations performed in the transaction, but generally it's equal to the amount

of space used to log each operation. This reserved space is freed when the transaction is

completed.

The section of the log file from the first log record that must be present for a successful

database-wide rollback to the last-written log record is called the active part of the log,

active

log

, or

tail of the log. This is the section of the log required to a full

recovery

of the database.

No part of the active log can ever be truncated. The log sequence number (LSN) of this first log

record is known as the

minimum recovery LSN

(MinLSN). For more information on operations

supported by the transaction log, see

The transaction log.

Differential and log backups advance the restored database to a later time, which corresponds

to a higher LSN.

The database transaction log maps over one or more physical files. Conceptually, the log file is

a string of log records. Physically, the sequence of log records is stored efficiently in the set of

physical files that implement the transaction log. There must be at least one log file for each

database.

### This can slow down database startup, log backup and restore operations, and cause

### transactional replication/CDC and Always On redo latency.

### required size

### autogrow
