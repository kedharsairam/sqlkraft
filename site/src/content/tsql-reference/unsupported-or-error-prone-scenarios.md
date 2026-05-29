---
name: 'Unsupported or error-prone scenarios'
title: 'Unsupported or error-prone scenarios'
category: 'operators'
description: 'SQL Server supports both'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

## Explicit and implicit conversion between base types float32

## and float16

SQL Server supports both

implicit

and

explicit

conversion from

,

, and

strings to

, as long as the vector is declared with an

explicit dimension count.

SQL

Implicit Conversion is supported only when the target

type is fully declared.

SQL

The following examples highlight common errors and limitations when working with half-

precision float

data type in SQL Server.

### not

## Dimension mismatch

## Null handling

SQL Server currently does

support implicit conversion between

and

.

Additionally,

explicit conversion

using

or

is currently

blocked

.

SQL

The following error is returned:

Output

Conversion between vectors with mismatched dimensions isn't allowed and raises a dimension

mismatch error.

SQL

The following error is returned:

Output

If a vector is declared without a dimension count, assigning a value to it raises an error.

This example works:

SQL

## Out-of-range values

## Mixed base types in functions

However, if the dimension count isn't specified, it raises an error:

SQL

Out-of-range values for

(for example, above 65504.0) raise an error during

assignment.

SQL

The following error is returned:

Output

Mixed base types in functions like

aren't supported and raises a type error.

SQL

The following error is returned:

Output

### varchar(max)

## Unsupported architecture

## SIMD overflow

## Tools support

## Binary transport support for float16 vectors not yet available

isn't supported on Arm64 architectures, and using it raises a runtime error

SQL

The following error is returned:

Output

Single instruction, multiple data (SIMD)-based operations, such as AVX2 or SSE4.2, might

produce overflow errors if values exceed representable ranges.

SQL

The behavior depends on the

setting:

results in an error

results in

SQL Server Management Studio (SSMS) doesn't currently distinguish between

and

in the UI. Use

to confirm the actual base type used in a schema.

vectors are currently transmitted as

(JSON array) over TDS. Binary

transport support for

isn't yet available in drivers like ODBC, JDBC, and .NET.

### vector

Vector search and vector indexes in the SQL Database Engine

Intelligent applications

Last updated on 12/08/2025

７

Note

All limitations that apply to the default

type (with

) also apply to

.

Related content

```sql
VECTOR(<dimension_count>, float16)
```

```sql
DECLARE
@j
AS
JSON
=
'[1.0, 2.0, 3.0]'
;
DECLARE
@v
AS
VECTOR(3, float16);
SET
@v =
CAST
(@j
AS
VECTOR(3, float16));
-- Explicit conversion from JSON to
float16
DECLARE
@v1
AS
VARCHAR
(50) =
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3, float16);
SET
@v2 =
CAST
(@v1
AS
VECTOR(3, float16));
-- Explicit conversion from VARCHAR to
float16
DECLARE
@v1
AS
NVARCHAR
(50) = N
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3, float16);
SET
@v2 =
CAST
(@v1
AS
VECTOR(3, float16));
-- Explicit conversion from NVARCHAR to
float16
-- Implicit conversion from VARCHAR to float16
DECLARE
@v1
AS
VARCHAR
(50) =
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3, float16);
SET
@v2 = @v1;
-- Implicit conversion from NVARCHAR to float16
DECLARE
@v1
AS
NVARCHAR
(50) = N
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3, float16);
SET
@v2 = @v1;
--From JSON_ARRAY to VECTOR
DECLARE
@v3
AS
VECTOR(3, float16) = JSON_ARRAY(1.0, 2.0, 3.0);
```

```sql
VECTOR(float32)
```

```sql
VECTOR(float16)
```

```sql
CAST
```

```sql
CONVERT
```

```sql
DECLARE
@v1
AS
VECTOR(3, float16);
DECLARE
@v2
AS
VECTOR(3, float32) =
'[1.0, 2.0, 3.0]'
;
SET
@v1 =
CAST
(@v2
AS
VECTOR(3, float16));
-- Explicit conversion from float32 to
float16
Error: Msg 42238, Level 16, State 1, Line 61
Conversion of vector from data type float32 to float16 is not allowed.
```

```sql
DECLARE
@v1
AS
VECTOR(3, float16) =
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(4, float16) =
NULL
;
SET
@v1 = @v2;
Error: Msg 42204, Level 16, State 1, Line 10
The vector dimensions 4 and 3 do not match
```

```sql
float16
```

```sql
VECTOR_DISTANCE
```

```sql
DECLARE
@v1
AS
VECTOR(3, float16) =
NULL
;
DECLARE
@v2
AS
VECTOR(3, float16) =
'[1.0, 2.0, 3.0]'
;
SET
@v1 = @v2;
DECLARE
@v1
AS
VECTOR(float16) =
NULL
;
DECLARE
@v2
AS
VECTOR(3, float16) =
'[1.0, 2.0, 3.0]'
;
SET
@v1 = @v2;
```

```sql
DECLARE
@v
AS
VECTOR(3, float16) =
'[1.0, 2.0, 70000.0]'
;
Input JSON contains out-of-range values for float16
```

```sql
DECLARE
@v1
AS
VECTOR(3, float32) =
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3, float16) =
'[1, 2, 3]'
;
SELECT
VECTOR_DISTANCE(
'euclidean'
, @v1, @v2);
VECTOR_DISTANCE does not support different base types
```

```sql
float16
```

```sql
ARITHABORT
```

```sql
ARITHABORT ON
```

```sql
ARITHABORT OFF
```

```sql
NULL
```

```sql
float32
```

```sql
float16
```

```sql
sys.columns
```

```sql
float16
```

```sql
float16
```

```sql
DECLARE
@v1
AS
VECTOR(3, float16) =
'[1.0, 2.0, 3.0]'
;
DECLARE
@v2
AS
VECTOR(3,
int
) =
'[1, 2, 3]'
;
SELECT
VECTOR_DISTANCE(
'euclidean'
, @v1, @v2);
float16 is not supported on ARM64 architecture
```

```sql
DECLARE
@v
AS
VECTOR(8) =
'[-2.9e+38, ..., 2.9e+38]'
;
SELECT
VECTOR_NORM(@v,
'norm1'
);
```

```sql
float32
```

```sql
VECTOR(float16)
```
