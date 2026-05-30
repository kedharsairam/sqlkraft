---
name: "Set a value in a Transact-SQL variable"
title: "Set a value in a Transact-SQL variable"
category: "statements"
description: "Variables have local scope and are only visible within the batch or procedure where you define"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Variables have local scope and are only visible within the batch or procedure where you define

them. In the following example, the nested scope created for execution of

doesn't have access to the variable declared in the higher scope and returns an error.

This query produces the following error:

Output

When you first declare a variable, its value is

. To assign a value to a variable, use the

statement. This method is the preferred way to assign a value to a variable. You can also assign

a value to a variable by referencing it in the select list of a

statement.

To assign a variable a value by using the

statement, include the variable name and the

value to assign to the variable. This method is the preferred way to assign a value to a variable.

The following batch, for example, declares two variables, assigns values to them, and then uses

them in the

clause of a

statement:

You can also assign a value to a variable by referencing it in a select list. If you reference a

variable in a select list, assign it a scalar value or ensure the

statement returns only one

row. For example:

If a

statement returns more than one row and the variable references a nonscalar

expression, the variable is set to the value returned for the expression in the last row of the

result set. For example, in the following batch

is set to the

value of the last row returned, which is

:

２

Warning

If there are multiple assignment clauses in a single

statement, the Database Engine

doesn't guarantee the order of evaluation of the expressions. Effects are only visible if

there are references among the assignments.

`sp_executesql`

`NULL`

`SET`

`SELECT`

`SET`

`WHERE`

`SELECT`

```sql
DECLARE
@MyVariable
AS
INT
;
SET
@MyVariable = 1;
EXECUTE sp_executesql N
'SELECT @MyVariable'
;
Msg 137, Level 15, State 2, Line 1
Must declare the scalar variable "@MyVariable".
```

```sql
USE
AdventureWorks2025;
GO
-- Declare two variables.
DECLARE
@FirstNameVariable
AS
NVARCHAR (50),
@PostalCodeVariable
AS
NVARCHAR (15);
-- Set their values.
SET
@FirstNameVariable = N
'Amy'
;
SET
@PostalCodeVariable = N
'BA5 3HX'
;
-- Use them in the WHERE clause of a SELECT statement.
SELECT
LastName,
FirstName,
JobTitle,
City,
```

`SELECT`

`SELECT`

```sql
@EmpIDVariable
```

`BusinessEntityID`

```sql
1
```

```sql
PostalCode,
StateProvinceName,
CountryRegionName
FROM
HumanResources.vEmployee
WHERE
FirstName = @FirstNameVariable
OR
PostalCode = @PostalCodeVariable;
USE
AdventureWorks2025;
GO
DECLARE
@EmpIDVariable
AS
INT
;
SELECT
@EmpIDVariable =
MAX (BusinessEntityID)
FROM
HumanResources.Employee;
```

`SELECT`

```sql
USE
AdventureWorks2025;
GO
DECLARE
@EmpIDVariable
AS
INT
;
SELECT
@EmpIDVariable = BusinessEntityID
FROM
HumanResources.Employee
ORDER
BY
BusinessEntityID
DESC
;
SELECT
@EmpIDVariable;
```
