---
title: "Stored procedure and trigger execution"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

can't predict what key value will be supplied by the

parameter every time the procedure is executed. Because the key value can't be predicted, the

query processor also can't predict which member table will have to be accessed. To handle this

case, SQL Server builds an execution plan that has conditional logic, referred to as dynamic

filters, to control which member table is accessed, based on the input parameter value.

Assuming the

stored procedure was executed on Server1, the execution plan logic

can be represented as shown in the following:

Output

sometimes builds these types of dynamic execution plans even for queries that

aren't parameterized. The Query Optimizer can parameterize a query so that the execution plan

can be reused. If the Query Optimizer parameterizes a query referencing a partitioned view, the

Query Optimizer can no longer assume the required rows will come from a specified base

table. It will then have to use dynamic filters in the execution plan.

stores only the source for stored procedures and triggers. When a stored procedure

or trigger is first executed, the source is compiled into an execution plan. If the stored

procedure or trigger is again executed before the execution plan is aged from memory, the

relational engine detects the existing plan and reuses it. If the plan has aged out of memory, a

new plan is built. This process is similar to the process SQL Server follows for all Transact-SQL

statements. The main performance advantage that stored procedures and triggers have in SQL

Server compared with batches of dynamic Transact-SQL is that their Transact-SQL statements

are always the same. Therefore, the relational engine easily matches them with any existing

execution plans. Stored procedure and trigger plans are easily reused.

The execution plan for stored procedures and triggers is executed separately from the

execution plan for the batch calling the stored procedure or firing the trigger. This allows for

## Object Plans

## Compiled Plan

```sql
@CustomerIDParameter
```

`GetCustomer`

```sql
CREATE
PROCEDURE
GetCustomer @CustomerIDParameter
INT
AS
SELECT
*
FROM
CompanyData.dbo.Customers
WHERE
CustomerID = @CustomerIDParameter;
IF @CustomerIDParameter BETWEEN 1 and 3299999
Retrieve row from local table CustomerData.dbo.Customer_33
ELSE IF @CustomerIDParameter BETWEEN 3300000 and 6599999
Retrieve row from linked table Server2.CustomerData.dbo.Customer_66
ELSE IF @CustomerIDParameter BETWEEN 6600000 and 9999999
Retrieve row from linked table Server3.CustomerData.dbo.Customer_99
```
