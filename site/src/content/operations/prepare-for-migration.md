---
title: "Prepare for migration"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  This article helps you prepare your environment for a

  SQL Server VM migration

  of your SQL

  Server instance enabled by Azure Arc to

  SQL Server on Azure VMs

  in the Azure por
tags:
  - "azure-synapse"
  - "prepare-for-migration"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article helps you prepare your environment for a

SQL Server VM migration

of your SQL

Server instance enabled by Azure Arc to

SQL Server on Azure VMs

in the Azure portal.

To migrate your SQL Server databases to SQL Server on Azure VMs through the Azure portal,

you need the following prerequisites:

An active Azure subscription. If you don't have one,

create a free account

.

An instance of SQL Server

enabled by Azure Arc

with the

latest version

of the Azure

extension for SQL Server. To upgrade your extension, see

Upgrade the extension

.

You can choose to use an existing SQL Server on Azure VM, or you can provision a target

SQL Server VM during the migration process. If you choose to use an existing SQL Server

VM, it must be

registered with the SQL IaaS Agent extension

.

SQL Server VM migration works with every edition of SQL Server on Windows and Linux.

The following table lists the minimum supported SQL Server versions for migration:

７

Note

Migrating to SQL Server on Azure VMs through the Azure portal is currently in

.

You can provide feedback about your migration experience

.

ﾉ

Expand table
