---
title: "Index data"
topic: "json-data"
description: ""
tags: ["json-data","index-data"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

You can optimize your queries over JSON documents using standard indexes.

Indexes work the same way on JSON data in

/

or the

native

data type.

Database indexes improve the performance of filter and sort operations. Without indexes, SQL

Server has to perform a full table scan every time you query data.

When you store JSON data in SQL Server, typically you want to filter or sort query results by

one or more

properties

of the JSON documents.

In this example, assume that the

table has an

column

that contains various information in JSON format about sales orders. For example, it contains

unstructured data about customer, sales person, shipping and billing addresses, and so forth.

You could use values from the

column to filter sales orders for a customer.

By default, the column

used doesn't exist, it can be created in the

database with the following code. The following examples don't apply to the

series of sample databases.

７

Note

In SQL Server 2025 (17.x), you can use the

feature.

７

Note

The

:

is generally available for Azure SQL Database and Azure SQL Managed Instance with

the

2025

or.

is in preview for SQL Server 2025 (17.x) and SQL database in Fabric.

```sql
AdventureWorks.SalesOrderHeader
Info
Info
Info
AdventureWorks
AdventureWorksLT
```
