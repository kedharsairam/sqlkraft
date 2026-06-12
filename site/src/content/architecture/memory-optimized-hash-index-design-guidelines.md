---
title: "Memory-optimized hash index design guidelines"
topic: "index-architecture"
description: "A nonclustered index contains a copy of part or all of the rows and columns in the underlying"
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

A nonclustered index contains a copy of part or all of the rows and columns in the underlying

table. The index is defined as one or more columns of the table, and has an optional condition

that filters the rows.

You can create an updatable

nonclustered columnstore index on a rowstore table. The

columnstore index stores a copy of the data so you do need extra storage. However, the data

in the columnstore index compresses to a much smaller size than the rowstore table requires.

By doing this, you can run analytics on the columnstore index and OLTP workloads on the

rowstore index at the same time. The columnstore is updated when data changes in the

rowstore table, so both indexes are working against the same data.

A rowstore table can have one nonclustered columnstore index. For more information, see

Columnstore indexes - design guidance.

You can have

one or more nonclustered rowstore indexes on a clustered columnstore table. By

doing this, you can perform efficient table seeks on the underlying columnstore. Other options

become available too. For example, you can enforce uniqueness by using a

constraint

on the rowstore table. When a nonunique value fails to insert into the rowstore table, the

Database Engine doesn't insert the value into the columnstore either.

The nonclustered columnstore index definition supports using a filtered condition. To minimize

the performance effect of adding a columnstore index, use a filter expression to create a

nonclustered columnstore index on only the subset of data required for analytics.

A memory-optimized table can have one columnstore index. You can create it when the table is

created or add it later with

ALTER TABLE.

For more information, see

Columnstore indexes - query performance.

When using

In-Memory OLTP

, all memory-optimized tables must have at least one index. For a

memory-optimized table, every index is also memory-optimized. Hash indexes are one of the

possible index types in a memory-optimized table. For more information, see

Indexes on

Memory-Optimized Tables.

`UNIQUE`
