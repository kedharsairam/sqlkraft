---
title: "Transaction Lifetimes"
topic: "clr-integration"
description: |
  Article

  •

  12/30/2024

  Applies to:

  SQL Server

  There's an important difference between transactions started in Transact-SQL stored

  procedures, and transactions started in managed code: common langu
tags:
  - "clr-integration"
  - "transaction-lifetimes"
pubDate: 2025-12-01
---

Article

•

12/30/2024

SQL Server

There's an important difference between transactions started in Transact-SQL stored

procedures, and transactions started in managed code: common language runtime (CLR) code

can't unbalance the transaction state on entry or exit of a CLR invocation. Be aware of the

following implications of this difference:

A transaction started inside a CLR frame must be committed or rolled back, or else SQL

Server generates an error when the frame is exited.

An outer transaction can't be committed or rolled back inside the CLR code.

An attempt to commit a transaction not started in the same procedure causes a run-time

error.

An attempt to roll back a transaction not started in the same procedure causes the

transaction to stop responding (preventing any other side-effecting operation from

happening). The transaction discontinues until the CLR code goes out of scope. This

behavior can be useful when you detect an error inside your procedure and want to make

sure the whole transaction terminates.

CLR integration and transactions
