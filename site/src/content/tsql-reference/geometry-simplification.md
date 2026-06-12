---
name: "Geometry simplification"
title: "Geometry simplification"
category: "data-types"
description: "ToString (geometry Data"
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

## Description

ToString (geometry Data

Type)

## Returns the string representation of a geometry instance augmented with Z

and M values.

These methods access the Z (elevation) and M (measure) values of geometry instances,

supporting 3D and 4D spatial data.

## Description

Z (geometry Data Type)

## Returns the Z (elevation) value of a geometry instance. Null if not defined.

M (geometry Data Type)

## Returns the M (measure) value of a geometry instance. Null if not defined.

HasZ (geometry DataType)

## Returns 1 if a geometry instance contains at least one point with a Z value.

HasM (geometry

DataType)

## Returns 1 if a geometry instance contains at least one point with an M

value.

These methods provide more control over buffer calculations than the standard OGC STBuffer

method.

## Description

BufferWithTolerance

(geometry Data Type)

## Returns a geometric object representing all points within a specified

distance from a geometry instance, with explicit tolerance control for

precision.

BufferWithCurves (geometry

Data Type)

## Returns a geometry instance representing all points within a specified

distance, preserving circular arc segments in the result.

These methods create simplified versions of geometry instances, useful for performance

optimization and visualization at different scales.

Expand table

Expand table

#### Method

#### Method

#### Method
