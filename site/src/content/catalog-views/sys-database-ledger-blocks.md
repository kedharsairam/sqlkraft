---
name: "sys.database_ledger_blocks"
title: "sys.database_ledger_blocks"
category: "compatibility"
description: "Captures the cryptographically chained blocks, each of which represents a block of transactions For more information on database ledger, see A sequence number identifying the row in this view. The hash of the root of the Merkle tree, formed by transactions The number of transactions in the block. A SHA-256 hash of the previous row in the view."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "sys.database_ledger_blocks"
---

## Description

Captures the cryptographically chained blocks, each of which represents a block of transactions For more information on database ledger, see A sequence number identifying the row in this view. The hash of the root of the Merkle tree, formed by transactions The number of transactions in the block. A SHA-256 hash of the previous row in the view.

## Syntax

`sys.database_ledger_blocks`

## Permissions

Article • 05/23/2023 x) Azure SQL Database Azure SQL Managed Instance Captures the cryptographically chained blocks, each of which represents a block of transactions against ledger tables. For more information on database ledger, see Ledger Description A sequence number identifying the row in this view. The hash of the root of the Merkle tree, formed by transactions stored in the block. The number of transactions in the block. A SHA-256 hash of the previous row in the view. Requires the permission. What is the database ledger? Ledger Overview ﾉ Expand table See also sys.database_audit_specification_details sys.database_ledger_transactions sys.database_ledger_blocks sys.ledger_table_history sys.ledger_column_history sys.database_ledger_digest_locations The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Security Center for SQL Server Database Engine and Azure SQL Database Security-Related Dynamic Management Views and Functions (Transact-SQL) See Also
