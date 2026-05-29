---
name: "xquery-functions-related-to-qnames-local-name-from-qname"
title: "XQuery - Functions Related to QNames - local-name-from-QName"
category: "xquery"
description: "XQuery Language Reference: Functions Related to QNames - local-name-from-QName"
syntax: "AdventureWorks2022"
tags:
  - "xquery"
  - "functions-related-to-qnames-local-name-from-qname"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns an xs:NCNAME that represents the local part of QName specified by

$arg

. The result is

an empty sequence if

$arg

is the empty sequence.

$arg

Is the QName that the local name should be extracted from.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the

database.

The following example uses the

function to retrieve the local name

and namespace URI parts from a QName type value. The example performs the following:

Creates an XML schema collection.

Creates a table with an xml type column. The xml type is typed using the XML schema

collection.

Stores a sample XML instance in the table. Using the

method of the xml data

type, the query expression is executed to retrieve the local name part of the QName type

value from the instance.

SQL

```sql
AdventureWorks2022
fn:local-name-from-QName($arg as xs:QName?) as xs:NCName?
DROP
TABLE
T
go
```
