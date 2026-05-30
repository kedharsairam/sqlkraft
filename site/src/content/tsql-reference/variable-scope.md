---
name: "Variable scope"
title: "Variable scope"
category: "variables"
description: "To declare more than one local variable, use a comma after the first local variable definition,"
tags: ["tsql", "variables"]
pubDate: 2026-05-29
---

To declare more than one local variable, use a comma after the first local variable definition,

and then specify the next local variable name and data type.

For example, the following

statement creates three local variables named

,

, and

, and initializes each to

:

In another example, the following

statement creates a Boolean variable called

, which is declared as

with a value of

(

):

The scope of a variable is the range of Transact-SQL statements that can reference the variable.

The scope of a variable lasts from the point it's declared until the end of the batch or stored

procedure in which it's declared. For example, the following script generates a syntax error

because the variable is declared in one batch (separated by the

keyword) and referenced in

another:

`DECLARE`

```sql
@LastName
```

```sql
@FirstName
```

```sql
@StateProvince
```

`NULL`

`DECLARE`

```sql
@IsActive
```

```sql
0
```

`false`

`GO`

```sql
DECLARE
@MyCounter
AS
INT
;
DECLARE
@LastName
AS
NVARCHAR (30),
@FirstName
AS
NVARCHAR (20),
@StateProvince
AS
NCHAR (2);
DECLARE
@IsActive
AS
BIT
= 0;
```

```sql
USE
AdventureWorks2025;
GO
DECLARE
@MyVariable
AS
INT
;
SET
@MyVariable = 1;
SELECT
BusinessEntityID,
NationalIDNumber,
JobTitle
FROM
HumanResources.Employee
WHERE
BusinessEntityID = @MyVariable;
```
