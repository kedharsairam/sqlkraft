---
name: "xquery-functions-on-sequences-empty"
title: "XQuery - Functions on Sequences - empty"
category: "xquery"
description: "XQuery Language Reference: Functions on Sequences - empty"
syntax: "fn:empty($arg as item()*) as xs:boolean"
tags:
  - "xquery"
  - "functions-on-sequences-empty"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns True if the value of

$arg

is an empty sequence. Otherwise, the function returns False.

$arg

A sequence of items. If the sequence is empty, the function returns True. Otherwise, the

function returns False.

The

function is not supported. As an alternative, the

function can be used.

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

In the manufacturing process for Product Model 7, this query returns all the work center

locations that do not have a

attribute.

```sql
fn:empty($arg as item()*) as xs:boolean
SELECT ProductModelID, Instructions.query('
declare namespace AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
for $i in /AWMI:root/AWMI:Location[empty(@MachineHours)]
```