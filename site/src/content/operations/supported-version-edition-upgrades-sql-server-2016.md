---
title: "Supported version & edition upgrades SQL Server 2016"
topic: "upgrade"
description: |
  06/03/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  You can upgrade from SQL Server 2008 (10.0.x), SQL Server 2008 R2 (10.50.x), SQL Server 2012
  
  (11.x), and SQL Server 2014 (12.x). This article list
tags:
  - "upgrade"
  - "supported-version-edition-upgrades-sql-server-2016"
pubDate: 2025-12-01
---

06/03/2025

Applies to:

SQL Server

- Windows only

You can upgrade from SQL Server 2008 (10.0.x), SQL Server 2008 R2 (10.50.x), SQL Server 2012

(11.x), and SQL Server 2014 (12.x). This article lists the supported upgrade paths from these

SQL Server versions, and the supported edition upgrades for SQL Server 2016 (13.x).

Before upgrading from one edition of SQL Server 2016 (13.x) to another, verify that the

functionality you're currently using is supported in the edition to which you're moving.

Before upgrading SQL Server, enable Windows Authentication for SQL Server Agent and

verify the default configuration that the SQL Server Agent service account is a member of

the SQL Server sysadmin group.

To upgrade to SQL Server 2016 (13.x), you must be running a supported operating

system. For more information, see

Hardware and software requirements for SQL Server

2016 and SQL Server 2017

.

Upgrade is blocked if there's a pending restart.

Upgrade is blocked if the Windows Installer service isn't running.

Cross-version instances of SQL Server 2016 (13.x) aren't supported. Version numbers of

the Database Engine, Analysis Services, and Reporting Services components must be the

same in an instance of SQL Server 2016 (13.x).

SQL Server 2016 (13.x) is only available for 64-bit platforms. Cross-platform upgrade isn't

supported. You can't upgrade a 32-bit instance of SQL Server to native 64-bit using SQL

Server Setup. However, you can back up or detach databases from a 32-bit instance of

SQL Server, and restore or attach them to a 64-bit instance of SQL Server if the databases

aren't published in replication. You must recreate any logins and other user objects in

,

, and

system databases.

```cmd
master
msdb
model
```