---
title: "Local variables"
topic: "query-processing"
description: |
  'Parameter sensitivity, also known as "parameter sniffing", refers to a process whereby SQL'
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Parameter sensitivity, also known as "parameter sniffing", refers to a process whereby SQL

Server "sniffs" the current parameter values during compilation or recompilation, and passes it

along to the Query Optimizer so that they can be used to generate potentially more efficient

query execution plans.

Parameter values are sniffed during compilation or recompilation for the following types of

batches:

Stored procedures

Queries submitted via

Prepared queries

For more information on troubleshooting parameter sniffing issues, see:

Investigate and resolve parameter-sensitive issues

Parameters and Execution Plan Reuse

Parameter Sensitive Plan optimization

Troubleshoot queries with parameter sensitive query execution plan issues in Azure SQL

Database

Troubleshoot queries with parameter sensitive query execution plan issues in Azure SQL

Managed Instance

When a query in SQL Server uses the

hint, the query optimizer turns

parameter and local variables into compile-time constants that can be constant folded and

reduced to literals. This means that during compilation, the optimizer knows and can use the

current runtime values of parameters and local variables as they exist immediately prior to that

statement. The OPTION (RECOMPILE) allows the optimizer to generate a more optimal query

plan tailored to the specific values and to take advantage of the best underlying indexes at run

time. For parameters, this process refers not to the values originally passed to the batch or

stored procedure, but to their values at the time of recompilation. These values might have

been modified within the procedure before reaching the statement that includes.

This behavior can improve performance for queries with highly variable or skewed input data.

When a query uses local variables, SQL Server can't sniff their values at compile time, so it

estimates cardinality using available statistics or heuristics. If statistics exist, it typically uses the

value (also known as

) from the statistical histogram to estimate

how many rows match the predicate. However, if no statistics are available for the column, SQL

Server falls back on heuristic estimates, such as assuming 10% selectivity for equality

predicates, and 30% for inequalities and ranges, which might lead to less accurate execution

plans. Here's an example of a query that uses a local variable.

### Scalar UDFs

### Remote Query

`sp_executesql`

```sql
OPTION (RECOMPILE)
```

`RECOMPILE`
