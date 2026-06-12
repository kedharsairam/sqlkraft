---
title: "Create, Construct, & Query geometry Instances"
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

  The planar spatia
tags:
  - "spatial-data"
  - "create-construct-query-geometry-instances"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

The planar spatial data type,

, represents data in a Euclidean (flat) coordinate system.

This type is implemented as a common language runtime (CLR) data type in SQL Server.

The

type is predefined and available in each database. You can create table columns

of type

and operate on

data in the same manner as you would use other

CLR types.

The

data type (planar) supported by SQL Server conforms to the Open Geospatial

Consortium (OGC) Simple Features for SQL Specification version 1.1.0.

For more information on OGC specifications, see the following:

OGC Specifications, Simple Feature Access Part 1 - Common Architecture

OGC Specifications, Simple Feature Access Part 2 - SQL Options

supports a subset of the existing GML 3.1 standard which is defined in the following

schema:

https://schemas.microsoft.com/sqlserver/profiles/gml/SpatialGML.xsd.

The

data type provides numerous built-in methods you can use to create new

instances based on existing instances.

STBuffer (geometry Data Type)

BufferWithTolerance (geometry Data Type)

Reduce (geometry Data Type)

STConvexHull (geometry Data Type)
