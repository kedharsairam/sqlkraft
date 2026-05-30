---
title: "Spatial Reference Identifiers (SRIDs)"
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

  Each spatial inst
tags:
  - "spatial-data"
  - "spatial-reference-identifiers-srids"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

database in Microsoft Fabric

Each spatial instance has a spatial reference identifier (SRID). The SRID corresponds to a spatial

reference system based on the specific ellipsoid used for either flat-earth mapping or round-

earth mapping in SQL Database Engine spatial data.

A spatial column can contain objects with different SRIDs. However, only spatial instances with

the same SRID can be used when performing operations with SQL Server spatial data methods

on your data. The result of any spatial method derived from two spatial data instances is valid

only if those instances have the same SRID that is based on the same unit of measurement,

datum, and projection used to determine the coordinates of the instances. The most common

units of measurement of a SRID are meters or square meters.

If two spatial instances do not have the same SRID, the results from a

or

Data Type method used on the instances will return

. For example, for the following

predicate term to return a non-

result, the two

instances,

and

, must have the same SRID:

Spatial Data Types Overview

Last updated on 11/18/2025

７

Note

The spatial reference identification system is defined by the

standard, which is a set of standards developed for cartography,

surveying, and geodetic data storage. This standard is owned by the Oil and Gas

Producers (OGP) Surveying and Positioning Committee.

```sql
NULL
NULL geometry1 geometry2 geometry1.STIntersects(geometry2) = 1
```
