---
name: "Implicit conversions"
title: "Implicit conversions"
category: "statements"
description: "Translates ASCII characters to binary bytes, or binary bytes to ASCII characters. Each character"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Microsoft Download Center

(default)

Translates ASCII characters to binary bytes, or binary bytes to ASCII characters. Each character

or byte is converted 1:1.

For a binary

data_type

, the characters 0x are added to the left of the result.

,

For a binary

data_type

, the expression must be a character expression. The

expression

must

have an

even

number of hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, a, b, c, d, e,

f). If the

style

is set to 1, the expression must have 0x as the first two characters. If the

expression contains an odd number of characters, or if any of the characters is invalid, an error

is raised.

If the length of the converted expression exceeds the length of the

data_type

, the result is

right truncated.

Fixed length

data_type

s larger than the converted result has zeros added to the right of the

result.

A

data_type

of type character requires a binary expression. Each binary character is converted

into two hexadecimal characters. Suppose the length of the converted expression exceeds the

length of the

data_type. In that case, it's truncated.

For a fixed size character type

data_type

, if the length of the converted result is less than its

length of the

data_type

, spaces are added to the right of the converted expression to maintain

an even number of hexadecimal digits.

The characters 0x aren't added to the left of the converted result for

style

2.

Implicit conversions don't require specification of either the

function or the

function. Explicit conversions require specification of the

function or the

function. The following illustration shows all explicit and implicit data type conversions allowed

for SQL Server system-supplied data types. These include

, and

sql_variant

, and.

There is no implicit conversion on assignment from the

sql_variant

data type, but there is

implicit conversion to

sql_variant.

Expand table



Tip

The

has this chart available for download as a PNG file.

The above chart illustrates all the explicit and implicit conversions that are allowed in SQL

Server, but the resulting data type of the conversion depends on the operation being

performed:

For explicit conversions, the statement itself determines the resulting data type.

For implicit conversions, assignment statements such as setting the value of a variable or

inserting a value into a column will result in the data type that was defined by the variable

declaration or column definition.

For comparison operators or other expressions, the resulting data type will depend on the

rules of

data type precedence.

## varbinary(max)

## varchar(max)

## nvarchar(max)

## varchar(max)

## effects of data type precedence in conversions

`CAST`

`CONVERT`

`CAST`

`CONVERT`
