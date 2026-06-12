---
title: "SQL Server Management Studio"
topic: "high-availability"
description: "This topic describes how to use the pane of SQL Server Management Studio to monitor and manage existing Always On availability groups, availability r"
tags: ["high-availability","sql-server-management-studio"]
pubDate: "2025-12-01"
---

This topic describes how to use the

pane of SQL Server Management

Studio to monitor and manage existing Always On availability groups, availability replicas, and

availability databases.

You must be connected to the instance of SQL Server (server instance) that hosts either the

primary replica or a secondary replica.

1. On the View menu, click

, or press the

key.

2. In Object Explorer, connect to the instance of SQL Server on which you want to monitor

an availability group, and click the server name to expand the server tree.

3. Expand the

node and the

node.

4. The

pane displays every availability group for which the

connected server instance hosts a replica. For each availability group, the

column displays the name of the server instance that is currently hosting the

primary replica. To display more information about a given availability group, select it in

Object Explorer.

5. The

pane then displays the

and

nodes for this availability group:

７

Note

For information about using the Object Explorer Details pane, see.
