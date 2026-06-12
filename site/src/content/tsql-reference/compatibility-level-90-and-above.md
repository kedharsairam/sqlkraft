---
name: "Compatibility level 90 and above"
title: "Compatibility level 90 and above"
category: "operators"
description: "In the preceding code example, the final example has a mismatch between format"
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

In the preceding code example, the final example has a mismatch between format versus the input string. The third node of the input string represents a numeric value that is too large to be a day. Microsoft doesn't guarantee the output value from such mismatches.

Our CAST and CONVERT documentation article lists explicit codes that can you can use with the CONVERT function to deterministically control date conversions. Every month the article has one of our highest pageview counts.

CAST and CONVERT (Transact-SQL): Date and time styles

CAST and CONVERT (Transact-SQL): Certain datetime conversions are nondeterministic

In SQL Server 2000, the compatibility level was 80. For level settings of 80 or below, implicit date conversions were deterministic.

Starting with SQL Server 2005 and its compatibility level of 90, implicit date conversions became nondeterministic. Date conversions became dependent on SET LANGUAGE and SET

DATEFORMAT starting with level 90.

## Unicode

Conversion of non-Unicode character data between collations is also considered nondeterministic.

Set a Session Language

Date and Time Data Types and Functions (Transact-SQL)

FORMAT (Transact-SQL)

ISDATE (Transact-SQL)

See also json

xml

datetimeoffset

datetime2

datetime

smalldatetime

date

time

float

real

decimal

money

smallmoney

bigint

int

smallint

tinyint

bit

ntext

text

image

timestamp

uniqueidentifier

nvarchar

nvarchar(max)

nchar

varchar

varchar(max)

char

Analytics Platform System (PDW)

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

When an operator combines expressions of different data types, the data type with the lower precedence is first converted to the data type with the higher precedence. If the conversion isn't a supported implicit conversion, an error is returned. For an operator combining operand expressions having the same data type, the result of the operation has that data type.

uses the following precedence order for data types:

1. user-defined data types (highest)

2.

3.

sql_variant

4.

5.

6.

7.

8.

9.

10.

11.

12.

13.

14.

15.

16.

17.

18.

19.

20.

21.

22.

23.

24.

25.

26.

, including

27.

28.

, including

29.

varbinary

varbinary(max)

binary

30.

, including

31.

(lowest)

Data types (Transact-SQL)

Expressions (Transact-SQL)

CAST and CONVERT (Transact-SQL)

Synonym

binary varying

varbinary

char varying

varchar

character

char

character char(1) character(

) char(n) character varying(

) varchar(n) dec

decimal

double precision

float

float

(

)

real

float

(

)

float

integer

int

national character(

) nchar(n) national char(

) nchar(n) national character varying(

) nvarchar(n) national char varying(

) nvarchar(n) national text

ntext

rowversion

timestamp

Analytics Platform System (PDW)

SQL analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

Data type synonyms are included in SQL Server for ISO compatibility. The following table lists the synonyms and the SQL Server system data types that they map to.

system data type n n

[ n

] for n

= 1-7

[ n

] for n

= 8-15 n n n n

Data type synonyms can be used instead of the corresponding base data type name in data definition language (DDL) statements. These statements include CREATE TABLE, CREATE

PROCEDURE, and DECLARE

@variable. However, after the object is created, the synonyms have sp_help nvarchar(10) nvarchar(10) national character varying(10) no visibility. When the object is created, the object is assigned the base data type that is associated with the synonym. There's no record that the synonym was specified in the statement that created the object.

Objects that are derived from the original object, such as result set columns or expressions, are assigned the base data type. Any metadata functions that use the original object or any derived objects will report the base data type, not the synonym, including:

Metadata operations, such as and other system stored procedures,
Information schema views, and

Data access API metadata operations that report the data types of table or result set columns.

For example, you can create a table by specifying

: SQL is assigned an data type, and all following metadata functions will report the column as an column. The metadata functions will never report them as a column.

Data Types (Transact-SQL)

See also

```sql
SET
DATEFORMAT dmy;
SELECT
CONVERT (
DATE
, @yourDateString)
AS
[DMY-Interpretation-
of
-
input
-
format
];
SET
DATEFORMAT mdy;
SELECT
CONVERT (
DATE
, @yourDateString)
AS
[MDY-Interpretation-
of
-
input
-
format
];
SET
DATEFORMAT ymd;
SELECT
CONVERT (
DATE
, @yourDateString)
AS
[YMD-Interpretation
--?--NotGuaranteed];
/*** Actual output:
12-09-2018 = the input.
DMY-Interpretation-of-input-format
2018-09-12
MDY-Interpretation-of-input-format
2018-12-09
YMD-Interpretation--?--NotGuaranteed
2018-12-09
***/
```

```sql
national character varying
```

`VarCharCol`

```sql
CREATE
TABLE
ExampleTable (PriKey int
PRIMARY
KEY
, VarCharCol national character varying (10))
```
