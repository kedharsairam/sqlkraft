---
title: "How-to"
topic: "high-availability"
description: |
  Article

  •

  02/05/2024

  Applies to:

  SQL Server

  Managing an existing Always On availability group in SQL Server involves one or more of the

  following tasks:

  Altering the properties of an existing a
tags:
  - "high-availability"
  - "how-to"
pubDate: 2025-12-01
---

Article

•

02/05/2024

SQL Server

Managing an existing Always On availability group in SQL Server involves one or more of the

following tasks:

Altering the properties of an existing availability replica, for example to change client

connection access (for configuring readable secondary replicas), changing its failover

mode, availability mode, or session timeout setting.

Adding or removing secondary replicas.

Adding or removing a database.

Suspending or resuming a database.

Performing a planned manual failover (a

manual failover

) or a forced manual failover (a

forced failover

).

Creating or configuring an availability group listener.

Managing

readable secondary replicas

for a given availability group. This involves

configuring one or more replicas to read-only access when running under the secondary

role, and configuring read-only routing.

Managing

backups on secondary replicas

for a given availability group. This involves

configuring where you prefer that backup jobs run and then scripting backup jobs to

implement your backup preference. you need to script backup jobs for every database in

the availability group on every instance of SQL Server that hosts an availability replica.

Deleting an availability group.

Cross-cluster migration of Always On Availability Groups for OS upgrade

Add a Secondary Replica to an Availability Group (SQL Server)

Remove a Secondary Replica from an Availability Group (SQL Server)

Add a Database to an Availability Group (SQL Server)

Remove a Secondary Database from an Availability Group (SQL Server)

Remove a Primary Database from an Availability Group (SQL Server)

Configure the Flexible Failover Policy to Control Conditions for Automatic Failover (Always

On Availability Groups)
