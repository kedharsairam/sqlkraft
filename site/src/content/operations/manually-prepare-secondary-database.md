---
title: "Manually prepare secondary database"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to prepare a database for an Always On availability group in SQL
  
  Server by using SQL Server Management Studio, Transact-SQL, 
tags:
  - "high-availability"
  - "manually-prepare-secondary-database"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to prepare a database for an Always On availability group in SQL

Server by using SQL Server Management Studio, Transact-SQL, or PowerShell. Preparing a

database requires two steps:

1. Restore a recent database backup of the primary database and subsequent log backups

onto each server instance that hosts the secondary replica, using RESTORE WITH

NORECOVERY

2. Join the restored database to the availability group.

Make sure that the system where you plan to place database possesses a disk drive with

sufficient space for the secondary databases.

The name of the secondary database must be the same as the name of the primary

database.

Use RESTORE WITH NORECOVERY for every restore operation.

If the secondary database needs to reside on a different file path (including the drive

letter) than the primary database, the restore command must also use the WITH MOVE

option for each of the database files to specify them to the path of the secondary

database.

If you restore the database filegroup by filegroup, be sure to restore the whole database.



Tip

If you have an existing log shipping configuration, you might be able to convert the log

shipping primary database along with one or more of its secondary databases to an

availability group primary replica and one or more secondary replicas. For more

information, see

Prerequisites for migrating from log Shipping to Always On Availability

.

Prerequisites and restrictions