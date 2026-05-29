---
name: "sys.dm_tran_active_transactions"
title: "sys.dm_tran_active_transactions"
category: "io"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric dynamic management view returns information about transactions for the instance. ID of the transaction at the instance level, not the database level. It is only unique across all databases within an instance but not unique across all server Transaction name. This is overwritten if the transaction is marked and the marked name replace"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_tran_active_transactions"
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric dynamic management view returns information about transactions for the instance. ID of the transaction at the instance level, not the database level. It is only unique across all databases within an instance but not unique across all server Transaction name. This is overwritten if the transaction is marked and the marked name replaces the transaction

## Syntax

```sql
sys.dm_tran_active_transactions
```
