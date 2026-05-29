---
title: "Create, Construct, & Query geography Instances"
topic: "spatial-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL analytics endpoint in Microsoft Fabric
  
  Warehouse in Microsoft Fabric
  
  SQL
  
  database in Microsoft Fabric
  
  The geography spa
tags:
  - "spatial-data"
  - "create-construct-query-geography-instances"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL

database in Microsoft Fabric

The geography spatial data type,

, represents data in a round-earth coordinate

system. This type is implemented as a .NET common language runtime (CLR) data type in SQL

Server. The SQL Server

data type stores ellipsoidal (round-earth) data, such as GPS

latitude and longitude coordinates.

The

type is predefined and available in each database. You can create table

columns of type

and operate on

data in the same manner as you would

use other system-supplied types.

The

data type provides numerous built-in methods you can use to create new

instances based on existing instances.

STBuffer (geography Data Type)

BufferWithTolerance (geography Data Type)

STIntersection (geography Data Type)

STUnion (geography Data Type)

STDifference (geography Data Type)