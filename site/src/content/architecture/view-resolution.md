---
title: "View resolution"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

When the

statement in

is optimized in SQL Server, the value of

isn't

known. Therefore, the Query Optimizer uses a default estimate for the selectivity of

, (in this case 30 percent).

The basic steps described for processing a

statement apply to other Transact-SQL

statements such as

,

, and

.

and

statements both have to

target the set of rows to be modified or deleted. The process of identifying these rows is the

same process used to identify the source rows that contribute to the result set of a

statement. The

and

statements might both contain embedded

statements that provide the data values to be updated or inserted.

Even Data Definition Language (DDL) statements, such as

or

,

are ultimately resolved to a series of relational operations on the system catalog tables and

sometimes (such as

) against the data tables.

The Relational Engine might need to build a worktable to perform a logical operation specified

in an Transact-SQL statement. Worktables are internal tables that are used to hold intermediate

results. Worktables are generated for certain

,

, or

queries. For

example, if an

clause references columns that aren't covered by any indexes, the

Relational Engine might need to generate a worktable to sort the result set into the order

requested. Worktables are also sometimes used as spools that temporarily hold the result of

executing a part of a query plan. Worktables are built in

and are dropped automatically

when they are no longer needed.

The SQL Server query processor treats indexed and nonindexed views differently:

The rows of an indexed view are stored in the database in the same format as a table. If

the Query Optimizer decides to use an indexed view in a query plan, the indexed view is

treated the same way as a base table.

Only the definition of a nonindexed view is stored, not the rows of the view. The Query

Optimizer incorporates the logic from the view definition into the execution plan it builds

for the Transact-SQL statement that references the nonindexed view.

The logic used by the SQL Server Query Optimizer to decide when to use an indexed view is

similar to the logic used to decide when to use an index on a table. If the data in the indexed

view covers all or part of the Transact-SQL statement, and the Query Optimizer determines that

an index on the view is the low-cost access path, the Query Optimizer will choose the index

regardless of whether the view is referenced by name in the query.

When an Transact-SQL statement references a nonindexed view, the parser and Query

Optimizer analyze the source of both the Transact-SQL statement and the view and then

resolve them into a single execution plan. There isn't one plan for the Transact-SQL statement

and a separate plan for the view.

For example, consider the following view:

Based on this view, both of these Transact-SQL statements perform the same operations on the

base tables and produce the same results:

The SQL Server Management Studio Showplan feature shows that the relational engine builds

the same execution plan for both of these

statements.

`SELECT`

`MyProc2`

```sql
@d2
```

```sql
OrderDate
> @d2
```

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

`UPDATE`

`DELETE`

`SELECT`

`UPDATE`

`INSERT`

`SELECT`

```sql
CREATE PROCEDURE
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE ADD COLUMN
```

```sql
GROUP BY
```

```sql
ORDER BY
```

`UNION`

```sql
ORDER BY
```

`tempdb`

```sql
WHERE
OrderDate > @d2
END
;
```

`SELECT`

```sql
USE
AdventureWorks2022;
GO
CREATE
VIEW
EmployeeName
AS
SELECT h.BusinessEntityID, p.LastName, p.FirstName
FROM
HumanResources.Employee
AS h
JOIN
Person.Person
AS p
ON h.BusinessEntityID = p.BusinessEntityID;
GO
/* SELECT referencing the EmployeeName view. */
SELECT
LastName
AS
EmployeeLastName, SalesOrderID, OrderDate
FROM
AdventureWorks2022.Sales.SalesOrderHeader
AS soh
JOIN
AdventureWorks2022.dbo.EmployeeName
AS
EmpN
ON (soh.SalesPersonID = EmpN.BusinessEntityID)
WHERE
OrderDate >
'20020531'
;
/* SELECT referencing the Person and Employee tables directly. */
SELECT
LastName
AS
EmployeeLastName, SalesOrderID, OrderDate
FROM
AdventureWorks2022.HumanResources.Employee
AS e
JOIN
AdventureWorks2022.Sales.SalesOrderHeader
AS soh
ON soh.SalesPersonID = e.BusinessEntityID
JOIN
AdventureWorks2022.Person.Person
AS p
ON e.BusinessEntityID =p.BusinessEntityID
WHERE
OrderDate >
'20020531'
;
```
