---
title: "Prepare SQL statements"
topic: "query-processing"
description: "equivalent but differ only in their parameter values. Conversely, you can specify that forced"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

equivalent but differ only in their parameter values. Conversely, you can specify that forced

parameterization be attempted on only a set of syntactically equivalent queries, even if forced

parameterization is disabled in the database.

Plan guides

are used for this purpose.

The SQL Server relational engine introduces full support for preparing Transact-SQL statements

before they are executed. If an application has to execute an Transact-SQL statement several

times, it can use the database API to do the following:

Prepare the statement once. This compiles the Transact-SQL statement into an execution

plan.

Execute the precompiled execution plan every time it has to execute the statement. This

prevents having to recompile the Transact-SQL statement on each execution after the first

time. Preparing and executing statements is controlled by API functions and methods. It

isn't part of the Transact-SQL language. The prepare/execute model of executing

Transact-SQL statements is supported by the SQL Server Native Client OLE DB Provider

and the SQL Server Native Client ODBC driver. On a prepare request, either the provider

or the driver sends the statement to SQL Server with a request to prepare the statement.

SQL Server compiles an execution plan and returns a handle for that plan to the provider

or driver. On an execute request, either the provider or the driver sends the server a

request to execute the plan that is associated with the handle.

Prepared statements can't be used to create temporary objects on SQL Server. Prepared

statements can't reference system stored procedures that create temporary objects, such as

temporary tables. These procedures must be executed directly.

Excess use of the prepare/execute model can degrade performance. If a statement is executed

only once, a direct execution requires only one network round-trip to the server. Preparing and

executing an Transact-SQL statement executed only one time requires an extra network round-

trip; one trip to prepare the statement and one trip to execute it.

７

Note

When the

option is set to

, the reporting of error messages can

differ from when the

option is set to

: multiple error messages

might be reported under forced parameterization, where fewer messages would be

reported under simple parameterization, and the line numbers in which errors occur can

be reported incorrectly.

```sql
PARAMETERIZATION
```

```sql
FORCED
```

```sql
PARAMETERIZATION
```

```sql
SIMPLE
```
