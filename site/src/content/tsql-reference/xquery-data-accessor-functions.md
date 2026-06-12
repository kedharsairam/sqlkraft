---
name: "xquery-data-accessor-functions"
title: "XQuery - Data Accessor Functions"
category: "xquery"
description: "XQuery Language Reference: Data Accessor Functions"
tags:
  - "xquery"
  - "data-accessor-functions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

SQL Server

The topics in this section discuss and provide sample code for the data-accessor functions.

XQuery has a function

to extract scalar, typed values from nodes, a node test

to

return text nodes, and the function

that returns the string value of a node. Their use

can be confusing. The following are guidelines for using them correctly in SQL Server. The XML

instance <age>12</age> is used for the purpose of illustration.

Untyped XML: The path expression /age/text() returns the text node "12". The function

fn:data(/age) returns the string value "12" and so does fn:string(/age).

Typed XML: The expression /age/text() returns a static error for any simple typed <age>

element. On the other hand, fn:data(/age) returns integer 12. The fn:string(/age) yields the

string "12".

string Function (XQuery)

data Function (XQuery)

Path Expressions (XQuery)
