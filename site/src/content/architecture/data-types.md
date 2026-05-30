---
title: "Data Types"
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

  There are two typ
tags:
  - "spatial-data"
  - "data-types"
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

There are two types of spatial data. The

data type supports planar, or Euclidean (flat-

earth), data. The

data type both conforms to the

Open Geospatial Consortium (OGC)

Simple Features for SQL Specification

version 1.1.0 and is compliant with SQL MM (ISO

standard).

SQL Server also supports the

data type, which stores ellipsoidal (round-earth) data,

such as GPS latitude and longitude coordinates.

The

and

data types support 16 types of spatial data objects, or instance

types. However, only 11 of these instance types are

instantiable

; you can create and work with

these instances (or instantiate them) in a database. These instances derive certain properties

from their parent data types.

The following figure shows the geometry hierarchy upon which the

and

data types are based. The instantiable types of

and

are indicated in blue.



Tip

SQL Server spatial tools is a Microsoft sponsored open-source collection of tools for use

with the spatial types in SQL Server. This project provides a set of reusable functions which

applications can make use of. These functions may include data conversion routines, new

transformations, aggregates, etc. See

in GitHub for

more details.
