---
name: "xquery-xquery-extension-functions-sqlvariable"
title: "XQuery - XQuery Extension Functions - sql:variable()"
category: "xquery"
description: "XQuery Language Reference: XQuery Extension Functions - sql:variable()"
syntax: "ProductID"
tags: ["xquery","xquery-extension-functions-sqlvariable"]
pubDate: 2025-12-01
---

Exposes a variable that contains a SQL relational value inside an XQuery expression.

As described in the topic

Binding Relational Data Inside XML

, you can use this function when

you use

XML data type methods

to expose a relational value inside XQuery.

For example, the

query() method

is used to specify a query against an XML instance that is

stored in an

data type variable or column. Sometimes, you might also want your query to

use values from a Transact-SQL variable, or parameter, to bring relational and XML data

together. To do this, you use the

sql:variable

function.

The SQL value will be mapped to a corresponding XQuery value and its type will be an XQuery

base type that is equivalent to the corresponding SQL type.

You can only refer to an

instance in the context of the source expression of an XML-DML

insert statement; otherwise you cannot refer to values that are of type

or a common

language runtime (CLR) user-defined type.

The following example constructs an XML instance that made up of the following:

A value (

) from a non-XML column. The

sql:column() function

is used to bind

this value in the XML.

```sql
ProductID sql:variable("variableName") as xdt:anyAtomicType?
```
