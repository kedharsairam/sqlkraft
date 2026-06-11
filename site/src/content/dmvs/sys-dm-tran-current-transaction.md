---
name: "sys.dm_tran_current_transaction"
title: "sys.dm_tran_current_transaction"
category: "io"
description: "Analytics Platform System (PDW) Returns a single row that displays the state information of the transaction in the current Transaction ID of the current snapshot. Sequence number of the transaction that generates the Snapshot isolation state. This value is 1 if the transaction is started under snapshot isolation. Otherwise, the value is 0."
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_tran_current_transaction"
---

## Description

Analytics Platform System (PDW) Returns a single row that displays the state information of the transaction in the current Transaction ID of the current snapshot. Sequence number of the transaction that generates the Snapshot isolation state. This value is 1 if the transaction is started under snapshot isolation. Otherwise, the value is 0. Lowest transaction sequence number of the transactions that

## Syntax

`sys.dm_tran_current_transaction`
