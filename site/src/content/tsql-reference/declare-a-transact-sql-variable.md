---
name: "Declare a Transact-SQL variable"
title: "Declare a Transact-SQL variable"
category: "language-elements"
description: ""
tags: ["tsql","language-elements"]
pubDate: 2026-05-29
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

A Transact-SQL local variable is an object that can hold a single data value of a specific type.

You typically use variables in batches and scripts for the following purposes:

Use a variable as a counter to count the number of times a loop is performed, or to

control how many times the loop is performed.

Hold a data value to test by a control-of-flow statement.

Save a data value to return by a stored procedure return code or function return value.

The code samples in this article use the

or

sample

database, which you can download from the

Microsoft SQL Server Samples and Community

Projects

home page.

The names of some Transact-SQL system functions begin with two

at

signs (

). Although

earlier versions of SQL Server refer to the

functions as global variables,

functions aren't

variables, and they don't have the same behaviors as variables. The

functions are system

functions, and their syntax usage follows the rules for functions.

You can't use variables in a view.

Changes to variables aren't affected by the rollback of a transaction.

Use the

statement to initialize a Transact-SQL variable by:

Assigning a name. The name must start with a single

character.

Assigning a system-supplied or user-defined data type and a length. For numeric

variables, you can assign a precision and optional scale. For variables of type XML, you

can optionally assign a schema collection.

Setting the value to.

For example, the following

statement creates a local variable named

with

an

data type. By default, the value for this variable is.

`AdventureWorks2025`

`AdventureWorksDW2025`

```sql
@@
```

```sql
@@
```

```sql
@@
```

```sql
@@
```

`DECLARE`

```sql
@
```

`NULL`

`DECLARE`

```sql
@mycounter
```

`NULL`
