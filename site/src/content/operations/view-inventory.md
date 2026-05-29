---
title: "View inventory"
topic: "azure-synapse"
description: |
  Applies to:
  
  SQL Server
  
  When SQL Server engine instances or associated services are enabled by Azure Arc, you can
  
  use Azure to manage your inventory.
  
  Verify that the SQL Server service is
  
  Version 
tags:
  - "azure-synapse"
  - "view-inventory"
pubDate: 2025-12-01
---

Applies to:

SQL Server

When SQL Server engine instances or associated services are enabled by Azure Arc, you can

use Azure to manage your inventory.

Verify that the SQL Server service is

Version SQL Server 2014 (12.x) or later.

On a physical or virtual machine that's running the Windows operating system.

Connected to Azure Arc. See

Connect your SQL Server to Azure Arc

.

Connected to the internet directly or through a proxy server.

To inventory SQL Server databases, make sure that database names adhere to naming

conventions and don't contain reserved words. For a list of reserved words, see

Resolve errors

for reserved resource names

. For a complete list of naming rules and restrictions, review

naming rules and restrictions

.

To inventory databases:

1. Locate the instance of SQL Server enabled by Azure Arc in the Azure portal.

2. Select the SQL Server resource.

3. Under

, select

.

4. Use the

SQL Server databases - Azure Arc

area to view the databases that belong to the

instance.

To view the database size and space available, make sure that the built-in SQL Server login

is a member of the SQL Server

server role for all the SQL Server

instances running on the machine.

To view properties for a specific database, select the database in the portal.

```cmd
NT
AUTHORITY\SYSTEM
```