---
title: "Database considerations"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

For example, an index might be useful for columns with many distinct data values, but

less so for columns with many duplicate values. For columns with many NULLs or those

that have well-defined subsets of data, you can use a filtered index. For more information,

see

Filtered index design guidelines

in this guide.

4.

For example, creating a clustered index on an existing large table could benefit from the

index option. The

option allows for concurrent activity on the underlying

data to continue while the index is being created or rebuilt. Using row or page

data

compression

can improve performance by reducing the I/O and memory footprint of the

index. For more information, see

CREATE INDEX.

5.

It's often better to modify an existing index than to create a new but mostly duplicate

index. For example, consider adding one or two extra included columns to an existing

index, instead of creating a new index with these columns. This is particularly relevant

when you

tune nonclustered indexes with missing index suggestions

, or if you use the

Database Engine Tuning Advisor

, where you might be offered similar variations of indexes

on the same table and columns.

Understanding the characteristics of your database, queries, and table columns can help you

design optimal indexes initially and modify the design as your applications evolve.

When you design an index, consider the following database guidelines:

A large number of indexes on a table affect the performance of

,

,

,

and

statements because data in indexes might have to change as data in the table

changes. For example, if a column is used in several indexes and you execute an

statement that modifies that column's data, each index that contains that column must be

updated as well.

Avoid over-indexing heavily updated tables and keep indexes narrow, that is, with as

few columns as possible.

### S

### ARG

### able

`ONLINE`

`ONLINE`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`

`UPDATE`
