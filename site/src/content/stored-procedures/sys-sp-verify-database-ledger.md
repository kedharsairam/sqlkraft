---
name: "sys.sp_verify_database_ledger"
title: "sp_verify_database_ledger"
category: "general"
description: "Verifies the database ledger and the table ledgers. For each row in the 1. Recomputes a value stored in the previous_block_hash column of the row. 2. Checks if the recomputed value matches the value currently stored in the 3. If the specified list of digests contains a digest for the ledger block the row represents, it verifies the recomputed value matches the hash in the digest. 4."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.database_ledger"
---

## Description

Verifies the database ledger and the table ledgers. For each row in the 1. Recomputes a value stored in the previous_block_hash column of the row. 2. Checks if the recomputed value matches the value currently stored in the 3. If the specified list of digests contains a digest for the ledger block the row represents, it verifies the recomputed value matches the hash in the digest. 4.

## Syntax

`sys.database_ledger`
