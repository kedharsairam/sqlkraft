---
name: "xquery-context-functions-last"
title: "XQuery - Context Functions - last"
category: "xquery"
description: ""
syntax: "[ ]"
tags:
  - "xquery"
  - "context-functions-last"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Returns the number of items in the sequence that is currently being processed. Specifically, it

returns the integer index of the last item in the sequence. The first item in the sequence has an

index value of 1.

In SQL Server,

can only be used in the context of a context-dependent predicate.

Specifically, it can only be used inside brackets (

).

This topic provides XQuery examples against XML instances that are stored in various

type

columns in the AdventureWorks database.

The following query retrieves the last two manufacturing steps for a specific product model.

The value, the number of manufacturing steps, returned by the

function is used in this

query to retrieve the last two manufacturing steps.

```sql
[ ]
fn:last() as xs:integer
SELECT ProductModelID, Instructions.query('
declare namespace AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
<LastTwoManuSteps>
<Last-1Step>
{ (/AWMI:root/AWMI:Location)[1]/AWMI:step[(last()-1)]/text() }
</Last-1Step>
```
