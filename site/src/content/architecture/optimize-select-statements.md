---
title: 'Optimize SELECT statements'
topic: 'query-processing'
description: 'You can change the meaning of the query by adding parentheses to force evaluation of the'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

You can change the meaning of the query by adding parentheses to force evaluation of the

first. The following query finds only products under models 20 and 21 that are red.

SQL

Using parentheses, even when they aren't required, can improve the readability of queries, and

reduce the chance of making a subtle mistake because of operator precedence. There is no

significant performance penalty in using parentheses. The following example is more readable

than the original example, although they are syntactically the same.

SQL

A

statement is non-procedural; it doesn't state the exact steps that the database server

should use to retrieve the requested data. This means that the database server must analyze

the statement to determine the most efficient way to extract the requested data. This is

referred to as optimizing the

statement. The component that does this, is called the

Query Optimizer. The input to the Query Optimizer consists of the query, the database schema

(table and index definitions), and the database statistics. The output of the Query Optimizer is a

query execution plan, sometimes referred to as a query plan, or execution plan. The contents of

an execution plan are described in more detail later in this article.

The inputs and outputs of the Query Optimizer during optimization of a single

statement are illustrated in the following diagram:

### The sequence in which the source tables are accessed.

### The methods used to extract data from each table.

### The methods used to compute calculations, and how to filter, aggregate, and sort data

### from each table.

A

statement defines only the following:

The format of the result set. This is specified mostly in the select list. However, other

clauses such as

and

also affect the final form of the result set.

The tables that contain the source data. This is specified in the

clause.

How the tables are logically related for the purposes of the

statement. This is

defined in the join specifications, which might appear in the

clause or in an

clause following

.

The conditions that the rows in the source tables must satisfy to qualify for the

statement. These are specified in the

and

clauses.

A query execution plan is a definition of the following:

Typically, there are many sequences in which the database server can access the base

tables to build the result set. For example, if the

statement references three tables,

the database server could first access

, use the data from

to extract

matching rows from

, and then use the data from

to extract data from

. The other sequences in which the database server could access the tables are:

,

,

, or

,

,

, or

,

,

, or

,

,

Generally, there are different methods for accessing the data in each table. If only a few

rows with specific key values are required, the database server can use an index. If all the

rows in the table are required, the database server can ignore the indexes and perform a

table scan. If all the rows in a table are required but there is an index whose key columns

are in an

, performing an index scan instead of a table scan might save a

separate sort of the result set. If a table is very small, table scans might be the most

efficient method for almost all access to the table.

As data is accessed from tables, there are different methods to perform calculations over

data such as computing scalar values, and to aggregate and sort data as defined in the

query text, for example when using a

or

clause, and how to filter data,

for example when using a

or

clause.

The process of selecting one execution plan from potentially many possible plans is referred to

as optimization. The Query Optimizer is one of the most important components of the

Database Engine. While some overhead is used by the Query Optimizer to analyze the query

and select a plan, this overhead is typically saved several-fold when the Query Optimizer picks

an efficient execution plan. For example, two construction companies can be given identical

blueprints for a house. If one company spends a few days at the beginning to plan how they

will build the house, and the other company begins building without planning, the company

that takes the time to plan their project will probably finish first.

The SQL Server Query Optimizer is a cost-based optimizer. Each possible execution plan has an

associated cost in terms of the amount of computing resources used. The Query Optimizer

must analyze the possible plans and choose the one with the lowest estimated cost. Some

complex

statements have thousands of possible execution plans. In these cases, the

Query Optimizer doesn't analyze all possible combinations. Instead, it uses complex algorithms

to find an execution plan that has a cost reasonably close to the minimum possible cost.

The SQL Server Query Optimizer doesn't choose only the execution plan with the lowest

resource cost; it chooses the plan that returns results to the user with a reasonable cost in

resources and that returns the results the fastest. For example, processing a query in parallel

typically uses more resources than processing it serially, but completes the query faster. The

SQL Server Query Optimizer will use a parallel execution plan to return results if the load on the

server won't be adversely affected.

The SQL Server Query Optimizer relies on distribution statistics when it estimates the resource

costs of different methods for extracting information from a table or index. Distribution

statistics are kept for columns and indexes, and hold information on the density

of the

underlying data. This is used to indicate the selectivity of the values in a particular index or

column. For example, in a table representing cars, many cars have the same manufacturer, but

each car has a unique vehicle identification number (VIN). An index on the VIN is more

selective than an index on the manufacturer, because VIN has lower density than manufacturer.

If the index statistics aren't current, the Query Optimizer might not make the best choice for

the current state of the table. For more information about densities, see

Statistics

.

Density defines the distribution of unique values that exist in the data, or the average number

of duplicate values for a given column. As density decreases, selectivity of a value increases.

The SQL Server Query Optimizer is important because it enables the database server to adjust

dynamically to changing conditions in the database without requiring input from a

programmer or database administrator. This enables programmers to focus on describing the

final result of the query. They can trust that the SQL Server Query Optimizer will build an

efficient execution plan for the state of the database every time the statement is run.

1

1

### Estimated Execution Plan

### Actual Execution Plan

### Live Query Statistics

```sql
OR
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
SELECT
ProductID, ProductModelID
FROM
Production.Product
WHERE
(ProductModelID = 20
OR
ProductModelID = 21)
AND
Color =
'Red'
;
GO
SELECT
ProductID, ProductModelID
FROM
Production.Product
WHERE
ProductModelID = 20
OR
(ProductModelID = 21
AND
Color =
'Red'
);
GO
```

```sql
SELECT
```

```sql
ORDER BY
```

```sql
GROUP BY
```

```sql
FROM
```

```sql
SELECT
```

```sql
WHERE
```

```sql
ON
```

```sql
FROM
```

```sql
SELECT
```

```sql
WHERE
```

```sql
HAVING
```

```sql
SELECT
```

```sql
TableA
```

```sql
TableA
```

```sql
TableB
```

```sql
TableB
```

```sql
TableC
```

```sql
TableC
```

```sql
TableB
```

```sql
TableA
```

```sql
TableB
```

```sql
TableA
```

```sql
TableC
```

```sql
TableB
```

```sql
TableC
```

```sql
TableA
```

```sql
TableC
```

```sql
TableA
```

```sql
TableB
```

```sql
ORDER BY
```

```sql
GROUP BY
```

```sql
ORDER BY
```

```sql
WHERE
```

```sql
HAVING
```

```sql
SELECT
```
