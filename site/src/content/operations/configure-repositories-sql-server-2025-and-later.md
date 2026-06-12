---
title: "Configure repositories (SQL Server 2025 and later)"
topic: "linux-operations"
description: "on Linux This article describes how to configure the correct repository for installing and upgrading SQL Server 2025 (17.x) on Red Hat Enterprise Linux (RHEL) and Ubuntu. F"
tags: ["linux-operations","configure-repositories-sql-server-2025-and-later"]
pubDate: 2025-12-01
---

on Linux

This article describes how to configure the correct repository for installing and upgrading SQL

Server 2025 (17.x) on Red Hat Enterprise Linux (RHEL) and Ubuntu.

For instructions on how to configure repositories for SQL Server 2022 (16.x) and earlier

versions, see

Configure Repositories for Installing and Upgrading SQL Server on Linux.

When you install SQL Server on Linux, you must configure a Microsoft repository. Use this

repository to get the database engine package,

, and related SQL Server

packages. The following repositories are currently available:

Description

2025 (17.x) repository.

2022 (16.x) repository.

2019 (15.x) Cumulative Update (CU) repository.

2017 (14.x) Cumulative Update (CU) repository.

The Cumulative Update (CU) repository contains packages for the base SQL Server release, and

any bug fixes or improvements since that release. Cumulative updates are specific to a release

version, such as SQL Server 2025 (17.x). They're released on a regular cadence. General

distribution release (GDR) updates are released in the same CU repository.

Each release contains the full SQL Server package and all previous updates for that repository.

You can also

downgrade

to any release within your major version (for example, 2025).



Tip

RHEL 10 and Ubuntu 24.04 are supported starting with SQL Server 2025 (17.x) CU 1. For

more information, see the.

ﾉ

Expand table

```cmd
mssql-server mssql-server-2025 mssql-server-2022 mssql-server-2019 mssql-server-2017
```
