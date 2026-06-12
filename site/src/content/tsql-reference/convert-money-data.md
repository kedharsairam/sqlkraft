---
name: "Convert money data"
title: "Convert money data"
category: "data-types"
description: "You don't need to enclose currency or monetary data in single quotation marks ("
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

￥

Full-width Yen sign

￦

Full-width Won sign

You don't need to enclose currency or monetary data in single quotation marks (

). While you

can specify monetary values preceded by a currency symbol, SQL Server doesn't store any

currency information associated with the symbol, it only stores the numeric value.

When you convert to

from integer data types, units are assumed to be in monetary

units. For example, the integer value of

is converted to the

equivalent of 4 monetary

units.

The following example converts

and

values to

and

data

types, respectively.

Here's the result set. Because the

type in the example doesn't have a

scale

, the value is

truncated.

Output

２

Warning

You can experience rounding errors through truncation, when storing monetary values as

and. Avoid using this data type if your money or currency values are

used in calculations. Instead, use the

data type with at least four decimal places.

ALTER TABLE (Transact-SQL)

CAST and CONVERT (Transact-SQL)

CREATE TABLE (Transact-SQL)

Data types (Transact-SQL)

DECLARE @local_variable (Transact-SQL)

SET @local_variable (Transact-SQL)

sys.types (Transact-SQL)
