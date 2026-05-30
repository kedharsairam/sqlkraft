---
name: "xquery-atomization"
title: "XQuery - Atomization"
category: "xquery"
description: "XQuery Language Reference: Atomization"
syntax: "LaborHours"
tags:
  - "xquery"
  - "atomization"
pubDate: 2025-12-01
---

09/29/2025

Applies to:

SQL Server

Atomization is the process of extracting the typed value of an item. This process is implied

under certain circumstances. Some of the XQuery operators, such as arithmetic and

comparison operators, depend on this process. For example, when you apply arithmetic

operators directly to nodes, the typed value of a node is first retrieved by implicitly invoking

the

data function

. This passes the atomic value as an operand to the arithmetic operator.

For example, the following query returns the total of the

attributes. In this case,

is implicitly applied to the attribute nodes.

Although not required, you can also explicitly specify the

function:

Another example of implicit atomization is when you use arithmetic operators. The

operator

requires atomic values, and

is implicitly applied to retrieve the atomic value of the

attribute. The query is specified against the Instructions column of the

type in

the ProductModel table. The following query returns the

attribute three times. In

the query, consider:

In constructing the

attribute, atomization is implicitly applied to the

singleton sequence returned by

. The typed value of the

attribute is assigned to

.

```sql
LaborHours data() data()
+
data()
LaborHours
LaborHours
OriginalLaborHours
$WC/@LaborHours
LaborHours
OriginalLaborHours
DECLARE
@x
AS
XML
;
SET
@x =
'<ROOT><Location LID="1" SetupTime="1.1" LaborHours="3.3" />
<Location LID="2" SetupTime="1.0" LaborHours="5" />
<Location LID="3" SetupTime="2.1" LaborHours="4" />
</ROOT>'
;
-- data() implicitly applied to the attribute node sequence.
SELECT
@x.query(
'sum(/ROOT/Location/@LaborHours)'
);
SELECT
@x.query(
'sum(data(ROOT/Location/@LaborHours))'
);
```
