---
title: "Simple parameterization"
topic: "io-fundamentals"
description: "However, it can be parameterized according to simple parameterization rules. When forced"
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

However, it can be parameterized according to simple parameterization rules. When forced

parameterization is tried but fails, simple parameterization is still subsequently tried.

In SQL Server, using parameters or parameter markers in Transact-SQL statements increases

the ability of the relational engine to match new Transact-SQL statements with existing,

previously compiled execution plans.

If a Transact-SQL statement is executed without parameters, SQL Server parameterizes the

statement internally to increase the possibility of matching it against an existing execution

plan. This process is called simple parameterization. In SQL Server versions prior to 2005, the

process was referred to as auto-parameterization.

Consider this statement:

The value 1 at the end of the statement can be specified as a parameter. The relational engine

builds the execution plan for this batch as if a parameter had been specified in place of the

value 1. Because of this simple parameterization, SQL Server recognizes that the following two

statements generate essentially the same execution plan and reuses the first plan for the

second statement:

２

Warning

Using parameters or parameter markers to hold values typed by end users is more secure

than concatenating the values into a string that is then executed using either a data access

API method, the

statement, or the

stored procedure.

## EF Query caching and parameterization

## EF Raw SQL

## Queries

```sql
SELECT
*
FROM
Person.Address
WHERE
AddressID = 1 + 2;
```

`EXECUTE`

`sp_executesql`

```sql
SELECT
*
FROM
AdventureWorks2022.Production.Product
WHERE
ProductSubcategoryID = 1;
SELECT
*
FROM
AdventureWorks2022.Production.Product
WHERE
ProductSubcategoryID = 1;
```
