---
name: "xquery-functions-on-sequences-id"
title: "XQuery - Functions on Sequences - id"
category: "xquery"
description: ""
syntax: "AdventureWorks2022"
tags:
  - "xquery"
  - "functions-on-sequences-id"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the sequence of element nodes with xs:ID values that match the values of one or more

of the xs:IDREF values supplied in

$arg

.

$arg

One or more xs:IDREF values.

The result of the function is a sequence of elements in the XML instance, in document order,

that has an xs:ID value equal to one or more of the xs:IDREFs in the list of candidate xs:IDREFs.

If the xs:IDREF value does not match any element, the function returns the empty sequence.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the

database.

The following example uses fn:id to retrieve the <

> elements, based on the IDREF

manager attribute. In this example, the manager attribute is an IDREF type attribute and the eid

attribute is an ID type attribute.

For a specific manager attribute value, the

function finds the <

> element whose

ID type attribute value matches the input IDREF value. In other words, for a specific employee,

```sql
AdventureWorks2022 employee employee fn:id($arg as xs:IDREF*) as element()*
```
