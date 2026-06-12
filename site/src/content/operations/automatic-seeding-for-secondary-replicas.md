---
title: "Automatic seeding for secondary replicas"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  In SQL Server 2012 and 2014, the only way to initialize a secondary replica in a SQL Server

  Always On availability group is to use backup, copy, and r
tags:
  - "high-availability"
  - "automatic-seeding-for-secondary-replicas"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

In SQL Server 2012 and 2014, the only way to initialize a secondary replica in a SQL Server

Always On availability group is to use backup, copy, and restore. SQL Server 2016 introduces a

new feature to initialize a secondary replica -

automatic seeding. Automatic seeding uses the

log stream transport to stream the backup using VDI to the secondary replica for each

database of the availability group using the configured endpoints. This new feature can be

used either during the initial creation of an availability group or when a database is added to

one. Automatic seeding is in all editions of SQL Server that support Always On availability

groups, and can be used with both traditional availability groups and

distributed availability

groups.

Security permissions vary depending on the type of replica being initialized:

For a traditional availability group, permissions must be granted to the availability group

on the secondary replica as it is joined to the availability group. In Transact-SQL, use the

command.

For a distributed availability group where the replica's databases that are being created

are on the primary replica of the second availability group, no extra permissions are

required as it is already a primary. However, if there's only one replica on the second

availability group, then grant the

permission to the secondary

availability group name, or automatic seeding may fail.

For a secondary replica on the second availability group of a distributed availability

group, you must use the command. This secondary replica is seeded from the primary of the second

availability group.

```cmd
ALTER AVAILABILITY GROUP [<AGName>] GRANT CREATE ANY DATABASE
CREATE ANY DATABASE
ALTER AVAILABILITY GROUP [<2ndAGName>] GRANT
CREATE ANY DATABASE
```
