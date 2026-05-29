---
title: "CompoundCurve"
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
  
  is a collectio
tags:
  - "spatial-data"
  - "compoundcurve"
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

is a collection of zero or more continuous

or

instances of either

or

types.

An empty

instance can be instantiated, but for a

to be

valid it must meet the following criteria:

1. It must contain at least one

or

instance.

2. The sequence of

or

instances must be continuous.

If a

contains a sequence of multiple

and

instances,

the ending endpoint for every instance except for the last instance must be the starting

endpoint for the next instance in the sequence. This means that if the ending point of a prior

instance in the sequence is (4 3 7 2), the starting point for the next instance in the sequence

must be (4 3 7 2). Z(elevation) and M(measure) values for the point must also be the same. If

there is a difference in the two points, a

is thrown. Points in a

do not have to have a Z or M value. If no Z or M values are given for the ending

point of the prior instance, the starting point of the next instance cannot include Z or M values.

If the ending point for the prior sequence is (4 3), the starting point for the next sequence must

be (4 3); it cannot be (4 3 7 2). All points in a

instance must have either no Z

value or the same Z value.

The following illustration shows valid

types.

instance is accepted if it is an empty instance or meets the following criteria.

1. All the instances contained by

instance are accepted circular arc

segment instances. For more information on accepted circular arc segment instances, see

```sql
System.FormatException
```