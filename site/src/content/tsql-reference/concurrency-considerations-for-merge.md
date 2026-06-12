---
name: "Concurrency considerations for MERGE"
title: "Concurrency considerations for MERGE"
category: "queries"
description: "optimizer doesn't need to perform extra validation processing to locate and update"
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

optimizer doesn't need to perform extra validation processing to locate and update

duplicate rows and additional sort operations aren't necessary.

Avoid tables with any form of columnstore index as the target of

statements. As

with any UPDATEs, you might find performance better with columnstore indexes by

updating a staged rowstore table, then performing a batched

and

, instead

of an

or.

In terms of locking,

is different from discrete, consecutive

,

, and

statements.

still executes

,

, and

operations, however using

different locking mechanisms. It might be more efficient to write discrete

,

, and

statements for some application needs. At scale,

might introduce complicated

concurrency issues or require advanced troubleshooting. As such, plan to thoroughly test any

statement before deploying to production.

statements are a suitable replacement for discrete

,

, and

operations in (but not limited to) the following scenarios:

ETL operations involving large row counts be executed during a time when other

concurrent operations aren't\* expected. When heavy concurrency is expected, separate

,

, and

logic might perform better, with less blocking, than a

statement.

Complex operations involving small row counts and transactions unlikely to execute for

extended duration.

Complex operations involving user tables where indexes can be designed to ensure

optimal execution plans, avoiding table scans and lookups in favor of index scans or -

ideally - index seeks.

Other considerations for concurrency:

In some scenarios where unique keys are expected to be both inserted and updated by

the

, specifying the

will prevent against unique key violations.

is

a synonym for the

transaction isolation level, which doesn't allow for other

concurrent transactions to modify data that this transaction has read.

is the

safest isolation level but provides for the least concurrency with other transactions that

retains locks on ranges of data to prevent phantom rows from being inserted or updated

while reads are in progress. For more information on

, see

Table Hints

and

SET

TRANSACTION ISOLATION LEVEL (Transact-SQL).

## JOIN best practices

## Parameterization best practices

To improve the performance of the

statement and ensure correct results are obtained,

we recommend the following join guidelines:

Specify only search conditions in the

clause that determine

the criteria for matching data in the source and target tables. That is, specify only columns

from the target table that are compared to the corresponding columns of the source

table.

Don't include comparisons to other values such as a constant.

To filter out rows from the source or target tables, use one of the following methods.

Specify the search condition for row filtering in the appropriate

clause. For example,

Define a view on the source or target that returns the filtered rows and reference the view

as the source or target table. If the view is defined on the target table, any actions against

it must satisfy the conditions for updating views. For more information about updating

data by using a view, see

Modify Data Through a View.

Use the

clause to filter out rows from the source or

target tables. This method is similar to specifying additional search criteria in the

clause and might produce incorrect results. We recommend that you avoid using this

method or test thoroughly before implementing it.

The join operation in the

statement is optimized in the same way as a join in a

statement. That is, when SQL Server processes join, the query optimizer chooses the most

efficient method (out of several possibilities) of processing the join. When the source and

target are of similar size and the index guidelines described previously are applied to the

source and target tables, a merge join operator is the most efficient query plan. This is because

both tables are scanned once and there's no need to sort the data. When the source is smaller

than the target table, a nested loops operator is preferable.

You can force the use of a specific join by specifying the

clause in the

statement. We recommend that you don't use the hash join as a query hint for

statements because this join type doesn't use indexes.

If a

,

,

, or

statement is executed without parameters, the SQL

Server query optimizer might choose to parameterize the statement internally. This means that

any literal values that are contained in the query are substituted with parameters. For example,

the statement

, might be implemented

## TOP clause best practices

internally as. This process, which is called

simple parameterization

, increases the ability of the relational engine to match new SQL

statements with existing, previously compiled execution plans. Query performance might be

improved because the frequency of query compilations and recompilations is reduced. The

query optimizer doesn't apply the simple parameterization process to

statements.

Therefore,

statements that contain literal values might not perform and individual

,

, or

statements because a new plan is compiled each time the

statement is executed.

To improve query performance, we recommend the following parameterization guidelines:

Parameterize all literal values in the

clause and in the

clauses of the

statement. For example, you can incorporate the

statement

into a stored procedure replacing the literal values with appropriate input parameters.

If you can't parameterize the statement, create a plan guide of type

and specify

the

query hint in the plan guide. For more information, see

Specify Query Parameterization Behavior by Using Plan Guides.

If

statements are executed frequently on the database, consider setting the

option on the database to. Use caution when setting this

option. The

option is a database-level setting and affects how all

queries against the database are processed. For more information, see

Forced

Parameterization.

As a newer and easier alternative to plan guides, consider a similar strategy with Query

Store hints. For more information, see

Query Store hints.

In the

statement, the

clause specifies the number or percentage of rows that are

affected after the source table and the target table are joined, and after rows that don't qualify

for an insert, update, or delete action are removed. The

clause further reduces the number

of joined rows to the specified value and the insert, update, or delete actions are applied to the

remaining joined rows in an unordered fashion. That is, there's no order in which the rows are

distributed among the actions defined in the

clauses. For example, specifying

affects 10 rows; of these rows, 7 might be updated and 3 inserted, or 1 might be deleted, 5

updated, and 4 inserted and so on.

It's common to use the

clause to perform data manipulation language (DML) operations

on a large table in batches. When using the

clause in the

statement for this

purpose, it's important to understand the following implications.

I/O performance might be affected.

## Bulk load best practices

The

statement performs a full table scan of both the source and target tables.

Dividing the operation into batches reduces the number of write operations performed

per batch; however, each batch performs a full table scan of the source and target tables.

The resulting read activity might affect the performance of the query and other

concurrent activity on the tables.

Incorrect results can occur.

It's important to ensure that all successive batches target new rows or undesired behavior

such as incorrectly inserting duplicate rows into the target table can occur. This can

happen when the source table includes a row that wasn't in a target batch but was in the

overall target table. To ensure correct results:

Use the

clause to determine which source rows affect existing target rows and

which are genuinely new.

Use an additional condition in the

clause to determine if the target row

was already updated by a previous batch.

Use an additional condition in the

clause and

logic to verify the

same row can't be updated twice.

Because the

clause is only applied after these clauses are applied, each execution either

inserts one genuinely unmatched row or updates one existing row.

The

statement can be used to efficiently bulk load data from a source data file into a

target table by specifying the

clause as the table source. By doing so, the

entire file is processed in a single batch.

To improve the performance of the bulk merge process, we recommend the following

guidelines:

Create a clustered index on the join columns in the target table.

Disable other non-unique, nonclustered indexes on the target table during the bulk load

, enable them afterwards. This is common and useful for nightly bulk data

operations.

Use the

and

hints in the

clause, to specify how the

source data file is sorted.

By default, the bulk operation assumes the data file is unordered. Therefore, it's important

that the source data is sorted according to the clustered index on the target table and

that the

hint is used to indicate the order so that the query optimizer can generate

### merge stmt

## Measure and diagnose MERGE performance

`MERGE`

`DELETE`

`INSERT`

`UPDATE`

`MERGE`

`MERGE`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`INSERT`

`UPDATE`

`DELETE`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`MERGE`

`MERGE`

`INSERT`

`UPDATE`

`DELETE`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`MERGE`

`HOLDLOCK`

`HOLDLOCK`

`SERIALIZABLE`

`SERIALIZABLE`

`HOLDLOCK`

`MERGE`

```sql
ON <merge_search_condition>
```

`WHEN`

```sql
WHEN NOT MATCHED AND S.EmployeeName LIKE 'S%' THEN INSERT.
```

```sql
WITH <common table expression>
```

`ON`

`MERGE`

`SELECT`

```sql
OPTION (<query_hint>)
```

`MERGE`

`MERGE`

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

```sql
INSERT dbo.MyTable (Col1, Col2) VALUES (1, 10)
```

```sql
INSERT dbo.MyTable (Col1, Col2) VALUES (@p1, @p2)
```

`MERGE`

`MERGE`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

```sql
ON <merge_search_condition>
```

`WHEN`

`MERGE`

`MERGE`

`TEMPLATE`

```sql
PARAMETERIZATION FORCED
```

`MERGE`

`PARAMETERIZATION`

`FORCED`

`PARAMETERIZATION`

`MERGE`

`TOP`

`TOP`

`WHEN`

```sql
TOP (10)
```

`TOP`

`TOP`

`MERGE`

`MERGE`

`ON`

```sql
WHEN MATCHED
```

```sql
WHEN MATCHED
```

`SET`

`TOP`

`MERGE`

`OPENROWSET(BULK.)`

`MERGE`

`ORDER`

`UNIQUE`

`OPENROWSET(BULK.)`

`ORDER`
