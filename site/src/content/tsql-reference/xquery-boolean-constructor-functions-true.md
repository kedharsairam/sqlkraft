---
name: "xquery-boolean-constructor-functions-true"
title: "XQuery - Boolean Constructor Functions - true"
category: "xquery"
description: ""
syntax: 'xs:boolean("1")'
tags:
  - "xquery"
  - "boolean-constructor-functions-true"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Returns the xs:boolean value True. This is equivalent to.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

The following example queries an untyped

variable. The expression in the

method

returns Boolean

if "aaa" is the attribute value. The

method of the

data type

converts the Boolean value into a bit and returns it.

In the following example, the query is specified against a typed

column. The

expression

checks the typed Boolean value of the <

> element and returns the constructed XML,

accordingly. The example performs the following:

Creates an XML schema collection that defines the <

> element of the xs:boolean

type.

```sql
xs:boolean("1") if
ROOT
ROOT fn:true() as xs:boolean
DECLARE @x XML
SET @x= '<ROOT><elem attr="aaa">bbb</elem></ROOT>'
select @x.value(' if ( (/ROOT/elem/@attr)[1] eq "aaa" ) then fn:true() else fn:false() ', 'bit') go
-- result = 1
```
