---
name: "Collection access"
title: "Collection access"
category: "statements"
description: "Returns the start point of a geometry instance (for LineString types)."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Description

STStartPoint

## Returns the start point of a geometry instance (for LineString types).

STEndpoint

## Returns the end point of a geometry instance (for LineString types).

STPointN

## Returns a specified point from a geometry instance.

STPointOnSurface

## Returns an arbitrary point guaranteed to be within a geometry instance.

STCurveN (geometry Data

Type)

## Returns the specified curve from a geometry instance that's a LineString,

CircularString, or CompoundCurve.

STCurveToLine (geometry

Data Type)

## Returns a polygonal approximation of a geometry instance containing

circular arc segments.

STX

## Returns the X-coordinate of a Point instance.

STY

## Returns the Y-coordinate of a Point instance.

These methods access rings within polygon geometry instances.

## Description

STExteriorRing

## Returns the exterior ring of a Polygon instance as a LineString.

STInteriorRingN

## Returns the specified interior ring of a Polygon instance as a LineString.

STNumInteriorRing

## Returns the number of interior rings in a Polygon instance.

These methods work with geometry collections and return information about their elements.

## Description

STGeometryN

## Returns a specified geometry from a geometry collection.

STNumGeometries

## Returns the number of geometries in a geometry collection.

ﾉ

Expand table

ﾉ

Expand table

#### Method

#### Method
