---
name: "Angle conversion"
title: "Angle conversion"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

This group provides the elementary trigonometric functions that compute ratios of a right

triangle or model periodic behavior. In SQL workloads, these functions typically support

geometric computation, spatial transformations, data analysis, and simulation models that

require angle-based calculations.

## Description

SIN

Sine of the specified angle.

COS

Cosine of the specified angle.

TAN

Tangent of the input expression.

COT

Cotangent of the specified angle.

Inverse trigonometric functions return the angle that corresponds to a given trigonometric

ratio. These functions enable you to recover an angle from coordinate or sensor data. Use

them in navigation, geospatial analytics, error-vector calculations, and any scenario where you

compute direction or orientation from component values.

## Description

ASIN

Angle (in radians) whose sine is the given value (arcsine).

ACOS

Angle (in radians) whose cosine is the given value (arccosine).

ATAN

Angle (in radians) whose tangent is the given value (arctangent).

ATN2

Angle (in radians) between the positive x-axis and a ray to point

.

These functions convert values between degrees and radians. They serve as utility operations

that support interoperability with APIs, libraries, and mathematical formulas that expect a

specific angular measurement unit.

Expand table

Expand table

#### Function

#### Function

#### Function

```sql
(y, x)
```
