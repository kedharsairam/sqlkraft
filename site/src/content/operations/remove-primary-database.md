---
title: "Remove primary database"
topic: "high-availability"
description: ""
tags: ["high-availability","remove-primary-database"]
pubDate: "2025-12-01"
---

This topic describes how to remove both the primary database and the corresponding

secondary database(s) from an Always On availability group by using SQL Server Management

Studio, Transact-SQL, or PowerShell in SQL Server.

This task is supported only on primary replicas. You must be connected to the server

instance that hosts the primary replica.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica of the

database or databases to be removed, and expand the server tree.

2. Expand the

node and the

node.

3. Select the availability group, and expand the

node.

4. This step depends on whether you want to remove multiple databases groups or only

one database, as follows:

To remove multiple databases, use the

pane to view and

select all the databases that you want to remove. For more information, see

Use the

Object Explorer Details to Monitor Availability Groups (SQL Server Management

Studio).

Prerequisites and Restrictions
