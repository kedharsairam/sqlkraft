---
name: 'sys.database_ledger_transactions'
title: 'sys.database_ledger_transactions'
category: 'compatibility'
description: 'Captures the cryptographically protected history of database transactions against ledger tables in the database. A row in this view represents a database transaction. For more information on database ledger, see A transaction ID that is unique for the database (it corresponds to a transaction ID in the database transaction log). A sequence number identifying a row. Offset of the transaction in the'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  <version>
  <length>[<key><value>]
---

## Description

Captures the cryptographically protected history of database transactions against ledger tables in the database. A row in this view represents a database transaction. For more information on database ledger, see A transaction ID that is unique for the database (it corresponds to a transaction ID in the database transaction log). A sequence number identifying a row. Offset of the transaction in the block.

## Syntax

```sql
<version>
<length>[<key><value>]
```

## Permissions

SQL) Article • 05/23/2023 Applies to: SQL Server 2022 (16.x) Azure SQL Database Azure SQL Managed Instance Captures the cryptographically protected history of database transactions against ledger tables in the database. A row in this view represents a database transaction. For more information on database ledger, see Ledger . Description A transaction ID that is unique for the database (it corresponds to a transaction ID in the database transaction log). A sequence number identifying a row. Offset of the transaction in the block. The time of the committing transaction. The name of the user who started the transaction. Captured by calling . This is a set of key-values pairs, stored in a binary format. The keys are object IDs (from ) of ledger database tables, modified by the transaction. Each value is a SHA-256 hash of all row versions a transaction created or invalidated. The binary format of data stored in this row is: , where - - indicates the encoding version. Length: 1 byte. - - the number of entries in the key-value pair list. Length: 1 byte. - - an object ID. Length: 4 bytes. - - the hash of rows the transaction cached in the table with the object ID stored as the key. Length: 32 bytes. Requires the permission. ﾉ Expand table sys.database_audit_specification_details sys.database_ledger_transactions sys.database_ledger_blocks sys.ledger_table_history sys.ledger_column_history sys.database_ledger_digest_locations The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Security Center for SQL Server Database Engine and Azure SQL Database Security-Related Dynamic Management Views and Functions (Transact-SQL) See Also
