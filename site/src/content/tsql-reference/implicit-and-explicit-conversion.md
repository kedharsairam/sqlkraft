---
name: "Implicit and explicit conversion"
title: "Implicit and explicit conversion"
category: "operators"
description: "Azure SQL Managed Instance"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Data types can be converted in the following scenarios:

When data from one object is moved to, compared with, or combined with data from

another object, the data might have to be converted from the data type of one object to

the data type of the other.

When data from a Transact-SQL result column, return code, or output parameter is

moved into a program variable, the data must be converted from the SQL Server system

data type to the data type of the variable.

When you convert between an application variable and a SQL Server result set column, return

code, parameter, or parameter marker, the supported data type conversions are defined by the

database API.

Data types can be converted either implicitly or explicitly.

Implicit conversions are not visible to the user. SQL Server automatically converts the data from

one data type to another. For example, when a

is compared to an

, the

is

implicitly converted to

before the comparison proceeds.

implicitly converts to

date style

.

implicitly converts to date style

.

Explicit conversions use the

or

functions.

The

CAST and CONVERT

functions convert a value (a local variable, a column, or another

expression) from one data type to another. For example, the following

function converts

the numeric value of

into a character string of

:

SQL

Use

instead of

if you want Transact-SQL program code to comply with ISO. Use

instead of

to take advantage of the style functionality in

.

### xml

### bigint

The following illustration shows all explicit and implicit data type conversions that are allowed

for SQL Server system-supplied data types. These include

,

, and

sql_variant

. There is

no implicit conversion on assignment from the

sql_variant

data type, but there is implicit

conversion to

sql_variant

.

While the previous chart illustrates all the explicit and implicit conversions that are allowed in

SQL Server, it does not indicate the resulting data type of the conversion.

When SQL Server performs an explicit conversion, the statement itself determines the

resulting data type.

For implicit conversions, assignment statements such as setting the value of a variable or

inserting a value into a column result in the data type that was defined by the variable

declaration or column definition.



### varchar

### int

### int

### varchar

### int

### int

### varchar

For comparison operators or other expressions, the resulting data type depends on the

rules of

data type precedence

.

As an example, the following script defines a variable of type

, assigns an

type value

to the variable, then selects a concatenation of the variable with a string.

SQL

The

value of

is converted to a

, so the

statement returns the value

.

The following example shows a similar script with an

variable instead:

SQL

In this case, the

statement throws the following error:

In order to evaluate the expression

, SQL Server follows the

rules of data type precedence to complete the implicit conversion before the result of the

expression can be calculated. Because

has a higher precedence than

, SQL Server

attempts to convert the string to an integer and fails because this string cannot be converted

to an integer. If the expression provides a string that can be converted, the statement

succeeds, as in the following example:

SQL

In this case, the string

can be converted to the integer value

, so this

statement

## returns the value

. The

operator becomes addition rather than concatenation when the

data types provided are integers.

### nchar

### image

### nchar

### binary

### binary

### nchar

### nvarchar

## Convert data types by using OLE Automation stored

## procedures

Some implicit and explicit data type conversions are not supported when you are converting

the data type of one SQL Server object to another. For example, an

value cannot be

converted to an

value. An

can only be converted to

by using explicit

conversion. An implicit conversion to

is not supported. However, an

can be

explicitly or implicitly converted to

.

The following articles describe the conversion behaviors exhibited by their corresponding data

types:

binary and varbinary

datetime2

money and smallmoney

bit

datetimeoffset

smalldatetime

char and varchar

decimal and numeric

sql_variant

date

float and real

time

datetime

int, bigint, smallint, and tinyint

uniqueidentifier

xml

json

Because SQL Server uses Transact-SQL data types and OLE Automation uses Visual Basic data

types, the OLE Automation stored procedures must convert the data that passes between

them.

The following table describes SQL Server to Visual Basic data type conversions.



Expand table

#### Visual Basic data type

#### char

#### varchar

#### text

#### nvarchar

#### ntext

#### String

#### decimal

#### numeric

#### String

#### bit

#### Boolean

#### binary

#### varbinary

#### image

#### int

#### Long

#### smallint

#### Integer

#### tinyint

#### Byte

#### float

#### Double

#### real

#### Single

#### money

#### smallmoney

#### Currency

#### datetime

#### smalldatetime

#### Date

#### Variant

### binary

### varbinary

### image

### binary

### varbinary

### image

#### Visual Basic data type

#### Long

#### Integer

#### Byte

#### Boolean

#### Object

#### int

#### Double

#### Single

#### float

#### Currency

#### money

#### Date

#### datetime

#### String

#### varchar

#### nvarchar

#### String

#### text

#### ntext

#### varbinary

SQL Server data type

,

,

,

,

,

,

,

One-dimensional

array

,

,

Anything set to

set to Null

All single SQL Server values are converted to a single Visual Basic value except for

,

, and

values. These values are converted to a one-dimensional

array in

Visual Basic. This array has a range of

where

length

is the number of

bytes in the SQL Server

,

, or

values.

These are the conversions from Visual Basic data types to SQL Server data types.

SQL Server data type

,

,

,

,

,

with 4,000 characters or less

/

with more than 4,000 characters

/

One-dimensional

array with 8,000 bytes or less



Expand table

#### Visual Basic data type

#### image

SQL Server data type

One-dimensional

array with more than 8,000 bytes

OLE Automation Stored Procedures (Transact-SQL)

CAST and CONVERT (Transact-SQL)

Data Types (Transact-SQL)

COLLATE (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
GETDATE()
```

```sql
0
```

```sql
SYSDATETIME()
```

```sql
21
```

```sql
CAST
```

```sql
CONVERT
```

```sql
CAST
```

```sql
$157.27
```

```sql
'157.27'
```

```sql
CAST
```

```sql
CONVERT
```

```sql
CONVERT
```

```sql
CAST
```

```sql
CONVERT
```

```sql
CAST ( $157.27 AS VARCHAR(10) )
```

```sql
1
```

```sql
SELECT
```

```sql
1 is a
string.
```

```sql
SELECT
```

```sql
Msg 245, Level 16, State 1, Line 3
Conversion failed when converting the varchar value '
is not a string.' to data type int.
```

```sql
@notastring + ' is not a string.'
```

```sql
1
```

```sql
1
```

```sql
SELECT
```

```sql
2
```

```sql
+
```

```sql
DECLARE
@
string
VARCHAR
(10);
SET
@
string
= 1;
SELECT
@
string
+
' is a string.'
DECLARE
@notastring
INT
;
SET
@notastring =
'1'
;
SELECT
@notastring +
' is not a string.'
DECLARE
@notastring
INT
;
SET
@notastring =
'1'
;
SELECT
@notastring +
'1'
```

```sql
Byte()
```

```sql
NULL
```

```sql
Byte()
```

```sql
Byte( 0 to length 1)
```

```sql
Byte()
```

```sql
Byte()
```
