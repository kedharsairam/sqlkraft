---
name: "database"
title: "Database"
category: "statements"
description: "command isn't supported for the statistics object on a"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

## A. Create a simple nonclustered rowstore index

database clone. The

UPDATE STATISTICS

command isn't supported for the statistics object on a

columnstore index in any other scenario.

Requires the

permission on the table or view or membership in the

fixed

database role.

In Azure Synapse Analytics and Analytics Platform System (PDW), you can't create:

A clustered or nonclustered rowstore index on a data warehouse table when a

columnstore index already exists. This behavior is different from SMP SQL Server which

allows both rowstore and columnstore indexes to co-exist on the same table.

You can't create an index on a view.

To view information on existing indexes, you can query the

sys.indexes

catalog view.

and SQL database in Microsoft Fabric don't support filegroups other

than.

, SQL database in Microsoft Fabric, and Azure SQL Managed Instance

don't support

options.

Columnstore indexes aren't available before SQL Server 2012 (11.x).

Resumable index operations are available starting with SQL Server 2017 (14.x), in Azure

SQL Database, SQL database in Microsoft Fabric, and in Azure SQL Managed Instance.

The following examples create a nonclustered index on the

column of the

table.

## B. Create a simple nonclustered rowstore composite index

## C. Create an index on a table in another database

## D. Add a column to an index

`ALTER`

`db_ddladmin`

`PRIMARY`

`FILESTREAM`

`VendorID`

`Purchasing.ProductVendor`
