---
title: 'Forced parameterization'
topic: 'io-fundamentals'
description: 'When processing complex Transact-SQL statements, the relational engine can have difficulty'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

SQL

When processing complex Transact-SQL statements, the relational engine can have difficulty

determining which expressions can be parameterized. To increase the ability of the relational

engine to match complex Transact-SQL statements to existing, unused execution plans,

explicitly specify the parameters using either

or parameter markers.

Under the default behavior of simple parameterization, SQL Server parameterizes a relatively

small class of queries. However, you can specify that all queries in a database be

parameterized, subject to certain limitations, by setting the

option of the

command to

. Doing so can improve the performance of databases that

experience high volumes of concurrent queries by reducing the frequency of query

compilations.

Alternatively, you can specify that a single query, and any others that are syntactically

equivalent but differ only in their parameter values, be parameterized.

You can override the default simple parameterization behavior of SQL Server by specifying that

all

,

,

, and

statements in a database be parameterized, subject to

７

Note

When the

,

,

,

, or

arithmetic operators are used to perform implicit or explicit

conversion of int, smallint, tinyint, or bigint constant values to the float, real, decimal or

numeric data types, SQL Server applies specific rules to calculate the type and precision of

the expression results. However, these rules differ, depending on whether the query is

parameterized or not. Therefore, similar expressions in queries can, in some cases,

produce differing results.



Tip

When using an Object-Relational Mapping (ORM) solution such as Entity Framework (EF),

application queries like manual LINQ query trees or certain raw SQL queries might not be

parameterized, which impacts plan re-use and the ability to track queries in the Query

Store. For more information, see

and

.

certain limitations. Forced parameterization is enabled by setting the

option

to

in the

statement. Forced parameterization might improve the

performance of certain databases by reducing the frequency of query compilations and

recompilations. Databases that might benefit from forced parameterization are generally those

that experience high volumes of concurrent queries from sources such as point-of-sale

applications.

When the

option is set to

, any literal value that appears in a

,

,

, or

statement, submitted in any form, is converted to a parameter

during query compilation. The exceptions are literals that appear in the following query

constructs:

statements.

Statements inside the bodies of stored procedures, triggers, or user-defined functions.

SQL Server already reuses query plans for these routines.

Prepared statements that have already been parameterized on the client-side application.

Statements that contain XQuery method calls, where the method appears in a context

where its arguments would typically be parameterized, such as a

clause. If the

method appears in a context where its arguments wouldn't be parameterized, the rest of

the statement is parameterized.

Statements inside a Transact-SQL cursor. (

statements inside API cursors are

parameterized.)

Deprecated query constructs.

Any statement that is run in the context of

or

set to

.

Statements that contain more than 2,097 literals that are eligible for parameterization.

Statements that reference variables, such as

.

Statements that contain the

query hint.

Statements that contain a

clause.

Statements that contain a

clause.

Additionally, the following query clauses aren't parameterized. In these cases, only the clauses

aren't parameterized. Other clauses within the same query can be eligible for forced

parameterization.

The <select_list> of any

statement. This includes

lists of subqueries and

lists inside

statements.

Subquery

statements that appear inside an

statement.

The

,

,

,

,

,

, or

clauses of

a query.


## Arguments, either direct or as subexpressions, to
,

,

,

, or any

operator.

The pattern and escape_character arguments of a

clause.

The style argument of a

clause.

Integer constants inside an

clause.

Constants specified by using ODBC extension syntax.

Constant-foldable expressions that are arguments of the

,

,

,

, and

operators.

When considering eligibility for forced parameterization, SQL Server considers an

expression to be constant-foldable when either of the following conditions is true:

No columns, variables, or subqueries appear in the expression.

The expression contains a

clause.


## Arguments to query hint clauses. These include the
number_of_rows

argument of the

query hint, the

number_of_processors

argument of the

query hint, and the

number

argument of the

query hint.

Parameterization occurs at the level of individual Transact-SQL statements. In other words,

individual statements in a batch are parameterized. After compiling, a parameterized query is

executed in the context of the batch in which it was originally submitted. If an execution plan

for a query is cached, you can determine whether the query was parameterized by referencing

the sql column of the

dynamic management view. If a query is

parameterized, the names and data types of parameters come before the text of the submitted

batch in this column, such as (@1 tinyint).

When SQL Server parameterizes literals, the parameters are converted to the following data

types:

Integer literals whose size would otherwise fit within the int data type parameterize to int.

Larger integer literals that are parts of predicates that involve any comparison operator

(includes

,

,

,

,

,

,

,

,

,

,

,

,

, and

) parameterize

to numeric(38,0). Larger literals that aren't parts of predicates that involve comparison

operators parameterize to numeric whose precision is just large enough to support its

size and whose scale is 0.

７

Note

Parameter names are arbitrary. Users or applications should not rely on a particular

naming order. Also, the following can change between versions of SQL Server and Service

Pack upgrades: Parameter names, the choice of literals that are parameterized, and the

spacing in the parameterized text.

```sql
sp_executesql
```

```sql
PARAMETERIZATION
```

```sql
ALTER DATABASE
```

```sql
FORCED
```

```sql
SELECT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
SELECT
*
FROM
AdventureWorks2022.Production.Product
WHERE
ProductSubcategoryID = 4;
```

```sql
+
```

```sql
-
```

```sql
*
```

```sql
/
```

```sql
%
```

```sql
PARAMETERIZATION
```

```sql
FORCED
```

```sql
ALTER DATABASE
```

```sql
PARAMETERIZATION
```

```sql
FORCED
```

```sql
SELECT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
INSERT...EXECUTE
```

```sql
WHERE
```

```sql
SELECT
```

```sql
ANSI_PADDING
```

```sql
ANSI_NULLS
```

```sql
OFF
```

```sql
WHERE T.col2 >= @bb
```

```sql
RECOMPILE
```

```sql
COMPUTE
```

```sql
WHERE CURRENT OF
```

```sql
SELECT
```

```sql
SELECT
```

```sql
SELECT
```

```sql
INSERT
```

```sql
SELECT
```

```sql
IF
```

```sql
TOP
```

```sql
TABLESAMPLE
```

```sql
HAVING
```

```sql
GROUP BY
```

```sql
ORDER BY
```

```sql
OUTPUT...INTO
```

```sql
FOR XML
```

```sql
OPENROWSET
```

```sql
OPENQUERY
```

```sql
OPENDATASOURCE
```

```sql
OPENXML
```

```sql
FULLTEXT
```

```sql
LIKE
```

```sql
CONVERT
```

```sql
IDENTITY
```

```sql
+
```

```sql
-
```

```sql
*
```

```sql
/
```

```sql
%
```

```sql
CASE
```

```sql
FAST
```

```sql
MAXDOP
```

```sql
MAXRECURSION
```

```sql
sys.syscacheobjects
```

```sql
<
```

```sql
<=
```

```sql
=
```

```sql
!=
```

```sql
>
```

```sql
>=
```

```sql
!<
```

```sql
!>
```

```sql
<>
```

```sql
ALL
```

```sql
ANY
```

```sql
SOME
```

```sql
BETWEEN
```

```sql
IN
```
