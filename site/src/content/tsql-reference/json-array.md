---
name: "JSON_ARRAY"
title: "JSON_ARRAY"
category: "statements"
description: "The following example returns rows in which the column"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The following example returns rows in which the column

contains valid JSON.

SQL

The following example returns rows in which the column

contains valid JSON

SCALAR value at top level.

SQL

The following example returns 1 since the input is a valid JSON value -

true

.

SQL

The following example returns 0 since the input is an invalid JSON value.

SQL

The following example returns 1 since the input is a valid JSON scalar according to RFC 8259.

SQL

JSON data in SQL Server

Last updated on 11/18/2025

Related content

### nvarchar(max)

### json

```sql
json_col
```

```sql
json_col
```

```sql
SELECT
id
, json_col
FROM
tab1
WHERE
ISJSON(json_col) = 1
```

```sql
SELECT
id
, json_col
FROM
tab1
WHERE
ISJSON(json_col, SCALAR) = 1
```

```sql
SELECT
ISJSON(
'true'
,
VALUE
)
```

```sql
SELECT
ISJSON(
'test string'
,
VALUE
)
```

```sql
SELECT
ISJSON(
'"test string"'
, SCALAR)
```
