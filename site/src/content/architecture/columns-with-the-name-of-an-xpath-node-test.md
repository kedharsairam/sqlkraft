---
title: "Columns with the Name of an XPath Node Test"
topic: "xml-data"
description: ""
tags: ["xml-data","columns-with-the-name-of-an-xpath-node-test"]
pubDate: "2025-12-01"
---

If the column name is one of the XPath node tests, the content is mapped as shown in the

following table. When the column name is an XPath node test, the content is mapped to the

corresponding node. If the SQL type of the column is

, an error is returned.

text()

For a column with the name of text(), the string value in that column is added as

a text node.

comment()

For a column with the name of comment(), the string value in that column is

added as an XML comment.

node()

For a column with the name of node(), the result is the same as when the

column name is a wildcard character (

).

processing-

instruction(name)

For a column with the name of a processing instruction, the string value in that

column is added as the PI value for the processing instruction target name.

The following query shows the use of the node tests as column names. It adds text nodes and

comments in the resulting XML.

ﾉ

Expand table

```sql
*
USE
AdventureWorks2022;
GO
SELECT
E.BusinessEntityID
"@EmpID"
,
'Example of using node tests such as text(), comment(), processing-
instruction()'
as
"comment()"
,
'Some PI'
as
"processing-instruction(PI)"
,
'Employee name and address data'
as
"text()"
,
'middle name is optional'
as
"EmpName/text()"
,
FirstName as
"EmpName/First"
,
MiddleName as
"EmpName/Middle"
,
LastName as
"EmpName/Last"
,
AddressLine1 as
"Address/AddrLine1"
,
AddressLine2 as
"Address/AddrLIne2"
,
City as
"Address/City"
FROM
HumanResources.Employee
AS
E
INNER
JOIN
Person.Person
AS
P
ON
P.BusinessEntityID = E.BusinessEntityID
```
