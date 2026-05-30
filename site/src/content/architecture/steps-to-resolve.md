---
title: "Steps to resolve"
topic: "query-processing"
description: "1. If the MSTVF is single statement only, convert to an inline table valued function."
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

1. If the MSTVF is single statement only, convert to an inline table valued function.

The inline format example is displayed next.

2. If more complex, consider using intermediate results stored in Memory-Optimized tables

or temporary tables.

## Best practices for monitoring workloads with Query Store

Sample Database for In-Memory OLTP

User-defined functions

Table Variables and Row Estimations - Part 1

Table Variables and Row Estimations - Part 2

Execution Plan Caching and Reuse

Related content

```sql
CREATE
FUNCTION dbo.tfnGetRecentAddress (@
ID
INT
)
RETURNS
@tblAddress
TABLE ([Address]
VARCHAR (60)
NOT
NULL
)
AS
BEGIN
INSERT
INTO
@tblAddress ([Address])
SELECT
TOP 1 [AddressLine1]
FROM
[Person].[Address]
WHERE
AddressID = @
ID
ORDER
BY
[ModifiedDate]
DESC
;
RETURN;
END
CREATE
FUNCTION dbo.tfnGetRecentAddress_inline (@
ID
INT
)
RETURNS
TABLE
AS
RETURN (
SELECT
TOP 1 [AddressLine1]
AS
[Address]
FROM
[Person].[Address]
WHERE
AddressID = @
ID
ORDER
BY
[ModifiedDate]
DESC
)
```
