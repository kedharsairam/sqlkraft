---
name: "C. Four ranking functions used in the same query"
title: "C. Four ranking functions used in the same query"
category: "predicates"
description: "This example returns the top ten employees ranked by their salary. Because the"
tags: ["tsql", "predicates"]
pubDate: 2026-05-29
---

This example returns the top ten employees ranked by their salary. Because the statement did not specify a clause, the function applied to all result set rows.

SQL

Here's the result set.

This example shows the four ranking functions

DENSE_RANK()

NTILE()

RANK()

ROW_NUMBER() used in the same query. See each ranking function for function-specific examples.

SQL

FirstName

LastName

Row

Number

Rank

Dense

Rank

Quartile

SalesYTD

PostalCode

Here's the result set.

Michael

Blythe

1

1

1

1

4557045.0459

98027

Linda

Mitchell

2

1

1

1

5200475.2313

98027

Jillian

Carson

3

1

1

1

3857163.6332

98027

Garrett

Vargas

4

1

1

1

1764938.9859

98027

Tsvi

Reiter

5

1

1

2

2811012.7151

98027

Shu

Ito

6

6

2

2

3018725.4858

98055

José

Saraiva

7

6

2

2

3189356.2465

98055

David

Campbell

8

6

2

3

3587378.4257

98055

Tete

Mensa-Annan

9

6

2

3

1931620.1835

98055

Lynn

Tsoflias

10

6

2

3

1758385.926

98055

Rachel

Valdez

11

6

2

4

2241204.0424

98055

Jae

Pak

12

6

2

4

5015682.3752

98055

Ranjit

Varkey

Chudukatil

13

6

2

4

3827950.238

98055

```sql
SELECT
```

```sql
PARTITION BY
```

```sql
DENSE_RANK
```

```sql
(10 row(s) affected)
```

```sql
USE
AdventureWorks2022;
GO
SELECT
TOP(10) BusinessEntityID, Rate,
DENSE_RANK
()
OVER
(
ORDER
BY
Rate
DESC
)
AS
RankBySalary
FROM
HumanResources.EmployeePayHistory;
BusinessEntityID Rate                  RankBySalary
---------------- --------------------- --------------------
1                125.50                1
25               84.1346               2
273              72.1154               3
2                63.4615               4
234              60.0962               5
263              50.4808               6
7                50.4808               6
234              48.5577               7
285              48.101                8
274              48.101                8
```

```sql
USE
AdventureWorks2022;
GO
SELECT
p.FirstName, p.LastName
,ROW_NUMBER()
OVER
(
ORDER
BY
a.PostalCode)
AS
"Row Number"
,
RANK
()
OVER
(
ORDER
BY
a.PostalCode)
AS
Rank
,
DENSE_RANK
()
OVER
(
ORDER
BY
a.PostalCode)
AS
"Dense Rank"
,NTILE(4)
OVER
(
ORDER
BY
a.PostalCode)
AS
Quartile
,s.SalesYTD
,a.PostalCode
FROM
Sales.SalesPerson
AS
s
INNER
JOIN
Person.Person
AS
p
ON
s.BusinessEntityID = p.BusinessEntityID
INNER
JOIN
Person.Address
AS
a
ON
a.AddressID = p.BusinessEntityID
WHERE
TerritoryID
IS
NOT
NULL
AND
SalesYTD <> 0;
```
