---
title: "Change transaction safety"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Transaction safety is the attribute that controls the operating mode of the session. At any time,

  however, the database owner can change the transacti
tags:
  - "high-availability"
  - "change-transaction-safety"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

Transaction safety is the attribute that controls the operating mode of the session. At any time,

however, the database owner can change the transaction safety. By default, the level of

transaction safety is set to FULL (synchronous operating mode).

Turning off transaction safety shifts the session into asynchronous operating mode, which

maximizes performance. If the principal becomes unavailable, the mirror stops but is available

as a warm standby (failover requires forcing service with possible data loss).

1. Connect to the principal server.

2. Issue the following Transact-SQL statement:

where

<database>

is the name of the mirrored database.

1. Connect to the principal server.

2. Issue the following statement:

where

<database>

is the mirrored database.

ALTER DATABASE Database Mirroring (Transact-SQL)

Database Mirroring Operating Modes

```cmd
ALTER DATABASE <database> SET PARTNER SAFETY FULL
ALTER DATABASE <database> SET PARTNER SAFETY OFF
```
