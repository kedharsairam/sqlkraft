---
title: "Manipulating UDT data"
topic: "clr-integration"
description: "Transact-SQL provides no specialized syntax for , , or statements when modifying data in user-defined type (UDT) columns."
tags: ["clr-integration","manipulating-udt-data"]
pubDate: "2025-12-01"
---

Transact-SQL provides no specialized syntax for

,

, or

statements when

modifying data in user-defined type (UDT) columns. The Transact-SQL

or

functions are used to cast native data types to the UDT type.

The following Transact-SQL statements insert three rows of sample data into the

table.

The

data type consists of X and Y integer values that are exposed as properties of the

UDT. You must use either the

or

function to cast the comma-delimited X and Y

values to the

type. The first two statements use the

function to convert a string

value to the

type, and the third statement uses the

function:

The following

statement selects the binary value of the UDT.

To see the output displayed in a readable format, call the

method of the

UDT,

which converts the value to its string representation.

```sql
INSERT
UPDATE
DELETE
CAST
CONVERT
Points
Point
CAST
CONVERT
Point
CONVERT
Point
CAST
SELECT
ToString
Point
INSERT
INTO dbo.Points (PointValue)
VALUES (
CONVERT (Point,
'3,4'
));
INSERT
INTO dbo.Points (PointValue)
VALUES (
CONVERT (Point,
'1,5'
));
INSERT
INTO dbo.Points (PointValue)
VALUES (
CAST (
'1,99'
AS
Point));
SELECT
ID
, PointValue
FROM dbo.Points;
```
