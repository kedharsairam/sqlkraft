---
name: "Pattern match using LIKE"
title: "Pattern match using LIKE"
category: "predicates"
description: "Here's the result set."
tags: ["tsql","predicates"]
pubDate: 2026-05-29
---

Here's the result set.

Output

supports ASCII pattern matching and Unicode pattern matching. When all arguments

(

match_expression

,

pattern

, and

escape_character

, if present) are ASCII character data types,

ASCII pattern matching is performed. If any one of the arguments are of Unicode data type, all

## arguments are converted to Unicode, and Unicode pattern matching is performed. When you

use Unicode data (

or

data types) with

, trailing blanks are significant;

however, for non-Unicode data, trailing blanks aren't significant. Unicode

is compatible

with the ISO standard. ASCII

is compatible with earlier versions of SQL Server.

The following series of examples shows the differences in rows returned between ASCII and

Unicode

pattern matching.

### COLLATE (Transact-

`LIKE`

`LIKE`

`LIKE`

`LIKE`

`LIKE`

```sql
-- Uses AdventureWorks
CREATE
PROCEDURE
FindEmployee @EmpLName
VARCHAR (20)
AS
SELECT
@EmpLName =
RTRIM (@EmpLName) +
'%'
;
SELECT p.FirstName,
p.LastName,
a.City
FROM
Person.Person p
INNER
JOIN
Person.Address a
ON p.BusinessEntityID = a.AddressID
WHERE p.LastName
LIKE
@EmpLName;
GO
EXEC FindEmployee @EmpLName = 'Barb';
GO
FirstName LastName City
---------- -------------------- ---------------
Angela Barbariol Snohomish
David Barber Snohomish (2 row(s) affected)
```

```sql
-- ASCII pattern matching with char column
CREATE
TABLE t (col1
CHAR (30));
INSERT
INTO t
```
