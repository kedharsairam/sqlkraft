---
title: "Join secondary replica"
topic: "high-availability"
description: "08/26/2025 This topic describes how to join a secondary replica to an Always On availability group by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL"
tags: ["high-availability","join-secondary-replica"]
pubDate: 2025-12-01
---

This topic describes how to join a secondary replica to an Always On availability group by using

Management Studio, Transact-SQL, or PowerShell in SQL Server. After a secondary

replica is added to an Always On availability group, the secondary replica must be joined to the

availability group.

The primary replica of the availability group must currently be online.

The instance that you intend on joining to the availability group has already been

added

as a secondary replica.

To use SQL Server Management Studio (SSMS), you must be connected to the server

instance that hosts a primary replica. To use Transact-SQL or PowerShell, you must be

connected to, and execute the commands from, the secondary replica.

The local server instance must be able to connect to the database mirroring endpoint of

the server instance that is hosting the secondary replica.

Requires

permission on the availability group,

permission,

permission, or

permission.

）

Important

If any prerequisite is not met, the join operation fails. After a failed join attempt, you might

need to connect to the server instance that hosts the primary replica to remove and re-

add the secondary replica before you can join it to the availability group. For more

information, see

and.
