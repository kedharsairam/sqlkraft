---
title: "Configure backup on replicas"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to configure backup on secondary replicas for an Always On
  
  availability group by using SQL Server Management Studio, Transact
tags:
  - "high-availability"
  - "configure-backup-on-replicas"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to configure backup on secondary replicas for an Always On

availability group by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL

Server.

You must be connected to the server instance that hosts the primary replica in SSMS. The

secondary replica must be healthy, which includes being connected to the current primary

replica and in the secondary role.

To configure backup on

secondary replicas when

creating an availability group

Requires membership in the

fixed server role and either

CREATE AVAILABILITY GROUP server permission, ALTER ANY

AVAILABILITY GROUP permission, or CONTROL SERVER permission.

To modify an availability group

or availability replica

Requires ALTER AVAILABILITY GROUP permission on the availability

group, CONTROL AVAILABILITY GROUP permission, ALTER ANY

AVAILABILITY GROUP permission, or CONTROL SERVER permission.

７

Note

For an introduction to backup on secondary replicas, see

.

７

Note

The secondary replica does not need to be readable to offload backups to it. Backups will

still succeed on the secondary replica even if

is set to

, with the

exception of

.

ﾉ

Expand table

```cmd
Readable Secondary
no
```