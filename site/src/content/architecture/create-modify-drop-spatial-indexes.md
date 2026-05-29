---
title: "Create, Modify, & Drop Spatial Indexes"
topic: "spatial-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  A spatial index can more efficiently perform certain operations on a column of the
  
  or
  
  data 
tags:
  - "spatial-data"
  - "create-modify-drop-spatial-indexes"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A spatial index can more efficiently perform certain operations on a column of the

or

data type (a

spatial column

). More than one spatial index can be specified on a

spatial column. This is useful, for example, for indexing different tessellation parameters in a

single column.

There are a number of restrictions on creating spatial indexes. For more information, see

Restrictions on Spatial Indexes

in this topic.

CREATE SPATIAL INDEX (Transact-SQL)

1. In Object Explorer, connect to an instance of the SQL Server Database Engine and then

expand that instance.

2. Expand

, expand the database that contains the table with the specified index,

and then expand

.

3. Expand the table for which you want to create the index.

4. Right-click

and select

.

5. In the

field, enter a name for the index.

6. In the

drop-down list, select

.

７

Note

For information about the relationship of spatial indexes to partition and to filegroups, see

the "Remarks" section in

.

To create a spatial index in Management Studio