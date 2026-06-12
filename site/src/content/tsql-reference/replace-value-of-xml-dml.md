---
name: "replace value of (XML DML)"
title: "Replace value of (XML DML)"
category: "statements"
description: "Note the following from the previous query:"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Note the following from the previous query:

The

modify() Method (xml Data Type)

is used to specify the

XML DML keyword.

The

query() Method (xml Data Type)

is used to query the document.

This example deletes nodes from a manufacturing instructions XML document stored in a

typed

column.

In the example, you first create a table (T) with a typed

column in the AdventureWorks

database. You then copy a manufacturing instructions XML instance from the Instructions

column in the ProductModel table into table T and delete one or more nodes from the

document.

Compare Typed XML to Untyped XML

Create Instances of XML Data

xml Data Type Methods

XML Data Modification Language (XML DML)

See Also

```sql
-- delete the second feature
UPDATE
T
SET x.modify(
'delete /Root/ProductDescription/Features/*[2]'
)
-- verify the deletion
SELECT x.query(
' //ProductDescription/Features'
)
FROM
T
```

```sql
USE
AdventureWorks2022;
GO
DROP
TABLE
T
GO
CREATE
TABLE
T(
ProductModelID
INT
PRIMARY
KEY
,
Instructions
XML (Production.ManuInstructionsSchemaCollection))
GO
INSERT
T
SELECT
ProductModelID, Instructions
FROM
Production.ProductModel
WHERE
ProductModelID = 7
GO
SELECT
Instructions
FROM
T
--1) insert <Location 1000/>.
Note:
<Root> must be singleton in the query
UPDATE
T
SET
Instructions.modify(
'
DECLARE namespace MI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
INSERT <MI:Location LocationID="1000" LaborHours="1000" >
These are manu steps at location 1000.
<MI:step>New step1 instructions</MI:step>
Instructions for step 2 are here
<MI:step>New step 2 instructions</MI:step>
```

```sql
</MI:Location>
AS first
INTO (/MI:root)[1]
'
)
GO
SELECT
Instructions
FROM
T
-- delete an attribute
UPDATE
T
SET
Instructions.modify(
'
declare namespace MI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
delete(/MI:root/MI:Location[@LocationID=1000]/@LaborHours)
'
)
GO
SELECT
Instructions
FROM
T
-- delete text in <location>
UPDATE
T
SET
Instructions.modify(
'
declare namespace MI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
delete(/MI:root/MI:Location[@LocationID=1000]/text())
'
)
GO
SET
Instructions
FROM
T
-- delete 2nd manu step at location 1000
UPDATE
T
SET
Instructions.modify(
'
declare namespace MI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
delete(/MI:root/MI:Location[@LocationID=1000]/MI:step[2])
'
)
GO
SELECT
Instructions
FROM
T
-- cleanup
DROP
TABLE
T
GO
```
