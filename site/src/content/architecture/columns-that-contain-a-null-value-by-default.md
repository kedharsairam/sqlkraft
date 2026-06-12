---
title: "Columns that Contain a Null Value By Default"
topic: "xml-data"
description: "By default, a null value in a column maps to the absence of the attribute, node, or element."
tags: ["xml-data","columns-that-contain-a-null-value-by-default"]
pubDate: 2025-12-01
---

By default, a null value in a column maps to the absence of the attribute, node, or element. This

default behavior can be overridden by using the ELEMENTS XSINIL keyword phrase. This phrase

requests element-centric XML. This means that null values are explicitly indicated in the

returned results. These elements will have no value.

The ELEMENTS XSINIL phrase is shown in the following Transact-SQL SELECT example.

The following shows the result. If XSINIL isn't specified, the

element will be absent.

XML

Use PATH Mode with FOR XML

```sql
<Middle>
SELECT
EmployeeID as
"@EmpID"
,
FirstName as
"EmpName/First"
,
MiddleName as
"EmpName/Middle"
,
LastName as
"EmpName/Last"
FROM
HumanResources.Employee E, Person.Contact C
WHERE
E.EmployeeID = C.ContactID
AND
E.EmployeeID=1
FOR
XML
PATH
, ELEMENTS XSINIL;
<row xmlns:xsi
=
"http://www.w3.org/2001/XMLSchema-instance"
EmpID
=
"1"
>
<EmpName>
<First>
Gustavo
</First>
<Middle xsi:nil
=
"true"
/>
<Last>
Achong
</Last>
</EmpName>
</row>
```
