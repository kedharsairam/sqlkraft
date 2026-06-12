---
title: "Manually fail over (T-SQL)"
topic: "high-availability"
description: "When the mirrored database is synchronized (that is, when the database is in the SYNCHRONIZED state), the database owner can initiate manual failover"
tags: ["high-availability","manually-fail-over-t-sql"]
pubDate: "2025-12-01"
---

When the mirrored database is synchronized (that is, when the database is in the

SYNCHRONIZED state), the database owner can initiate manual failover to the mirror server.

Manual failover can be initiated only from the principal server.

1. Connect to the principal server.

2. Set the database context to the

database:

3. Issue the following statement on the principal server:

ALTER DATABASE

database_name

SET PARTNER FAILOVER, where

database_name

is the

mirrored database.

This initiates an immediate transition of the mirror server to the principal role.

On the former principal, clients are disconnected from the database and in-flight transactions

are rolled back.

ALTER DATABASE Database Mirroring (Transact-SQL)

Manually Fail Over a Database Mirroring Session (SQL Server Management Studio)

Role Switching During a Database Mirroring Session (SQL Server)

７

Note

Transactions that have been prepared by using the Microsoft Distributed Transaction

Coordinator but are still not committed when a failover occurs are considered aborted

after the database has failed over.
