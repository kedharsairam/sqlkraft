---
title: "Join a secondary database"
topic: "high-availability"
description: "This topic explains how to join a secondary database to an Always On availability group by using SQL Server Management Studio, Transact-SQL, or PowerS"
tags: ["high-availability","join-a-secondary-database"]
pubDate: 2025-12-01
---

This topic explains how to join a secondary database to an Always On availability group by

using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server. After you

prepare a secondary database for a secondary replica, you need to join the database to the

availability group as soon as possible. This will start data movement from the corresponding

primary database to the secondary database.

You must be connected to the server instance that hosts the secondary replica.

The secondary replica must already be joined to the availability group. For more

information, see

Join a Secondary Replica to an Availability Group (SQL Server).

The secondary database must have been prepared recently. For more information, see

Manually Prepare a Secondary Database for an Availability Group (SQL Server).

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the secondary replica, and

expand the server tree.

７

Note

For information about what happens after a secondary database joins the group, see.
