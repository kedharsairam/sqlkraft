---
name: "xquery-flwor-statement-iteration"
title: "XQuery - FLWOR Statement & Iteration"
category: "xquery"
description: "XQuery Language Reference: FLWOR Statement & Iteration"
syntax: "for"
tags:
  - "xquery"
  - "flwor-statement-iteration"
pubDate: 2025-12-01
---

09/29/2025

SQL Server

XQuery defines the FLWOR iteration syntax. FLWOR is the acronym for

,

,

,

, and.

A FLWOR statement is made up of the following parts:

One or more

clauses that bind one or more iterator variables to input sequences.

Input sequences can be other XQuery expressions such as XPath expressions. They're

either sequences of nodes or sequences of atomic values. Atomic value sequences can be

constructed using literals or constructor functions. Constructed XML nodes aren't allowed

as input sequences in SQL Server.

An optional

clause. This clause assigns a value to the given variable for a specific

iteration. The assigned expression can be an XQuery expression such as an XPath

expression, and can return either a sequence of nodes or a sequence of atomic values.

Atomic value sequences can be constructed by using literals or constructor functions.

Constructed XML nodes aren't allowed as input sequences in SQL Server.

An iterator variable. This variable can have an optional type assertion by using the

keyword.

An optional

clause. This clause applies a filter predicate on the iteration.

An optional

clause.

A

expression. The expression in the

clause constructs the result of the

FLWOR statement.

For example, the following query iterates over the <

> elements at the first manufacturing

location and returns the string value of the <

> nodes:

```sql
for let where order by return
FOR let as where order by return return
Step
Step
DECLARE
@x
AS
XML
;
SET
@x =
'<ManuInstructions ProductModelID="1" ProductModelName="SomeBike" >
<Location LocationID="L1" >
<Step>Manu step 1 at Loc 1</Step>
<Step>Manu step 2 at Loc 1</Step>
<Step>Manu step 3 at Loc 1</Step>
```
