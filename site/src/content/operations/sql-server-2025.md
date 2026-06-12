---
title: "SQL Server 2025"
topic: "linux-operations"
description: "2025 (17.x) on Linux This article describes the major features and services available for SQL Server 2025 (17.x) running on Linux."
tags: ["linux-operations","sql-server-2025"]
pubDate: "2025-12-01"
---

2025 (17.x) on Linux

This article describes the major features and services available for SQL Server 2025 (17.x)

running on Linux. For package downloads and known issues, see the

Release notes.

This section describes updates for each release of SQL Server 2025 (17.x).

Cumulative Update 3

Cumulative Update 1

GA release

The following updates apply to SQL Server 2025 (17.x) Cumulative Update (CU) 3. You can use the

server role or the

permission to perform

and

operations on SQL Server on Linux, without requiring

permissions. An administrator must configure Linux file system permissions and approve

directory paths using.

For more information, see

Configure bulk import operations for SQL Server on Linux

(preview).

The following updates apply to SQL Server 2025 (17.x) Cumulative Update (CU) 1. SQL Server 2025 (17.x) is fully supported on Red

Hat Enterprise Linux (RHEL) 10. For more information, see

Quickstart: Install SQL Server

and create a database on Red Hat. SQL Server 2025 (17.x) is fully supported on Ubuntu 24.04. For

more information, see

Quickstart: Install SQL Server and create a database on Ubuntu.

```cmd
ADMINISTER BULK OPERATIONS
BULK INSERT
OPENROWSET(BULK.) mssql-conf
```
