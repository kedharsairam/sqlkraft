---
title: "Transaction log logical architecture"
topic: "io-fundamentals"
description: "SQL Server transaction log architecture and"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

SQL Server transaction log architecture and

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Every SQL Server database has a transaction log that records all transactions and the database

modifications that are made by each transaction. The transaction log is a critical component of

the database and, if there's a system failure, the transaction log might be required to bring

your database back to a consistent state. This guide provides information about the physical

and logical architecture of the transaction log. Understanding the architecture can improve

your effectiveness in managing transaction logs.

The SQL Server transaction log operates logically as if the transaction log is a string of log

records. Each log record is identified by a

log sequence number

(LSN). Each new log record is

written to the logical end of the log with an LSN that is higher than the LSN of the record

before it. Log records are stored in a serial sequence as they're created, such that if LSN2 is

greater than LSN1, the change described by the log record referred to by LSN2 occurred after

the change described by the log record LSN1. Each log record contains the ID of the

transaction that it belongs to. For each transaction, all log records associated with the

transaction are individually linked in a chain using backward pointers that speed the rollback of

the transaction.

The basic structure of an LSN is

. For more information,

see the

VLF

and

log block

sections.

Here's an example of an LSN:

, where

is the ID of the VLF,

is the log block ID, and

is the first log record in that log block. For examples of LSNs, look

at the output of

sys.dm_db_log_info

DMV and examine the

column.

Log records for data modifications record either the logical operation performed, or they

record the before and after images of the modified data. The

before image

is a copy of the data

before the operation is performed; the

after image

is a copy of the data after the operation has

been performed.

The steps to recover an operation depend on the type of log record:

Logical operation logged

```sql
[VLF ID:Log Block ID:Log Record ID]
```

```sql
00000031:00000da0:0001
```

```sql
0x31
```

```sql
0xda0
```

```sql
0x1
```

```sql
vlf_create_lsn
```
