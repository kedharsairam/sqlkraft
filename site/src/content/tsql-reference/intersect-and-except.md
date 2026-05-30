---
name: "intersect, and except"
title: "Intersect, and except"
category: "queries"
description: "CTE names can be reused at different nesting levels. CTE names at the same nesting level can't"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

CTE names can be reused at different nesting levels. CTE names at the same nesting level can't

be duplicated. In this example, the name

is used in both outer and inner scope.

SQL

SQL

```sql
cte1
```

```sql
)
SELECT
*
FROM
INNER_CTE
)
SELECT
*
FROM
OUTER_CTE;
```

```sql
;
WITH
cte1
AS
(
WITH
inner_cte1_1
AS
(
SELECT
*
FROM
NestedCTE_t1
WHERE
c1 = 1
),
inner_cte1_2
AS
(
SELECT
*
FROM
inner_cte1_1
WHERE
c2 = 1
)
SELECT
*
FROM
inner_cte1_2
),
cte2
AS
(
WITH
cte1
AS
(
SELECT
*
FROM
NestedCTE_t1
WHERE
c3 = 1
),
inner_cte2_2
AS
(
SELECT
*
FROM
cte1
WHERE
c4 = 1
)
SELECT
*
FROM
inner_cte2_2
)
```

```sql
CREATE
TABLE
NestedCTE_t1 (
c1
INT
,
c2
INT
,
c3
INT
);
GO
INSERT
INTO
NestedCTE_t1
```
