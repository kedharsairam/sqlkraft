---
name: 'Feature availability'
title: 'Feature availability'
category: 'statements'
description: 'The following example declares vectors using the new'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The following example declares vectors using the new

data type and calculates

distances using the

function.

The

type can be used with variables:

SQL

The

data type can be used as parameter in stored procedure or functions. For example:

SQL

The new

type is available under all database compatibility levels.

### vector

### varchar(max)

### varbinary(max)

### nvarchar(max)

### xml

### json

### Supported

### TDS version 7.4 or higher

```sql
VECTOR_DISTANCE
```

```sql
v VECTOR(3, float16)
-- Uses float16 for reduced storage and precision
);
INSERT
INTO
dbo.vectors (
id
, v)
VALUES
(1,
'[0.1, 2, 30]'
),
(2,
'[-100.2, 0.123, 9.876]'
),
(3, JSON_ARRAY(1.0, 2.0, 3.0));
-- Using JSON_ARRAY to create a vector
SELECT
*
FROM
dbo.vectors;
```

```sql
DECLARE
@v
AS
VECTOR(3) =
'[0.1, 2, 30]'
;
SELECT
@v;
GO
DECLARE
@v
AS
VECTOR(3, float16) =
'[0.1, 2, 30]'
;
SELECT
@v;
```

```sql
CREATE
PROCEDURE
dbo.SampleStoredProcedure
@V VECTOR(3),
@V2 VECTOR(3)
OUTPUT
AS
BEGIN
SELECT
@V;
SET
@V2 = @V;
END
```
