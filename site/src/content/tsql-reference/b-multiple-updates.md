---
name: "B. Multiple updates"
title: "B. Multiple updates"
category: "statements"
description: "Here's the result set."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Here's the result set.

JSON

With

, you can update only one property. If you have to do multiple updates, you

can use multiple

calls.

SQL

Here's the result set.

JSON

## C. Rename a key

## D. Increment a value

The following example shows how to rename a property in JSON text with the

function. First you can take the value of an existing property and insert it as a new key:value

pair. Then you can delete the old key by setting the value of the old property to

.

SQL

Here's the result set.

JSON

If you don't cast the new value to a numeric type,

treats it as text and surrounds it

with double quotes.

The following example shows how to increment the value of a property in JSON text with the

function. First you can take the value of the existing property and insert it as a

new key:value pair. Then you can delete the old key by setting the value of the old property to

.

## E. Modify a JSON object

SQL

Here's the result set.

JSON

treats the

newValue

argument as plain text even if it contains properly formatted

JSON text. As a result, the JSON output of the function is surrounded with double quotes and

all special characters are escaped, as shown in the following example.

SQL

Here's the result set.

JSON

## F. Update a JSON column

To avoid automatic escaping, provide

newValue

by using the

function.

knows that the value returned by

is properly formatted JSON, so it doesn't escape

the value.

SQL

Here's the result set.

JSON

The following example updates the value of a property in a table column that contains JSON.

SQL

JSON Path Expressions

JSON data in SQL Server

Last updated on 11/18/2025

Related content

```sql
JSON_MODIFY
```

```sql
JSON_MODIFY
```

```sql
-- Delete name
SET
@info = JSON_MODIFY(@info,
'$.name'
,
NULL
);
PRINT @info;
-- Add skill
SET
@info = JSON_MODIFY(@info,
'append $.skills'
,
'Azure'
);
PRINT @info;
{
"name"
:
"John"
,
"skills"
: [
"C#"
,
"SQL"
]
} {
"name"
:
"Mike"
,
"skills"
: [
"C#"
,
"SQL"
]
} {
"name"
:
"Mike"
,
"skills"
: [
"C#"
,
"SQL"
],
"surname"
:
"Smith"
} {
"skills"
: [
"C#"
,
"SQL"
],
"surname"
:
"Smith"
} {
"skills"
: [
"C#"
,
"SQL"
,
"Azure"
],
"surname"
:
"Smith"
}
```

```sql
DECLARE
@info
NVARCHAR
(100) =
'{"name":"John","skills":["C#","SQL"]}'
;
PRINT @info;
-- Multiple updates
SET
@info = JSON_MODIFY(JSON_MODIFY(JSON_MODIFY(@info,
'$.name'
,
'Mike'
),
'$.surname'
,
'Smith'
),
'append $.skills'
,
'Azure'
);
PRINT @info;
```

```sql
JSON_MODIFY
```

```sql
NULL
```

```sql
JSON_MODIFY
```

```sql
JSON_MODIFY
```

```sql
NULL
```

```sql
{
"name"
:
"John"
,
"skills"
: [
"C#"
,
"SQL"
]
} {
"name"
:
"Mike"
,
"skills"
: [
"C#"
,
"SQL"
,
"Azure"
],
"surname"
:
"Smith"
}
```

```sql
DECLARE
@product
NVARCHAR
(100) =
'{"price":49.99}'
;
PRINT @product;
-- Rename property
SET
@product = JSON_MODIFY(JSON_MODIFY(@product,
'$.Price'
,
CAST
(JSON_VALUE(@product,
'$.price'
)
AS
NUMERIC
(4, 2))),
'$.price'
,
NULL
);
PRINT @product;
{
"price"
: 49.99
} {
"Price"
: 49.99
}
```

```sql
JSON_MODIFY
```

```sql
DECLARE
@stats
NVARCHAR
(100) =
'{"click_count": 173}'
;
PRINT @stats;
-- Increment value
SET
@stats = JSON_MODIFY(@stats,
'$.click_count'
,
CAST
(JSON_VALUE(@stats,
'$.click_count'
)
AS
INT
) + 1);
PRINT @stats;
{
"click_count"
: 173
} {
"click_count"
: 174
}
```

```sql
DECLARE
@info
NVARCHAR
(100) =
'{"name":"John","skills":["C#","SQL"]}'
;
PRINT @info;
-- Update skills array
SET
@info = JSON_MODIFY(@info,
'$.skills'
,
'["C#","T-SQL","Azure"]'
);
PRINT @info;
{
"name"
:
"John"
,
"skills"
: [
"C#"
,
"SQL"
]
} {
"name"
:
"John"
,
"skills"
:
"[\"C#\",\"T-SQL\",\"Azure\"]"
}
```

```sql
JSON_QUERY
```

```sql
JSON_MODIFY
```

```sql
JSON_QUERY
```

```sql
DECLARE
@info
NVARCHAR
(100) =
'{"name":"John","skills":["C#","SQL"]}'
;
PRINT @info;
-- Update skills array
SET
@info = JSON_MODIFY(@info,
'$.skills'
, JSON_QUERY(
'["C#","T-SQL","Azure"]'
));
PRINT @info;
{
"name"
:
"John"
,
"skills"
: [
"C#"
,
"SQL"
]
} {
"name"
:
"John"
,
"skills"
: [
"C#"
,
"T-SQL"
,
"Azure"
]
}
```

```sql
UPDATE
Employee
SET
jsonCol = JSON_MODIFY(jsonCol,
'$.info.address.town'
,
'London'
)
WHERE
EmployeeID = 17;
```
