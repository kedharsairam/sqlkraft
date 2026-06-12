---
title: "Table-Valued Parameters"
topic: "tables"
description: "Table-valued parameters are declared by using user-defined table types. You can use table- v"
tags: ["tables","table-valued-parameters"]
pubDate: 2025-12-01
---

Table-valued parameters are declared by using user-defined table types. You can use table-

valued parameters to send multiple rows of data to a Transact-SQL statement or a routine, such

as a stored procedure or function, without creating a temporary table or many parameters.

Table-valued parameters are like parameter arrays in OLE DB and ODBC, but offer more

flexibility and closer integration with Transact-SQL. Table-valued parameters also have the

benefit of being able to participate in set-based operations.

Transact-SQL passes table-valued parameters to routines by reference to avoid making a copy

of the input data. You can create and execute Transact-SQL routines with table-valued

parameters, and call them from Transact-SQL code, managed and native clients in any

managed language.

A table-valued parameter is scoped to the stored procedure, function, or dynamic Transact-SQL

text, exactly like other parameters. Similarly, a variable of table type has scope like any other

local variable that is created by using a DECLARE statement. You can declare table-valued

variables within dynamic Transact-SQL statements and pass these variables as table-valued

parameters to stored procedures and functions.

Table-valued parameters offer more flexibility and in some cases better performance than

temporary tables or other ways to pass a list of parameters. Table-valued parameters offer the

following benefits:

Do not acquire locks for the initial population of data from a client.

Provide a simple programming model.

Enable you to include complex business logic in a single routine.

Reduce round trips to the server.

Can have a table structure of different cardinality.

Are strongly typed.

Enable the client to specify sort order and unique keys.

Are cached like a temp table when used in a stored procedure. Starting with SQL Server

2012 (11.x) and later versions, table-valued parameters are also cached for parameterized

queries.
