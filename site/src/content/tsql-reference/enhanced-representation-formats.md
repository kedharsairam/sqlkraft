---
name: "Enhanced representation formats"
title: "Enhanced representation formats"
category: "statements"
description: "Summarize this article for me"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

SQL Server supports extended methods on

instances that go beyond the Open

Geospatial Consortium (OGC) standard methods. These extended methods provide additional

functionality for working with planar geometric data, including Z (elevation) and M (measure)

values, precise buffer operations, simplified representations, and enhanced WKT/WKB formats.

While OGC methods provide standardized spatial operations defined by the OpenGIS

specification, extended methods offer SQL Server-specific enhancements:

: Standardized operations for interoperability with other geospatial

systems. Use when standards compliance is required.

: SQL Server-specific operations that provide additional functionality,

performance optimizations, or support for features not covered by OGC standards (such

as circular arcs, Z/M values, and advanced buffer control).

For most spatial tasks, OGC methods provide the necessary functionality. Use extended

methods when you need the extra capabilities they provide.

These methods provide alternative formats for representing geometry data, including support

for Z (elevation) and M (measure) values.

## Description

AsBinaryZM (geometry

DataType)

## Returns the OGC Well-Known Binary (WKB) representation augmented with Z

(elevation) and M (measure) values.

AsTextZM (geometry

Data Type)

## Returns the OGC Well-Known Text (WKT) representation augmented with Z

(elevation) and M (measure) values.

AsGml (geometry Data

Type)

## Returns the Geography Markup Language (GML) representation of a

geometry instance.

ﾉ

Expand table

#### Method

#### Method

#### Method
