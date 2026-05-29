---
name: "Table variables vs temporary tables"
title: "Table variables vs temporary tables"
category: "data-types"
description: "Indexes can't be created explicitly on"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Indexes can't be created explicitly on

variables, and no statistics are kept on

variables. Starting with SQL Server 2014 (12.x), new syntax was introduced which allows you to

create certain index types inline with the table definition. Using this new syntax, you can create

indexes on

variables as part of the table definition. In some cases, performance may

improve by using temporary tables instead, which provide full index support and statistics. For

more information about temporary tables and inline index creation, see

CREATE TABLE

(Transact-SQL)

.

CHECK constraints, DEFAULT values, and computed columns in the

type declaration can't

call user-defined functions. Assignment operation between

variables isn't supported.

Because

variables have limited scope and aren't part of the persistent database,

transaction rollbacks don't affect them. Table variables can't be altered after creation.

Tables variables can't be used as the target of the

clause in a

statement.

You can't use the EXEC statement or the

stored procedure to run a dynamic SQL

Server query that refers a table variable, if the table variable was created outside the EXEC

statement or the

stored procedure. Because table variables can be referenced in

their local scope only, an EXEC statement and a

stored procedure would be

outside the scope of the table variable. However, you can create the table variable and perform

all processing inside the EXEC statement or the

stored procedure because then

the table variables local scope is in the EXEC statement or the

stored procedure.

A table variable isn't a memory-only structure. Because a table variable might hold more data

than can fit in memory, it has to have a place on disk to store data. Table variables are created

in the

database similar to temporary tables. If memory is available, both table variables

and temporary tables are created and processed while in memory (data cache).

Choosing between table variables and temporary tables depends on these factors:

The number of rows that are inserted to the table.

The number of recompilations the query is saved from.

The type of queries and their dependency on indexes and statistics for performance.

In some situations, breaking a stored procedure with temporary tables into smaller stored

procedures so that recompilation takes place on smaller units is helpful.

Database compatibility level 150 improves the performance of table variables with the

introduction of

. For more information, see

.

### table

```sql
INTO
```

```sql
SELECT ... INTO
```

```sql
sp_executesql
```

```sql
sp_executesql
```

```sql
sp_executesql
```

```sql
sp_executesql
```

```sql
sp_executesql
```

```sql
tempdb
```
