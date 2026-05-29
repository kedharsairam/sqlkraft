---
title: "Disable Publishing & Distribution"
topic: "migration"
description: |
  Article
  
  •
  
  09/27/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Managed Instance
  
  This topic describes how to disable publishing and distribution in SQL Server by using SQL
  
  Server Management Studio, Trans
tags:
  - "migration"
  - "disable-publishing-distribution"
pubDate: 2025-12-01
---

Article

•

09/27/2024

Applies to:

SQL Server

Azure SQL Managed Instance

This topic describes how to disable publishing and distribution in SQL Server by using SQL

Server Management Studio, Transact-SQL, or Replication Management Objects (RMO).

You can do the following:

Delete all distribution databases on the Distributor.

Disable all Publishers that use the Distributor and delete all publications on those

Publishers.

Delete all subscriptions to the publications. Data in the publication and subscription

databases will not be deleted; however, it loses its synchronization relationship to any

publication databases. If you want the data at the Subscriber to be deleted, you must

delete it manually.

SQL Server Management Studio

Transact-SQL

Replication Management Objects (RMO)

To disable publishing and distribution, all distribution and publication databases must be

online. If any

database snapshots

exist for distribution or publication databases, they must

be dropped before disabling publishing and distribution. A database snapshot is a read-

only offline copy of a database and is not related to a replication snapshot. For more

information, see

Database Snapshots (SQL Server)

.