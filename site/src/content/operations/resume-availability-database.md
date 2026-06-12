---
title: "Resume availability database"
topic: "high-availability"
description: "You can resume a suspended availability database in Always On availability groups by using SQL Server Management Studio, Transact-SQL, or PowerShell i"
tags: ["high-availability","resume-availability-database"]
pubDate: 2025-12-01
---

You can resume a suspended availability database in Always On availability groups by using

Management Studio, Transact-SQL, or PowerShell in SQL Server. Resuming a

suspended database puts the database into the SYNCHRONIZING state. Resuming the primary

database also resumes any of its secondary databases that were suspended as the result of

suspending the primary database. If any secondary database was suspended locally, from the

server instance that hosts the secondary replica, that secondary database must be resumed

locally. Once a given secondary database and the corresponding primary database are in the

SYNCHRONIZING state, data synchronization resumes on the secondary database.

A RESUME command returns as soon as it has been accepted by the replica that hosts the

target database, but actually resuming the database occurs asynchronously.

You must be connected to the server instance that hosts the database to be resumed.

The availability group must be online.

The primary database must be online and available.

７

Note

Suspending and resuming an Always On secondary database does not directly affect the

availability of the primary database. However, suspending a secondary database can

impact redundancy and failover capabilities for the primary database, until the suspended

secondary database is resumed. This is in contrast to database mirroring, where the

mirroring state is suspended on both the mirror database and the principal database until

mirroring is resumed. Suspending an Always On primary database suspends data

movement on all the corresponding secondary databases, and redundancy and failover

capabilities cease for that database until the primary database is resumed.
