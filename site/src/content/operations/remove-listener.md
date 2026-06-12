---
title: "Remove listener"
topic: "high-availability"
description: "This topic describes how to remove an availability group listener from an Always On availability group by using SQL Server Management Studio, Transact"
tags: ["high-availability","remove-listener"]
pubDate: 2025-12-01
---

This topic describes how to remove an availability group listener from an Always On availability

group by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

You must be connected to the server instance that hosts the primary replica.

Before you delete an availability group listener, we recommend that you ensure that no

applications are using it.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and click

the server name to expand the server tree.

2. Expand the

node and the

node.

3. Expand the node of the availability group, and expand the

node.

4. Right-click the listener to be removed, and select the

command.

5. This opens the

dialog box. For more

information, see

Remove Listener from Availability Group

, later in this topic.
