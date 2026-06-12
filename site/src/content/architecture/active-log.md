---
title: "Active log"
topic: "transaction-log"
description: ""
tags: ["transaction-log", "architecture"]
pubDate: 2026-05-29
---

The number of log records reaches the number the Database Engine estimates it can

process during the time specified in the recovery interval option.

For information about setting the recovery interval, see

Server configuration: recovery interval

(min).

Automatic checkpoints truncate the unused section of the transaction log if the database is

using the simple recovery model. However, if the database is using the full or bulk-logged

recovery models, the log isn't truncated by automatic checkpoints. For more information, see

The transaction log.

The

statement now provides an optional checkpoint_duration argument that

specifies the requested period of time, in seconds, for checkpoints to finish. For more

information, see

CHECKPOINT.

The section of the log file from the MinLSN to the last-written log record is called the active

portion of the log, or the active log. This is the section of the log required to do a full recovery

of the database. No part of the active log can ever be truncated. All log records must be

truncated from the parts of the log before the MinLSN.

The following diagram shows a simplified version of the end-of-a-transaction log with two

active transactions. Checkpoint records have been compacted to a single record.

LSN 148 is the last record in the transaction log. At the time that the recorded checkpoint at

LSN 147 was processed, Tran 1 had been committed and Tran 2 was the only active transaction.

That makes the first log record for Tran 2 the oldest log record for a transaction active at the

time of the last checkpoint. This makes LSN 142, the Begin transaction record for Tran 2, the

MinLSN.



Tip

The

advanced setup option enables a database administrator to throttle

checkpoint I/O behavior based on the throughput of the I/O subsystem for some types of

checkpoints. The

setup option applies to automatic checkpoints and any otherwise

unthrottled checkpoints.

### recovery interval

`CHECKPOINT`

```sql
-k
```

```sql
-k
```
