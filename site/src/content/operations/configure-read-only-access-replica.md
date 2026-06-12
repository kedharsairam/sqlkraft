---
title: "Configure read-only access replica"
topic: "high-availability"
description: "By default both read-write and read-intent access are allowed to the primary replica and no connections are allowed to secondary replicas of an Always"
tags: ["high-availability","configure-read-only-access-replica"]
pubDate: "2025-12-01"
---

By default both read-write and read-intent access are allowed to the primary replica and no

connections are allowed to secondary replicas of an Always On availability group. This topic

describes how to configure connection access on an availability replica of an Always On

availability group in SQL Server by using SQL Server Management Studio, Transact-SQL, or

PowerShell.

For information about the implications of enabling read-only access for a secondary replica

and for an introduction to connection access, see

About Client Connection Access to

Availability Replicas (SQL Server)

and

Active Secondaries: Readable Secondary Replicas (Always

On Availability Groups).

To configure different connection access, you must be connected to the server instance

that hosts the primary replica.

To configure replicas

when creating an

availability group

Requires membership in the

fixed server role and either CREATE

AVAILABILITY GROUP server permission, ALTER ANY AVAILABILITY GROUP

permission, or CONTROL SERVER permission.

To modify an availability

replica

Requires ALTER AVAILABILITY GROUP permission on the availability group,

CONTROL AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY

GROUP permission, or CONTROL SERVER permission.

Prerequisites and Restrictions

ﾉ

Expand table
