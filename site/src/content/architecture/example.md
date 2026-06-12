---
title: "Example"
topic: "query-processing"
description: "Table Partition 3: A >= 20 AND A < 30"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

Table Partition 3: A >= 20 AND A < 30

B=50, B=100, B=150

Table Partition 4: A >= 30

B=50, B=100, B=150

To improve the performance of queries that access a large amount of data from large

partitioned tables and indexes, we recommend the following best practices:

Stripe each partition across many disks. This is especially relevant when using spinning

disks.

When possible, use a server with enough main memory to fit frequently accessed

partitions, or all partitions in memory, to reduce I/O cost.

If the data you query won't fit in memory, compress the tables and indexes. This will

reduce I/O cost.

Use a server with fast processors and as many processor cores as you can afford, to take

advantage of parallel query processing capability.

Ensure the server has sufficient I/O controller bandwidth.

Create a clustered index on every large partitioned table to take advantage of B-tree

scanning optimizations.

Follow the best practice recommendations in the white paper,

The Data Loading

Performance Guide

, when bulk loading data into partitioned tables.

The following example creates a test database containing a single table with seven partitions.

Use the tools described previously when executing the queries in this example to view

partitioning information for both compile-time and run-time plans.

７

Note

This example inserts more than 1 million rows into the table. Running this example can

take several minutes depending on your hardware. Before executing this example, verify

that you have more than 1.5 GB of disk space available.

Logical and physical showplan operator reference

Extended Events overview

## Best practices for monitoring workloads with Query Store

Cardinality Estimation (SQL Server)

Intelligent query processing in SQL databases

Operator Precedence (Transact-SQL)

Execution plan overview

Performance Center for SQL Server Database Engine and Azure SQL Database

）

Note:

The author created this article with assistance from AI.

Learn more
