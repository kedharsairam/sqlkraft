---
title: "View & modify properties"
topic: "migration"
description: |
  Article

  •

  09/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  This topic describes how to view and modify publication properties in SQL Server by using SQL

  Server Management Studio, Tr
tags:
  - "migration"
  - "view-modify-properties-2"
pubDate: 2025-12-01
---

Article

•

09/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

This topic describes how to view and modify publication properties in SQL Server by using SQL

Server Management Studio, Transact-SQL, or Replication Management Objects (RMO).

Limitations and Restrictions

Recommendations

SQL Server Management Studio

Transact-SQL

Replication Management Objects (RMO)

Some properties cannot be modified after a publication has been created, and others

cannot be modified if there are subscriptions to the publication. Properties that cannot be

modified are displayed as read-only.

After a publication is created, some property changes require a new snapshot. If a

publication has subscriptions, some changes also require all subscriptions to be

reinitialized. For more information, see

Change Publication and Article Properties

and

Add

Articles to and Drop Articles from Existing Publications

.

View and modify publication properties in the

dialog

box, which is available in SQL Server Management Studio and Replication Monitor. For
