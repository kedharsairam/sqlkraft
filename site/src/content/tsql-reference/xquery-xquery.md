---
name: "xquery-xquery"
title: "XQuery - xQuery"
category: "xquery"
description: "XQuery Language Reference: xQuery"
syntax: |
  DECLARE
    @x
    xml
    SET
    @x =
    '<ROOT><a>111</a></ROOT>'
    SELECT
    @x.query(
    '/ROOT/a'
    )
    SELECT
    Instructions.query(
    'declare namespace
    AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
    works/ProductModelManuInstructions";
    /AWMI:root/AWMI:Location[@LocationID=10]
tags: ["xquery","xquery"]
pubDate: "2025-12-01"
---

Transact-SQL supports a subset of the XQuery language that is used for querying the

data

type. This XQuery implementation is aligned with the July 2004 Working Draft of XQuery. The

language is under development by the World Wide Web Consortium (W3C), with the

participation of all major database vendors and also Microsoft. Because the W3C specifications

may undergo future revisions before becoming a W3C recommendation, this implementation

may be different from the final recommendation. This topic outlines the semantics and syntax

of the subset of XQuery that is supported in SQL Server.

For more information, see the

W3C XQuery 1.0 Language Specification.

XQuery is a language that can query structured or semi-structured XML data. With the

data type support provided in the Database Engine, documents can be stored in a database

and then queried by using XQuery.

XQuery is based on the existing XPath query language, with support added for better iteration,

better sorting results, and the ability to construct the necessary XML. XQuery operates on the

XQuery Data Model. This is an abstraction of XML documents, and the XQuery results that can

be typed or untyped. The type information is based on the types provided by the W3C XML

Schema language. If no typing information is available, XQuery handles the data as untyped.

This is similar to how XPath version 1.0 handles XML.

To query an XML instance stored in a variable or column of

type, you use the

xml Data

Type Methods. For example, you can declare a variable of

type and query it by using the

method of the

data type.

In the following example, the query is specified against the Instructions column of

type in

ProductModel table in the AdventureWorks database.

```sql
DECLARE
@x xml
SET
@x =
'<ROOT><a>111</a></ROOT>'
SELECT
@x.query(
'/ROOT/a'
)
SELECT
Instructions.query(
'declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
/AWMI:root/AWMI:Location[@LocationID=10]
```
