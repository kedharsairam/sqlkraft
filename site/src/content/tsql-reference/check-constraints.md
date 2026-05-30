---
name: "CHECK constraints"
title: "CHECK constraints"
category: "statements"
description: "Columns participating in a foreign key relationship must be defined with the same length"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Columns participating in a foreign key relationship must be defined with the same length

and scale.

A column can have only one DEFAULT definition.

A DEFAULT definition can contain constant values, functions, SQL standard niladic

functions, or

. The following table shows the niladic functions and the values they

return for the default during an INSERT statement.

SQL-92 niladic function

Current date and time.

Name of user performing an insert.

Name of user performing an insert.

Name of user performing an insert.

Name of user performing an insert.

constant_expression

in a DEFAULT definition can't refer to another column in the table, or

to other tables, views, or stored procedures.

DEFAULT definitions can't be created on columns with a

data type or columns

with an IDENTITY property.

DEFAULT definitions can't be created for columns with alias data types if the alias data

type is bound to a default object.

A column can have any number of CHECK constraints, and the condition can include

multiple logical expressions combined with AND and OR. Multiple CHECK constraints for

a column are validated in the order they are created.

The search condition must evaluate to a Boolean expression and can't reference another

table.

Expand table

`NULL`

`CURRENT_TIMESTAMP`

`CURRENT_USER`

`SESSION_USER`

`SYSTEM_USER`

`USER`
