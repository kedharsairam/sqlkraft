---
title: "Add secondary replica"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to add a secondary replica to an existing Always On availability group
  
  by using SQL Server Management Studio, Transact-SQL, o
tags:
  - "high-availability"
  - "add-secondary-replica"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to add a secondary replica to an existing Always On availability group

by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

You must be connected to the server instance that hosts the primary replica.

For more information, see

Prerequisites, Restrictions, and Recommendations for Always On

Availability Groups (SQL Server)

.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

We are listening:

If you find something outdated or incorrect in this article, such as a step

or a code example, please tell us. You can click the

button in the

section at the bottom of this page. We read every item of feedback about SQL, typically the

next day. Thanks.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Right-click the availability group, and select one of the following commands:

Prerequisites and Restrictions