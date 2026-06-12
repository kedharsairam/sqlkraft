---
title: "View health with policies"
topic: "high-availability"
description: "This topic describes how to determine the operational health of an Always On availability group by using an Always On policy in SQL Server Management"
tags: ["high-availability","view-health-with-policies"]
pubDate: 2025-12-01
---

This topic describes how to determine the operational health of an Always On availability

group by using an Always On policy in SQL Server Management Studio or PowerShell in SQL

Server. For information about Always On Policy Based Management, see

Always On Policies for

Operational Issues with Always On Availability Groups (SQL Server).

Requires CONNECT, VIEW SERVER STATE, and VIEW ANY DEFINITION permissions.

1. In Object Explorer, connect to the server instance that hosts one of the availability

replicas. To view information about all of the availability replicas in an availability group,

use to the server instance that hosts the primary replica.

2. Click the server name to expand the server tree.

3. Expand the

node.

Either right-click the

node or expand this node and right-click a

specific availability group.

4. Select the

command.

For information about how to use the Always On Dashboard, see

Use the Always On

Dashboard (SQL Server Management Studio).

）

Important

For Always On policies, the category names are used as IDs. Changing the name of an

Always On category would break its health-evaluation functionality. Therefore, the names

of Always On category should never be modified.
