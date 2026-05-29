---
title: "View availability group properties"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  This topic describes how to view the properties of an availability group for an Always On

  availability group by using SQL Server Management Studio or
tags:
  - "high-availability"
  - "view-availability-group-properties"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic describes how to view the properties of an availability group for an Always On

availability group by using SQL Server Management Studio or Transact-SQL in SQL Server.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Right-click the availability group whose properties you want to view, and select the

command.

4. In the

dialog box, use the

and

pages to view and, in some cases, change properties of the selected availability group. For

more information, see

Availability Group Properties: New Availability Group (General

Page)

and

Availability Group Properties: New Availability Group (Backup Preferences

Page)

.

Use the

page to view the current logins, roles, and explicit permissions

associated with the availability group. For more information, see

Permissions or

Securables Page

.

To query the properties and states of the availability groups for which the server instance hosts

an availability replica, use the following views:

sys.availability_groups

Returns a row for each availability group for which the local instance of SQL Server hosts an

availability replica. Each row contains a cached copy of the availability group metadata.
