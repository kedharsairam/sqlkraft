---
title: "Parameter sensitivity"
topic: "query-processing"
description: "Preparing a statement is more effective if parameter markers are used. For example, assume"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Preparing a statement is more effective if parameter markers are used. For example, assume

that an application is occasionally asked to retrieve product information from the

sample database. There are two ways the application can do this.

Using the first way, the application can execute a separate query for each product requested:

Using the second way, the application does the following:

1. Prepares a statement that contains a parameter marker (?):

2. Binds a program variable to the parameter marker.

3. Each time product information is needed, fills the bound variable with the key value and

executes the statement.

The second way is more efficient when the statement is executed more than three times.

In SQL Server, the prepare/execute model has no significant performance advantage over

direct execution, because of the way SQL Server reuses execution plans. SQL Server has

efficient algorithms for matching current Transact-SQL statements with execution plans that are

generated for prior executions of the same Transact-SQL statement. If an application executes

a Transact-SQL statement with parameter markers multiple times, SQL Server will reuse the

execution plan from the first execution for the second and subsequent executions (unless the

plan ages from the plan cache). The prepare/execute model still has these benefits:

Finding an execution plan by an identifying handle is more efficient than the algorithms

used to match an Transact-SQL statement to existing execution plans.

The application can control when the execution plan is created and when it is reused.

The prepare/execute model is portable to other databases, including earlier versions of.

### All Density

### average density

`AdventureWorks`

```sql
SELECT
*
FROM
AdventureWorks2022.Production.Product
WHERE
ProductID = 63;
SELECT
*
FROM
AdventureWorks2022.Production.Product
WHERE
ProductID = ?;
```
