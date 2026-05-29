---
title: "CurvePolygon"
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
  
  A
  
  is a topologic
tags:
  - "spatial-data"
  - "curvepolygon"
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

A

is a topologically closed surface defined by an exterior bounding ring and

zero or more interior rings in SQL Database Engine spatial data.

The following criteria define attributes of a

instance:

The boundary of the

instance is defined by the exterior ring and all interior

rings.

The interior of the

instance is the space between the exterior ring and all

of the interior rings.

A

instance differs from a

instance in that a

instance can

contain the following circular arc segments:

and

.

Illustration below shows valid

figures:

For a

instance to be accepted, it needs to be either empty or contain only

circular arc rings that are accepted. An accepted circular arc ring meets the following

requirements.

1. Is an accepted

,

, or

instance. For more

information on accepted instances, see

LineString

,

CircularString

, and

CompoundCurve

.

2. Has at least four points.

3. The start and endpoint have the same X and Y coordinates.

）

Important

For a detailed description and examples of spatial features introduced in SQL Server 2012

(11.x), including the

subtype, download the white paper,

.