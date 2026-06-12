---
title: "Parameters and execution plan reuse"
topic: "query-processing"
description: "The use of parameters, including parameter markers in ADO, OLE DB, and ODBC applications,"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

The use of parameters, including parameter markers in ADO, OLE DB, and ODBC applications,

can increase the reuse of execution plans.

The only difference between the following two

statements is the values that are

compared in the

clause:

The only difference between the execution plans for these queries is the value stored for the

comparison against the

column. While the goal is for SQL Server to

always recognize that the statements generate essentially the same plan and reuse the plans,

sometimes doesn't detect this in complex Transact-SQL statements.

Separating constants from the Transact-SQL statement by using parameters helps the relational

engine recognize duplicate plans. You can use parameters in the following ways:

In Transact-SQL , use

:

In SQL Server prior to 2005, queries continue to recompile based on cardinality changes to

the DML trigger inserted and deleted tables, even when this setting is.

２

Warning

Using parameters or parameter markers to hold values that are typed by end users is

more secure than concatenating the values into a string that is then executed by using

either a data access API method, the

statement, or the

stored

procedure.

This method is recommended for Transact-SQL scripts, stored procedures, or triggers that

generate SQL statements dynamically.

ADO, OLE DB, and ODBC use parameter markers. Parameter markers are question marks

(?) that replace a constant in a SQL statement and are bound to a program variable. For

example, you would do the following in an ODBC application:

Use

to bind an integer variable to the first parameter marker in a

SQL statement.

Put the integer value in the variable.

Execute the statement, specifying the parameter marker (?):

VB

The SQL Server Native Client OLE DB Provider and the SQL Server Native Client ODBC

driver included with SQL Server use

to send statements to SQL Server

when parameter markers are used in applications.

To design stored procedures, which use parameters by design.

If you don't explicitly build parameters into the design of your applications, you can also rely

on the SQL Server Query Optimizer to automatically parameterize certain queries by using the

default behavior of simple parameterization. Alternatively, you can force the Query Optimizer

to consider parameterizing all queries in the database by setting the

option

of the

statement to.

When forced parameterization is enabled, simple parameterization can still occur. For example,

the following query can't be parameterized according to the rules of forced parameterization:

`SELECT`

`WHERE`

`ProductSubcategoryID`

`sp_executesql`

`OFF`

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
ProductSubcategoryID = 4;
```

`SQLBindParameter`

`sp_executesql`

`PARAMETERIZATION`

```sql
ALTER DATABASE
```

`FORCED`

```sql
DECLARE
@MyIntParm
INT
SET
@MyIntParm = 1
EXEC sp_executesql
N
'SELECT *
FROM AdventureWorks2022.Production.Product
WHERE ProductSubcategoryID = @Parm'
,
N
'@Parm INT'
,
@MyIntParm
SQLExecDirect(hstmt,
"SELECT *
FROM AdventureWorks2022.Production.Product
WHERE ProductSubcategoryID = ?"
,
SQL_NTS);
```
