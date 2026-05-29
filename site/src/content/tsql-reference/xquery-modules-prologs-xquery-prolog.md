---
name: "xquery-modules-prologs-xquery-prolog"
title: "XQuery - Modules & Prologs - XQuery Prolog"
category: "xquery"
description: "XQuery Language Reference: Modules & Prologs - XQuery Prolog"
syntax: "10"
tags:
  - "xquery"
  - "modules-prologs-xquery-prolog"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

An XQuery query is made up of a prolog and a body. The XQuery prolog is a series of

declarations and definitions that together create the required environment for query

processing. In SQL Server, the XQuery prolog can include namespace declarations. The XQuery

body is made up of a sequence of expressions that specify the intended query result.

For example, the following XQuery is specified against the Instructions column of

type that

stores manufacturing instructions as XML. The query retrieves the manufacturing instructions

for the work center location

. The

method of the

data type is used to specify

the XQuery.

Note the following from the previous query:

The XQuery prolog includes a namespace prefix (AWMI) declaration,

.

The

keyword defines a namespace prefix that is used later in the query

body.

is the query body.

A namespace declaration defines a prefix and associates it with a namespace URI, as shown in

the following query. In the query,

is an

type column.

In specifying XQuery against this column, the query prolog specifies the

declaration to associate the prefix

, product description, with the namespace URI. This prefix

```sql
10
query()
(namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
declare namespace
/AWMI:root/AWMI:Location[@LocationID="10"]
CatalogDescription
declare namespace
PD
SELECT Instructions.query('declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
/AWMI:root/AWMI:Location[@LocationID=10]
') AS Result
FROM  Production.ProductModel
WHERE ProductModelID=7
```
