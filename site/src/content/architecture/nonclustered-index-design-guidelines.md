---
title: "Nonclustered index design guidelines"
topic: "index-architecture"
description: "The main difference between a clustered and a nonclustered index is that a nonclustered index"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

The main difference between a clustered and a nonclustered index is that a nonclustered index

contains a subset of the columns in the table, usually sorted differently from the clustered

index. Optionally, a nonclustered index can be filtered, which means that it contains a subset of

all rows in the table.

A disk-based rowstore nonclustered index contains the row locators that point to the storage

location of the row in the base table. You can create multiple nonclustered indexes on a table

or indexed view. Generally, nonclustered indexes should be designed to improve the

performance of frequently used queries that would need to scan the base table otherwise.

Similar to the way you use an index in a book, the query optimizer searches for a data value by

searching the nonclustered index to find the location of the data value in the table and then

retrieves the data directly from that location. This makes nonclustered indexes the optimal

choice for exact match queries because the index contains entries describing the exact location

in the table of the data values being searched for in the queries.

For example, to query the

table for all employees that report to a

specific manager, the query optimizer might use the nonclustered index

; this has

as its first key column. Because the

`HumanResources.Employee`

`IX_Employee_ManagerID`

`ManagerID`

`ManagerID`
