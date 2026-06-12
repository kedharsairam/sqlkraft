---
title: "Dialog"
topic: "high-availability"
description: |
  Article

  •

  09/04/2024

  Applies to:

  SQL Server

  This topic describes how to add a database to an Always On availability group by using SQL

  Server Management Studio, Transact-SQL, or PowerShell in SQ
tags:
  - "high-availability"
  - "dialog-2"
pubDate: 2025-12-01
---

Article

•

09/04/2024

SQL Server

This topic describes how to add a database to an Always On availability group by using SQL

Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

You must be connected to the server instance that hosts the primary replica.

The database must reside on the server instance that hosts the primary replica and

comply with the prerequisites and restrictions for availability databases. For more

information, see

Prerequisites, Restrictions, and Recommendations for Always On

Availability Groups (SQL Server).

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Right-click the availability group, and select one of the following commands:

To launch the Add Database to Availability Group Wizard, select the

command. For more information, see

Use the Add Database to Availability Group

Wizard (SQL Server Management Studio).

To add one or more databases by specifying them in the

dialog box, select the

command. The steps for adding a

database are as follows:

Prerequisites and Restrictions
