---
title: "Computed Columns"
topic: "filestream"
description: "You can define indexes on computed columns as long as the following requirements are met: Ow"
tags: ["filestream","computed-columns"]
pubDate: "2025-12-01"
---

You can define indexes on computed columns as long as the following requirements are met:

Ownership requirements

Determinism requirements

Precision requirements

Data type requirements

SET option requirements

All function references in the computed column must have the same owner as the table.

Expressions are deterministic if they always return the same result for a specified set of inputs.

The

property of the

COLUMNPROPERTY

function reports whether a

computed_column_expression

is deterministic.

The

computed_column_expression

must be deterministic. A

computed_column_expression

is

deterministic when all of the following are true:

All functions that are referenced by the expression are deterministic and precise. These

functions include both user-defined and built-in functions. For more information, see

Deterministic and Nondeterministic Functions. Functions might be imprecise if the

computed column is. For more information, see

Create indexes on persisted

computed columns

late in this article.

All columns that are referenced in the expression come from the table that contains the

computed column.

７

Note

must be

when you are creating or changing indexes on

computed columns or indexed views. For more information, see.

```sql
IsDeterministic
PERSISTED
SET QUOTED_IDENTIFIER
ON
```
