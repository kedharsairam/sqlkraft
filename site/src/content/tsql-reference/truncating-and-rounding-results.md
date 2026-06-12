---
name: "Truncating and rounding results"
title: "Truncating and rounding results"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: 2026-05-29
---

When you explicitly or implicitly cast the data type to a string or binary data type, the content of the data type is serialized based on a defined set of rules. For information about these rules, see

Define the Serialization of XML Data. For information about conversion from other data types to the data type, see

Create Instances of XML Data.

The and data types don't support automatic data type conversion. You can explicitly convert data to character data, and data to or

, but the maximum length is 8000 bytes. If you try an incorrect conversion, for example trying to convert a character expression that includes letters to an
, SQL Server returns an error message.

When the or functions output a character string, and they receive a character string input, the output has the same collation and collation label as the input. If the input isn't a character string, the output has the default collation of the database, and a collation label of coercible-default. For more information, see

Collation Precedence (Transact-SQL).

To assign a different collation to the output, apply the COLLATE clause to the result expression of the or function. For example: SQL

When converting character or binary expressions (

,

,

,

,

, or

) to an expression of a different data type, the conversion operation could truncate the output data, only partially display the output data, or return an error. These cases will occur if the result is too short to display. Conversions to

,

,

,

,

, or are truncated, except for the conversions shown in the following table.

,

, or

Too short to display

From data type

To data type

Result

nchar

nvarchar

money

smallmoney

numeric

decimal

float

real

char

varchar

nchar

nvarchar

binary

decimal

numeric

binary

Error

,

,

,

,

, or Error

Error

Error returned because result length is too short to display.

guarantees that only roundtrip conversions, in other words conversions that convert a data type from its original data type and back again, yield the same values from version to version. The following example shows such a roundtrip conversion: SQL

The following example shows a resulting expression that is too small to display.

1

1

1

1

２

Warning

Don't construct

values, and then convert them to a data type of the numeric data type category. SQL Server does not guarantee that the result of a or data type conversion, to

, will be the same between versions of SQL Server.

From

To

Behavior

numeric

numeric

numeric

int

numeric

money

money

int

money

numeric

float

int

float

numeric

float

datetime

datetime

int

float

decimal

numeric

int

numeric

Here's the result set.

Output

When you convert data types that differ in decimal places, SQL Server will sometimes return a truncated result value, and at other times it will return a rounded value. This table shows the behavior.

Round

Truncate

Round

Round

Round

Truncate

Round

Round

Round

Conversion of values that use scientific notation to or is restricted to values of precision 17 digits only. Any value with precision higher than 17 rounds to zero.

For example, the values 10.6496 and -10.6496 may be truncated or rounded during conversion to or types:
1

1 trunc1 trunc2 round1 round2

char

nchar

nvarchar

varchar

decimal

float

int

numeric

numeric

decimal

`CAST`

`CONVERT`

`CAST`

`CONVERT`

```sql
SELECT
CAST (
'abc'
AS varchar (5))
COLLATE
French_CS_AS;
```

```sql
DECLARE
@myval
DECIMAL (5, 2);
SET
@myval = 193.57;
SELECT
CAST (
CAST (@myval
AS
VARBINARY(20))
AS
DECIMAL (10, 5));
-- Or, using CONVERT
SELECT
CONVERT (
DECIMAL (10, 5),
CONVERT (VARBINARY(20), @myval));
GO
```

```sql
USE
AdventureWorks2022;
GO
SELECT p.FirstName,
p.LastName,
SUBSTRING (p.Title, 1, 25)
AS
Title,
CAST (e.SickLeaveHours
AS
CHAR (1))
AS
[Sick Leave]
FROM
HumanResources.Employee e
INNER
JOIN
Person.Person p
ON e.BusinessEntityID = p.BusinessEntityID
```

```sql
WHERE
NOT e.BusinessEntityID > 5;
GO
FirstName LastName Title Sick Leave
--------- ------------- ------- --------`
Ken Sanchez NULL *
Terri Duffy NULL *
Roberto Tamburello NULL *
Rob Walters NULL *
Gail Erickson Ms. *
(5 row(s) affected)
```
