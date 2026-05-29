---
name: 'sys.database_ledger_transactions'
title: 'sys.database_ledger_transactions (Transact-'
category: 'objects'
description: 'SQL Server 2022 (16.x)'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL)

Article

•

05/23/2023

Applies to:

SQL Server 2022 (16.x)

Azure SQL Database

Azure SQL Managed

Instance

Captures the cryptographically protected history of database transactions against ledger tables

in the database. A row in this view represents a database transaction.

For more information on database ledger, see

Ledger

.


## Description
A transaction ID that is unique for the database (it corresponds

to a transaction ID in the database transaction log).

A sequence number identifying a row.

Offset of the transaction in the block.

The time of the committing transaction.

The name of the user who started the transaction. Captured by

calling

.

This is a set of key-values pairs, stored in a binary format. The

keys are object IDs (from

) of ledger database tables,

modified by the transaction. Each value is a SHA-256 hash of all

row versions a transaction created or invalidated.

The binary format of data stored in this row is:

, where

-

- indicates the encoding version. Length: 1 byte.

-

- the number of entries in the key-value pair list.

Length: 1 byte.

-

- an object ID. Length: 4 bytes.

-

- the hash of rows the transaction cached in the table

with the object ID stored as the key. Length: 32 bytes.

Requires the

permission.

ﾉ

Expand table

What is the database ledger?

Ledger overview

See also

```sql
ORIGINAL_LOGIN()
```

```sql
<version>
<length>[<key><value>]
```

```sql
version
```

```sql
length
```

```sql
key
```

```sql
value
```
