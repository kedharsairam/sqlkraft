---
title: "Of a Database"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Azure Synapse Analytics
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft
  
  Fabric
  
  When you design a database, you mi
tags:
  - "collation"
  - "of-a-database"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

When you design a database, you might have to estimate how large the database will be when

filled with data. Estimating the size of the database can help you determine the hardware

configuration you'll require to do the following:

Achieve the performance required by your applications.

Guarantee the appropriate physical amount of disk space required to store the data and

indexes.

Estimating the size of a database can also help you determine whether the database design

needs refining. For example, you might determine that the estimated size of the database is

too large to implement in your organization and that more normalization is required.

Conversely, the estimated size might be smaller than expected. This would allow you to

denormalize the database to improve query performance.

To estimate the size of a database, estimate the size of each table individually and then add the

values obtained. The size of a table depends on whether the table has indexes and, if they do,

what type of indexes.

Description

Estimate the size of a

table

Defines the steps and calculations needed to estimate the amount of space

required to store the data in a table and associated indexes.

Estimate the size of a

heap

Defines the steps and calculations needed to estimate the amount of space

required to store the data in a heap. A heap is a table that doesn't have a

clustered index.

Estimate the size of a

clustered index

Defines the steps and calculations needed to estimate the amount of space

required to store the data in a clustered index.

Estimate the size of a

nonclustered index

Defines the steps and calculations needed to estimate the amount of space

required to store the data in a nonclustered index.

ﾉ

Expand table