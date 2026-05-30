---
name: "sys.sp_generate_database_ledger_digest"
title: "sp_generate_database_ledger_digest"
category: "general"
description: "Generates the ledger digest, which is the hash of the last block in If the last block is open (transactions are grouped to the block but no final block hash has been generated), this stored procedure closes the block and generates the hash. Future transactions will then be assigned to the next block. Transact-SQL syntax conventions The results are returned in a column called containing the followi"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sys.database_ledger_blocks"
---

## Description

Generates the ledger digest, which is the hash of the last block in If the last block is open (transactions are grouped to the block but no final block hash has been generated), this stored procedure closes the block and generates the hash. Future transactions will then be assigned to the next block. Transact-SQL syntax conventions The results are returned in a column called containing the following data:

## Syntax

`sys.database_ledger_blocks`
