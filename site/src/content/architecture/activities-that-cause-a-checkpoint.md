---
title: "Activities that cause a checkpoint"
topic: "query-processing"
description: "Checkpoints flush dirty data pages from the buffer cache of the current database to disk. This"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Checkpoints flush dirty data pages from the buffer cache of the current database to disk. This

minimizes the active portion of the log that must be processed during a full recovery of a

database. During a full recovery, the following types of actions are performed:

The log records of modifications not flushed to disk before the system stopped are rolled

forward.

All modifications associated with incomplete transactions, such as transactions for which

there's no

or

log record, are rolled back.

A checkpoint performs the following processes in the database:

Writes a record to the log file, marking the start of the checkpoint.

Stores information recorded for the checkpoint in a chain of checkpoint log records.

One piece of information recorded in the checkpoint is the log sequence number (LSN) of

the first log record that must be present for a successful database-wide rollback. This LSN

is called the Minimum Recovery LSN (MinLSN). The MinLSN is the minimum of the:

LSN of the start of the checkpoint.

LSN of the start of the oldest active transaction.

LSN of the start of the oldest replication transaction that hasn't yet been delivered to

the distribution database.

The checkpoint records also contain a list of all the active transactions that have modified

the database.

If the database uses the simple recovery model, marks for reuse the space that precedes

the MinLSN.

Writes all dirty log and data pages to disk.

Writes a record marking the end of the checkpoint to the log file.

Writes the LSN of the start of this chain to the database boot page.

Checkpoints occur in the following situations:

A

statement is explicitly executed. A checkpoint occurs in the current

database for the connection.

## recovery interval

## recovery interval

`COMMIT`

`ROLLBACK`

`CHECKPOINT`
