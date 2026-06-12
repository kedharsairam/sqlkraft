---
name: "Collation labels"
title: "Collation labels"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

Collation precedence, also known as collation coercion rules, determines the following two

outcomes:

The collation of the final result of an expression that is evaluated to a character string.

The collation that is used by collation-sensitive operators that use character string inputs

but don't return a character string, such as

and IN.

The collation precedence rules apply only to the character string data types:

,

,

,

,

, and. Objects that have other data types don't participate in collation

evaluations.

The following table lists and describes the four categories in which the collations of all objects

are identified. The name of each category is the collation label.

Any Transact-SQL character string variable, parameter, literal, or the output of a catalog

built-in function, or a built-in function that doesn't take string inputs but produces a string

output.

If the object is declared in a user-defined function, stored procedure, or trigger, the object

is assigned the default collation of the database in which the function, stored procedure,

or trigger is created. If the object is declared in a batch, the object is assigned the default

collation of the current database for the connection.

A column reference. The collation of the expression (X) is taken from the collation defined

for the column in the table or view.

Even if the column was explicitly assigned a collation by using a

clause in the

or

statement, the column reference is classified as implicit.

An expression that is explicitly cast to a specific collation (X) by using a

clause in

the expression.

Expand table

#### Collation

#### label

#### Types of objects

`LIKE`

```sql
Coercible-
default
```

```sql
Implicit X
```

`COLLATE`

```sql
CREATE TABLE
```

```sql
CREATE VIEW
```

```sql
Explicit X
```

`COLLATE`
