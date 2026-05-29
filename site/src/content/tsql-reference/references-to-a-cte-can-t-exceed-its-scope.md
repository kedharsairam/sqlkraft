---
name: "References to a CTE can't exceed its scope"
title: "References to a CTE can't exceed its scope"
category: "statements"
description: "This query fails with the following error:"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

This query fails with the following error:

SQL

This query fails with the following error:

SQL

Related content

WITH common_table_expression (Transact-SQL)

SELECT (Transact-SQL)

T-SQL surface area in Microsoft Fabric

```sql
Msg 156, Level 15, State 1, Line 3. Incorrect
syntax near the keyword 'WITH'.
```

```sql
Msg 208, Level 16, State 1, Line 1. Invalid object
name 'inner_cte1_1'.
```

```sql
SELECT
*
FROM
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
c1 = 1),
inner_cte1_2
AS
(
SELECT
*
FROM
inner_cte1_1)
SELECT
*
FROM
inner_cte1_2
)
AS
subq1;
```

```sql
;
WITH
outer_cte_1
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
outer_cte_2
AS
(
WITH
inner_cte2_1
AS
(
SELECT
*
FROM
NestedCTE_t1
WHERE
c3 = 1
)
SELECT
tmp2.*
FROM
inner_cte1_1
AS
tmp1,
inner_cte2_1
AS
tmp2
WHERE
tmp1.c4 = tmp2.c4
)
SELECT
*
FROM
outer_cte_2;
```
