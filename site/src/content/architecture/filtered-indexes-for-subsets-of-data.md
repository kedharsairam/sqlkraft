---
title: "Filtered indexes for subsets of data"
topic: "index-architecture"
description: "Creating a filtered index can reduce disk storage for nonclustered indexes when a full-"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Creating a filtered index can reduce disk storage for nonclustered indexes when a full-

table index isn't necessary. You might be able to replace a full-table nonclustered index

with multiple filtered indexes without significantly increasing the storage requirements.

Filtered indexes are useful when columns contain well-defined subsets of data. Examples are:

Columns that contain many NULLs.

Heterogeneous columns that contain categories of data.

Columns that contain ranges of values such as amounts, time, and dates.

Reduced update costs for filtered indexes are most noticeable when the number of rows in the

index is small compared with a full-table index. If the filtered index includes most of the rows in

the table, it could cost more to maintain than a full-table index. In this case, you should use a

full-table index instead of a filtered index.

Filtered indexes are defined on one table and only support simple comparison operators. If you

need a filter expression that has complex logic or references multiple tables, you should create

an

indexed computed column

or an

indexed view.

In order to design effective filtered indexes, it's important to understand what queries your

application uses and how they relate to subsets of your data. Some examples of data that have

well-defined subsets are columns with many NULLs, columns with heterogeneous categories of

values and columns with distinct ranges of values.

The following design considerations give several scenarios for when a filtered index can

provide advantages over full-table indexes.

When a column only has a few relevant values for queries, you can create a filtered index on

the subset of values. For example, when the column is mostly NULL and the query requires only

non-NULL values, you can create a filtered index containing the non-NULL rows.

For example, the

AdventureWorks sample database

has a

table

with 2,679 rows. The

column has only 199 rows that contain a non-NULL value and the

other 2480 rows contain NULL. The following filtered index covers queries that return the

columns defined in the index and that require only rows with a non-NULL value for.

`Production.BillOfMaterials`

`EndDate`

`EndDate`
