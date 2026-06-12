---
name: "xquery-xquery-extension-functions-sqlcolumn"
title: "XQuery - XQuery Extension Functions - sql:column()"
category: "xquery"
description: "XQuery Language Reference: XQuery Extension Functions - sql:column()"
syntax: |
  'sql:column("columnName")'
tags: ["xquery","xquery-extension-functions-sqlcolumn"]
pubDate: "2025-12-01"
---

As described in the topic,

Binding Relational Data Inside XML

, you can use the

sql:column(()

function when you use

XML Data Type Methods

to expose a relational value inside XQuery.

For example, the

query() method (XML data type)

is used to specify a query against an XML

instance that is stored in a variable or column of

type. Sometimes, you may also want your

query to use values from another, non-XML column, to bring relational and XML data together.

To do this, you use the

sql:column()

function.

The SQL value will be mapped to a corresponding XQuery value and its type will be an XQuery

base type that is equivalent to the corresponding SQL type.

Note that reference to a column specified in the

sql:column()

function inside an XQuery refers

to a column in the row that is being processed.

In SQL Server, you can only refer to an

instance in the context of the source expression of

an XML-DML insert statement; otherwise, you cannot refer to columns that are of type

or a

CLR user-defined type.

The

sql:column()

function is not supported in JOIN operations. The APPLY operation can be

used instead.

```sql
sql:column("columnName")
```
