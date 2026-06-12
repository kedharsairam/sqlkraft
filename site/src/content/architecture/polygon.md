---
title: "Polygon"
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

  is a two-dimen
tags:
  - "spatial-data"
  - "polygon"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

A

is a two-dimensional surface stored as a sequence of points defining an exterior

bounding ring and zero or more interior rings.

A

instance can be formed from a ring that has at least three distinct points. A

instance can also be empty.

The exterior and any interior rings of a

define its boundary. The space within the rings

defines the interior of the.

The following illustration shows examples of

instances.

As shown in the illustration:

1. Figure 1 is a

instance whose boundary is defined by an exterior ring.

2. Figure 2 is a

instance whose boundary is defined by an exterior ring and two

interior rings. The area inside the interior rings is part of the exterior of the

instance.

3. Figure 3 is a valid

instance because its interior rings intersect at a single tangent

point.

Accepted

instances are instances that can be stored in a

or

variable without throwing an exception. The following are accepted

instances:

An Empty

instance
