---
title: "Configure repositories (up to SQL Server 2022)"
topic: "linux-operations"
description: "on Linux This article describes how to configure the correct repository for installing and upgrading SQL Server 2017 (14.x), SQL Server 2019 (15.x), and SQL Server 2022 (16."
tags: ["linux-operations","configure-repositories-up-to-sql-server-2022"]
pubDate: 2025-12-01
---

on Linux

This article describes how to configure the correct repository for installing and upgrading SQL

Server 2017 (14.x), SQL Server 2019 (15.x), and SQL Server 2022 (16.x) on Red Hat Enterprise

Linux (RHEL), SUSE Linux Enterprise Server (SLES), and Ubuntu.

For instructions on how to configure repositories for SQL Server 2022 (16.x) and later versions,

see

Configure repositories for installing and upgrading SQL Server 2025 on Linux.

When you install SQL Server on Linux, you must configure a Microsoft repository. This

repository is used to acquire the database engine package,

, and related SQL

Server packages. There are currently three main repositories:

Description

2022 (16.x) repository.

2019 (15.x) Cumulative Update (CU) repository.

2017 (14.x) Cumulative Update (CU) repository.

The Cumulative Update (CU) repository contains packages for the base SQL Server release, and

any bug fixes or improvements since that release. Cumulative updates are specific to a release

version, such as SQL Server 2022 (16.x). They're released on a regular cadence. General

distribution release (GDR) updates are released in the same CU repository.

Each release contains the full SQL Server package and all previous updates for that repository.

You can also

downgrade

to any release within your major version (for example, 2022).

Use the steps in the following sections to configure repositories on your Linux distribution.

ﾉ

Expand table

```cmd
mssql-server-2022 mssql-server-2019 mssql-server-2017
```
