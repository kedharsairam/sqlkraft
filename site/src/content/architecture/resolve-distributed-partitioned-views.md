---
title: "Resolve distributed partitioned views"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

For more information, see

Table Hints (Transact-SQL).

The SQL Server query processor optimizes the performance of distributed partitioned views.

The most important aspect of distributed partitioned view performance is minimizing the

amount of data transferred between member servers.

builds intelligent, dynamic plans that make efficient use of distributed queries to

access data from remote member tables:

The Query Processor first uses OLE DB to retrieve the check constraint definitions from

each member table. This allows the query processor to map the distribution of key values

across the member tables.

The Query Processor compares the key ranges specified in an Transact-SQL statement

clause to the map that shows how the rows are distributed in the member tables.

The query processor then builds a query execution plan that uses distributed queries to

retrieve only those remote rows that are required to complete the Transact-SQL

statement. The execution plan is also built in such a way that any access to remote

member tables, for either data or metadata, are delayed until the information is required.

For example, consider a system where a

table is partitioned across Server1

(

from 1 through 3299999), Server2 (

from 3300000 through 6599999),

and Server3 (

from 6600000 through 9999999).

Consider the execution plan built for this query executed on Server1:

The execution plan for this query extracts the rows with

key values from 3200000

through 3299999 from the local member table, and issues a distributed query to retrieve the

rows with key values from 3300000 through 3400000 from Server2.

The SQL Server Query Processor can also build dynamic logic into query execution plans for

Transact-SQL statements in which the key values aren't known when the plan must be built. For

example, consider this stored procedure:

`WHERE`

`Customers`

`CustomerID`

`CustomerID`

`CustomerID`

`CustomerID`

```sql
SELECT
*
FROM
CompanyData.dbo.Customers
WHERE
CustomerID
BETWEEN
3200000
AND
3400000;
```
