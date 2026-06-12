---
name: "Point and curve access"
title: "Point and curve access"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

## Description

STCentroid

## Returns the geometric center (centroid) of a geometry instance consisting of one or more

polygons.

STEnvelope

## Returns the minimum axis-aligned bounding rectangle (envelope) of a geometry instance.

STConvexHull

## Returns the convex hull of a geometry instance, representing the smallest convex polygon

that contains all points.

These methods convert geometry instances between different representation formats.

## Description

STAsBinary

## Returns the OGC Well-Known Binary (WKB) representation of a geometry instance.

STAsText

## Returns the OGC Well-Known Text (WKT) representation of a geometry instance.

These methods return information about the geometry type and characteristics.

## Description

STGeometryType

## Returns the OGC type name for a geometry instance (Point, LineString, Polygon,

MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection).

STDimension

## Returns the maximum dimension of a geometry instance: 0 for points, 1 for curves, or

2 for surfaces.

STSrid

## Returns the spatial reference identifier (SRID) of a geometry instance.

These methods access specific points and curves within a geometry instance.

Expand table

Expand table

Expand table

#### Method

#### Method

#### Method
