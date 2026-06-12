---
name: "Implicit and explicit conversion"
title: "Implicit and explicit conversion"
category: "operators"
description: ""
tags: ["tsql","operators"]
pubDate: 2026-05-29
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

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

date style.

implicitly converts to date style.

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

Use

instead of

if you want Transact-SQL program code to comply with ISO. Use

instead of

to take advantage of the style functionality in.

The following illustration shows all explicit and implicit data type conversions that are allowed

for SQL Server system-supplied data types. These include

,

, and

sql_variant. There is

no implicit conversion on assignment from the

sql_variant

data type, but there is implicit

conversion to

sql_variant.

While the previous chart illustrates all the explicit and implicit conversions that are allowed in

, it does not indicate the resulting data type of the conversion.

When SQL Server performs an explicit conversion, the statement itself determines the

resulting data type.

For implicit conversions, assignment statements such as setting the value of a variable or

inserting a value into a column result in the data type that was defined by the variable

declaration or column definition.



For comparison operators or other expressions, the resulting data type depends on the

rules of

data type precedence.

As an example, the following script defines a variable of type

, assigns an

type value

to the variable, then selects a concatenation of the variable with a string.

The

value of

is converted to a

, so the

statement returns the value.

The following example shows a similar script with an

variable instead:

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

In this case, the string

can be converted to the integer value

, so this

statement

## returns the value. The

operator becomes addition rather than concatenation when the

data types provided are integers.

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

explicitly or implicitly converted to.

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

#### String

#### String

#### Boolean

#### Long

#### Integer

#### Byte

#### Double

#### Single

#### Currency

#### smalldatetime

#### Variant

#### Visual Basic data type

#### Long

#### Integer

#### Byte

#### Boolean

#### Object

#### Double

#### Single

#### Currency

#### String

#### String

data type

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

data type

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

data type

One-dimensional

array with more than 8,000 bytes

OLE Automation Stored Procedures (Transact-SQL)

CAST and CONVERT (Transact-SQL)

Data Types (Transact-SQL)

COLLATE (Transact-SQL)
