---
title: "View listener properties"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  This topic describes how to view the properties of an Always On
  
  availability group listener
  
  by
  
  using SQL Server Management Studio or Transact-SQL in
tags:
  - "high-availability"
  - "view-listener-properties"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic describes how to view the properties of an Always On

availability group listener

by

using SQL Server Management Studio or Transact-SQL in SQL Server.

1. In Object Explorer, connect to a server instance that hosts any availability replica of the

availability group whose listener you want to view. Click the server name to expand the

server tree.

2. Expand the

node and the

node.

3. Expand the node of the availability group, and expand the

node.

4. Right-click the listener that you want to view, and select the

command.

5. This opens the

dialog box. For more information,

see

Availability Group Listener Properties (Dialog Box)

, later in this topic.

The network name of the availability group listener.

The TCP port used by this listener.

７

Note

If you are connected the primary replica, you can use this field to modify the port number

of the listener. This requires ALTER AVAILABILITY GROUP permission on the availability

group, CONTROL AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP

permission, or CONTROL SERVER permission.