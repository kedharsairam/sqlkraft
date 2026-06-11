---
name: "Shape properties"
title: "Shape properties"
category: "statements"
description: "Describes the shape properties available for spatial data types in T-SQL, including geometry and geography methods."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

SQL Server's

data type implements methods defined by the Open Geospatial

Consortium (OGC) Simple Features for SQL Specification version 1.1.0. These standardized

methods ensure that spatial calculations conform to industry standards and work consistently

with other geospatial applications.

The

data type represents data in a Euclidean (flat) coordinate system. Use OGC

methods when you need standards-compliant spatial operations for planar data, such as

calculating areas, distances, spatial relationships, and performing geometric transformations.

The OGC Simple Features specification defines a common architecture for geographic

information and provides SQL implementation options for spatial data. SQL Server's geometry

type conforms to these specifications, making it interoperable with other geospatial systems.

For more information on OGC specifications, see:

OGC Specifications, Simple Feature Access Part 1 - Common Architecture

OGC Specifications, Simple Feature Access Part 2 - SQL Options

These methods return measurements and properties that describe the geometric shape.

## Description

STArea

## Returns the total surface area of a geometry instance in square units based on its spatial

reference identifier (SRID).

STLength

## Returns the total length of elements in a geometry instance or all elements in a geometry

collection.

STBoundary

## Returns the boundary of a geometry instance as a lower-dimensional geometry.

Expand table

#### Method

#### Method

#### Method
