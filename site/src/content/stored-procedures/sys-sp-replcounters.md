---
name: "sys.sp_replcounters"
title: "sp_replcounters"
category: "general"
description: "Returns replication statistics about latency, throughput, and transaction count for each published database. This stored procedure is executed at the Publisher on any database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  Replicated
              transactions
---

## Description

Returns replication statistics about latency, throughput, and transaction count for each published database. This stored procedure is executed at the Publisher on any database.

## Syntax

```sql
Replicated transactions
```

## Permissions

Description LSN of the next commit record awaiting delivery to the distribution database. is used in transactional replication. Requires membership in the fixed database role or fixed server role. sp_replcmds (Transact-SQL) sp_repldone (Transact-SQL) sp_replflush (Transact-SQL) System stored procedures (Transact-SQL)
