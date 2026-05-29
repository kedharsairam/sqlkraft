---
name: "sys.sp_executesql"
title: "sp_executesql"
category: "general"
description: "A placeholder for the values of extra parameters. Values can only be constants or variables. Values can't be more complex expressions such as functions, or expressions built by using (success) or non-zero (failure). Returns the result sets from all the SQL statements built into the SQL string. parameters must be entered in the specific order as described in the section earlier in this article. If "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "AdventureWorks2025"
---

## Description

A placeholder for the values of extra parameters. Values can only be constants or variables. Values can't be more complex expressions such as functions, or expressions built by using (success) or non-zero (failure). Returns the result sets from all the SQL statements built into the SQL string. parameters must be entered in the specific order as described in the section earlier in this article. If the parameters are entered out of order, an error message has the same behavior as regarding batches, the scope of names, and database context. The Transact-SQL statement or batch in the isn't compiled until the statement is executed. The contents of compiled and executed as an execution plan separate from the execution plan of the batch batch can't reference variables declared in the batch that calls supports the setting of parameter values separately from the Transact-SQL

## Syntax

```sql
AdventureWorks2025
```

## Arguments

Applies to:

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Executes a Transact-SQL statement or batch that can be reused many times, or one that is built

dynamically. The Transact-SQL statement or batch can contain embedded parameters.

Transact-SQL syntax conventions

Syntax for SQL Server, Azure SQL Database, Azure SQL Managed Instance, Azure Synapse

Analytics, and Analytics Platform System (PDW).

The code samples in this article use the

database, which you can download from the

Microsoft SQL Server Samples and Community

Runtime-compiled Transact-SQL statements can expose applications to malicious attacks.

You should parameterize your queries when using

. For more information,

SQL injection

Arguments for extended stored procedures must be entered in the specific order as

described in the

section. If the parameters are entered out of order, an error

message occurs.

## Remarks

A placeholder for the values of extra parameters. Values can only be constants or variables.

Values can't be more complex expressions such as functions, or expressions built by using

(success) or non-zero (failure).

Returns the result sets from all the SQL statements built into the SQL string.

parameters must be entered in the specific order as described in the

section earlier in this article. If the parameters are entered out of order, an error message

has the same behavior as

regarding batches, the scope of names, and

database context. The Transact-SQL statement or batch in the

isn't compiled until the

statement is executed. The contents of

compiled and executed as an execution plan separate from the execution plan of the batch

that called

batch can't reference variables declared in the

batch that calls

. Local cursors or variables in the

batch aren't

visible to the batch that calls

. Changes in database context last only to the end

can be used instead of stored procedures to execute a Transact-SQL statement

many times when the change in parameter values to the statement is the only variation.

Because the Transact-SQL statement itself remains constant and only the parameter values

change, the SQL Server query optimizer is likely to reuse the execution plan it generates for the

first execution. In this scenario, performance is equivalent to that of a stored procedure.

To improve performance, use fully qualified object names in the statement string.

supports the setting of parameter values separately from the Transact-SQL

string, as shown in the following example.

Output parameters can also be used with

. The following example retrieves a job

title from the

table in the

sample database, and

returns it in the output parameter
