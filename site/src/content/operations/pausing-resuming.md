---
title: "Pausing & resuming"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  The database owner can pause and later resume a database mirroring session at any time.

  Pausing preserves the session state while suspending mirroring
tags:
  - "high-availability"
  - "pausing-resuming"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

The database owner can pause and later resume a database mirroring session at any time.

Pausing preserves the session state while suspending mirroring. During bottlenecks, pausing

might be useful to improve performance on the principal server.

When a session is paused, the principal database remains available. Pausing sets the state of

the mirroring session to SUSPENDED, and the mirror database no longer keeps up with the

principal database, causing the principal database to run exposed.

We recommend that you resume a paused session quickly, because as long as a database

mirroring session remains paused, the transaction log cannot be truncated. Therefore, if a

database mirroring session is paused for too long, the transaction log fills up, making the

database unavailable. For an explanation of why this happens, see "How Pausing and Resuming

Affect Log Truncation," later in this topic.

How Pausing and Resuming Affect Log Truncation

Avoid a Full Transaction Log

Normally, when an automatic checkpoint is performed on a database, its transaction log is

truncated to that checkpoint after the next log backup. While a database mirroring session

remains paused, all of the current log records remain active because the principal server is

waiting to send them to the mirror server. The unsent log records accumulate in the

）

Important

Following a forced service, when the original principal server reconnects mirroring is

suspended. Resuming mirroring in this situation could possibly cause data loss on the

original principal server. For information about managing the potential data loss, see.
