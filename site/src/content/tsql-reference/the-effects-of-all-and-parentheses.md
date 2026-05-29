---
name: 'the effects of ALL and parentheses'
title: 'the effects of ALL and parentheses'
category: 'operators'
description: 'The following examples use'
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

The following examples use

to combine the results of three tables that all have the same

five rows of data. The first example uses

to show the duplicated records, and returns

all 15 rows. The second example uses

without

to eliminate the duplicate rows from

the combined results of the three

statements, and returns five rows.

The third example uses

with the first

and parentheses enclose the second

that isn't using

. The second

is processed first because it's in parentheses, and


## returns five rows because the
option isn't used and the duplicates are removed. These five

rows are combined with the results of the first

by using the

keywords. This

example doesn't remove the duplicates between the two sets of five rows. The final result has

10 rows.

SQL

CREATE TRIGGER (Transact-SQL)

CREATE VIEW (Transact-SQL)

DELETE (Transact-SQL)

EXECUTE (Transact-SQL)

Expressions (Transact-SQL)

INSERT (Transact-SQL)

LIKE (Transact-SQL)

Set Operators - UNION (Transact-SQL)

Set Operators - EXCEPT and INTERSECT (Transact-SQL)

UPDATE (Transact-SQL)

WHERE (Transact-SQL)

PathName (Transact-SQL)

SELECT - INTO clause (Transact-SQL)

Last updated on 02/02/2026

Related content

```sql
UNION
```

```sql
UNION ALL
```

```sql
UNION
```

```sql
ALL
```

```sql
SELECT
```

```sql
ALL
```

```sql
UNION
```

```sql
UNION
```

```sql
ALL
```

```sql
UNION
```

```sql
ALL
```

```sql
SELECT
```

```sql
UNION ALL
```

```sql
ORDER
BY
Name
;
GO
```

```sql
USE
AdventureWorks2025;
GO
IF OBJECT_ID('dbo.EmployeeOne', 'U') IS NOT NULL
DROP
TABLE
dbo.EmployeeOne;
GO
IF OBJECT_ID('dbo.EmployeeTwo', 'U') IS NOT NULL
DROP
TABLE
dbo.EmployeeTwo;
GO
IF OBJECT_ID('dbo.EmployeeThree', 'U') IS NOT NULL
DROP
TABLE
dbo.EmployeeThree;
GO
SELECT
pp.LastName, pp.FirstName, e.JobTitle
INTO
dbo.EmployeeOne
FROM
Person.Person
AS
pp
INNER
JOIN
HumanResources.Employee
AS
e
ON
e.BusinessEntityID = pp.BusinessEntityID
WHERE
LastName =
'Johnson'
;
GO
SELECT
pp.LastName, pp.FirstName, e.JobTitle
INTO
dbo.EmployeeTwo
FROM
Person.Person
AS
pp
INNER
JOIN
HumanResources.Employee
AS
e
```

```sql
ON
e.BusinessEntityID = pp.BusinessEntityID
WHERE
LastName =
'Johnson'
;
GO
SELECT
pp.LastName, pp.FirstName, e.JobTitle
INTO
dbo.EmployeeThree
FROM
Person.Person
AS
pp
INNER
JOIN
HumanResources.Employee
AS
e
ON
e.BusinessEntityID = pp.BusinessEntityID
WHERE
LastName =
'Johnson'
;
GO
-- Union ALL
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeOne
UNION
ALL
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeTwo
UNION
ALL
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeThree;
GO
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeOne
UNION
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeTwo
UNION
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeThree;
GO
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeOne
UNION
ALL
(
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeTwo
UNION
SELECT
LastName, FirstName, JobTitle
FROM
dbo.EmployeeThree
```

```sql
);
GO
```
