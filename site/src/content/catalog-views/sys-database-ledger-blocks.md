---
name: 'sys.database_ledger_blocks'
title: 'sys.database_ledger_blocks'
category: 'objects'
description: 'SQL Server 2022 (16.x)'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

05/23/2023

Applies to:

SQL Server 2022 (16.x)

Azure SQL Database

Azure SQL Managed

Instance

Captures the cryptographically chained blocks, each of which represents a block of transactions

against ledger tables.

For more information on database ledger, see

Ledger


## Description
A sequence number identifying the row in this view.

The hash of the root of the Merkle tree, formed by transactions

stored in the block.

The number of transactions in the block.

A SHA-256 hash of the previous row in the view.

Requires the

permission.

What is the database ledger?

Ledger Overview

ﾉ

Expand table

See also
