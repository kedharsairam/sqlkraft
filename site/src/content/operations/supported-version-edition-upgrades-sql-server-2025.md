---
title: "Supported version & edition upgrades SQL Server 2025"
topic: "upgrade"
description: |
  Applies to:

  SQL Server

  - Windows only

  This article lists the supported upgrade paths from the following SQL Server versions, and the

  supported edition upgrades for SQL Server 2025 (17.x).

  You can
tags:
  - "upgrade"
  - "supported-version-edition-upgrades-sql-server-2025"
pubDate: 2025-12-01
---

SQL Server

- Windows only

This article lists the supported upgrade paths from the following SQL Server versions, and the

supported edition upgrades for SQL Server 2025 (17.x).

You can upgrade from:

2014 (12.x) SP3 or later

2016 (13.x) SP3 or later

2017 (14.x)

2019 (15.x)

2022 (16.x)

For older versions of SQL Server, you can also

Migrate to SQL Server 2025.

Before you upgrade from one edition of SQL Server 2025 (17.x) to another, verify that the

functionality you're currently using is supported in the edition to which you're moving.

For more information, see

Editions and supported features of SQL Server 2025.

Verify supported hardware and software, including the supported operating system. For

more information, see

Hardware and software requirements for SQL Server 2025.

Before upgrading SQL Server, enable Windows Authentication for SQL Server Agent and

verify the default configuration, that the SQL Server Agent service account is a member of

the SQL Server sysadmin group.

Upgrade is blocked if there's a pending restart.

Upgrade is blocked if the Windows Installer service isn't running.

Cross-version instances of SQL Server 2025 (17.x) aren't supported. Version numbers of

the Database Engine components must be the same in an instance of SQL Server 2025

(17.x).

2025 (17.x) is only available for 64-bit platforms. Cross-platform upgrade isn't

supported. You can't upgrade a 32-bit instance of SQL Server to native 64-bit using SQL
