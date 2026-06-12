---
title: "Agent roles"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  This article lists the server and database roles and mappings that the installation of Azure

  extension for SQL Server creates.

  When you install Azure extension for SQL Serve
tags:
  - "azure-synapse"
  - "agent-roles"
pubDate: 2025-12-01
---

SQL Server

This article lists the server and database roles and mappings that the installation of Azure

extension for SQL Server creates.

When you install Azure extension for SQL Server, the installation:

1. Creates a server level role: SQLArcExtensionServerRole

2. Creates a database level role: SQLArcExtensionUserRole

3. Adds NT AUTHORITY\SYSTEM

account to each role

4. Maps NT AUTHORITY\SYSTEM

at the database level for each database

5. Grants minimum permissions for the enabled features

Alternatively, you can configure SQL Server enabled by Azure Arc to run in least privilege

mode (available in preview). For details, review

Operate SQL Server enabled by Azure Arc

with least privilege (preview).

In addition, Azure extension for SQL Server revokes permissions for these roles when they're no

longer needed for specific features.

is a Windows task. It grants or revokes privileges in SQL

Server when it detects:

A new SQL Server instance is installed on the host

instance is uninstalled from host

An instance level feature is enabled or disabled or settings are updated

Extension service is restarted

-

-

-

７

Note

```cmd
SqlServerExtensionPermissionProvider
```
