---
name: 'Examples: Microsoft Fabric Data Warehouse'
title: 'Examples: Microsoft Fabric Data Warehouse'
category: 'statements'
description: 'The following example prevents the pushdown of the'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## I. Query data as of a point in time

## J. SELECT statement with a label in the OPTION clause

The following example prevents the pushdown of the

clause to the MapReduce job on

the external Hadoop table. All rows are returned to PDW where the

clause is applied.

SQL

For more information, see

FOR TIMESTAMP query hint

.

Use the


## syntax in the
clause to query data as it existed in the past, in Fabric

Data Warehouse. The following sample query returns data as it appeared on March 13, 2024 at

7:39:35.28 PM UTC. The time zone is always in UTC.

SQL

The following example shows a

statement with a label in the

clause. For more

information, see

Query labels in Fabric Data Warehouse

.

SQL

Query hints (Transact-SQL)

SELECT (Transact-SQL)

UPDATE (Transact-SQL)

MERGE (Transact-SQL)

DELETE (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
WHERE
```

```sql
WHERE
```

```sql
TIMESTAMP
```

```sql
OPTION
```

```sql
SELECT
```

```sql
OPTION
```

```sql
SELECT
ID
FROM
External_Table_AS A
WHERE
ID
< 1000000
OPTION
(
FORCE
EXTERNALPUSHDOWN);
SELECT
ID
FROM
External_Table_AS A
WHERE
ID
< 10
OPTION
(
DISABLE
EXTERNALPUSHDOWN);
```

```sql
SELECT
OrderDateKey,
SUM
(SalesAmount)
AS
TotalSales
FROM
FactInternetSales
GROUP
BY
OrderDateKey
ORDER
BY
OrderDateKey
OPTION
(
FOR
TIMESTAMP
AS
OF
'2024-03-13T19:39:35.28'
);
--March 13, 2024 at 7:39:35.28
PM UTC
```

```sql
SELECT
*
FROM
FactResellerSales
OPTION
(LABEL =
'q17'
);
```
