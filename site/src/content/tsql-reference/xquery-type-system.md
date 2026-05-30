---
name: "xquery-type-system"
title: "XQuery - Type System"
category: "xquery"
description: "XQuery Language Reference: Type System"
syntax: "Instructions"
tags:
  - "xquery"
  - "type-system"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

XQuery is a strongly-typed language for schema types and a weakly-typed language for

untyped data. The predefined types of XQuery include the following:

Built-in types of XML schema in the

namespace.

Types defined in the

namespace.

This topic also describes the following:

The typed value versus the string value of a node.

The

data Function (XQuery)

and the

string Function (XQuery)

.

Matching the sequence type returned by an expression.

The built-in types of XML schema have a predefined namespace prefix of xs. Some of these

types include

and

. All these built-in types are supported. You can use these

types when you create an XML schema collection.

When querying typed XML, the static and dynamic type of the nodes is determined by the XML

schema collection associated with the column or variable that is being queried. For more

information about static and dynamic types, see

Expression Context and Query Evaluation

(XQuery)

. For example, the following query is specified against a typed

column

(

). The expression uses

to verify that the typed value of the

attribute returned is of

type.

```sql
Instructions instance of
LotSize xs:decimal
SELECT Instructions.query('
DECLARE namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
data(/AWMI:root[1]/AWMI:Location[@LocationID=10][1]/@LotSize)[1] instance of xs:decimal
') AS Result
FROM Production.ProductModel
WHERE ProductModelID=7
```
