---
title: "Configure bulk import operations"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server 2022 (16.x) and later versions on Linux

  Starting with SQL Server 2022 (16.x) Cumulative Update 24 (CU24) and SQL Server 2025 (17.x)

  Cumulative Update 3 (CU3), you can use the
tags:
  - "linux-operations"
  - "configure-bulk-import-operations"
pubDate: 2025-12-01
---

2022 (16.x) and later versions on Linux

Starting with SQL Server 2022 (16.x) Cumulative Update 24 (CU24) and SQL Server 2025 (17.x)

Cumulative Update 3 (CU3), you can use the

server role or the

permission to perform bulk data import operations on SQL Server running on Linux.

Previously, only members of the

server role could run

BULK INSERT

or

OPENROWSET(BULK.)

on Linux.

on Linux enforces additional file system and path validation checks for bulk

operations, beyond what's required on Windows. An administrator must:

Grant appropriate SQL Server permissions to the user

Grant Linux file system permissions on the data files

Explicitly approve directory paths using

2022 (16.x) CU24 or later version on Linux, or SQL Server 2025 (17.x) CU3 or

later version on Linux

Administrative access to the Linux host

Administrative access to the SQL Server instance

Before you can run bulk import operations, the

service account must have read access to

the data files on the Linux file system.

1. Create a directory for your bulk data files:

）

Important

This feature is currently in preview.

```cmd
ADMINISTER BULK
OPERATIONS mssql-conf mssql mkdir
-p /tmp/bulkload/sales/
```
