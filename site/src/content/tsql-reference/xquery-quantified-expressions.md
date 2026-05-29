---
name: "xquery-quantified-expressions"
title: "XQuery - Quantified Expressions"
category: "xquery"
description: "XQuery Language Reference: Quantified Expressions"
syntax: "satisfies"
tags:
  - "xquery"
  - "quantified-expressions"
pubDate: 2025-12-01
---

Article

•

04/03/2023

Applies to:

SQL Server

Existential and universal quantifiers specify different semantics for Boolean operators that are

applied to two sequences. This is shown in the following table.

Existential quantifier

Given two sequences, if any item in the first sequence has a match in the second sequence,

based on the comparison operator that is used, the returned value is True.

Universal quantifier

Given two sequences, if every item in the first sequence has a match in the second sequence,

the returned value is True.

XQuery supports quantified expressions in the following form:

You can use these expressions in a query to explicitly apply either existential or universal

quantification to an expression over one or several sequences. In SQL Server, the expression in

the

clause has to result in one of the following: a node sequence, an empty

sequence, or a Boolean value. The effective Boolean value of the result of that expression will

be used in the quantification. The existential quantification that uses

will return True if at

least one of the values bound by the quantifier has a True result in the satisfy expression. The

universal quantification that uses

must have True for all values bound by the quantifier.

For example, the following query checks every <Location> element to see whether it has a

LocationID attribute.

```sql
satisfies
( some | every ) <variable> in <Expression> (,...) satisfies <Expression>
SELECT Instructions.query('
declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
if (every $WC in //AWMI:root/AWMI:Location
satisfies $WC/@LocationID)
then
<Result>All work centers have workcenterLocation ID</Result>
else
<Result>Not all work centers have workcenterLocation ID</Result>
') as Result
```