---
title: "When to use bound sessions"
topic: "io-fundamentals"
description: "Only one session in a set of bound sessions can be active at any time. If one session is executing"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Only one session in a set of bound sessions can be active at any time. If one session is executing

a statement on the instance or has results pending from the instance, no other session bound to

the same token can access the instance until the current session finishes processing or cancels

the current statement. If the instance is busy processing a statement from another of the bound

sessions, an error occurs indicating that the transaction space is in use and the session should

retry later.

When you bind sessions, each session retains its isolation level setting. Using

to change the isolation level setting of one session doesn't affect the setting of

any other session bound to the same token.

The two types of bound sessions are local and distributed.

Allows bound sessions to share the transaction space of a single

transaction in a single instance of the Database Engine.

Allows bound sessions to share the same transaction across two

or more instances until the entire transaction is either committed or rolled back by using

Microsoft Distributed Transaction Coordinator (MS DTC).

Distributed bound sessions aren't identified by a character string bind token; they're identified by

distributed transaction identification numbers. If a bound session is involved in a local transaction

and executes an RPC on a remote server with

, the local bound

transaction is automatically promoted to a distributed bound transaction by MS DTC and an MS

DTC session is started.

In earlier versions of SQL Server, bound sessions were primarily used in developing extended

stored procedures that must execute Transact-SQL statements on behalf of the process that calls

them. Having the calling process pass in a bind token as one parameter of the extended stored

procedure allows the procedure to join the transaction space of the calling process, thereby

integrating the extended stored procedure with the calling process.

In the Database Engine, stored procedures written using CLR are more secure, scalable, and

stable than extended stored procedures. CLR-stored procedures use the

object to

join the context of the calling session, not

.

```sql
SET TRANSACTION
ISOLATION LEVEL
```

```sql
SET REMOTE_PROC_TRANSACTIONS ON
```

`SqlContext`

`sp_bindsession`
