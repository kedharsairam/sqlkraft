---
title: 'Batch mode execution'
topic: 'io-fundamentals'
description: 'Azure SQL Managed Instance'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The SQL Server Database Engine processes queries on various data storage architectures such

as local tables, partitioned tables, and tables distributed across multiple servers. The following

sections cover how SQL Server processes queries and optimizes query reuse through execution

plan caching.

The SQL Server Database Engine can process Transact-SQL statements using two distinct

processing modes:

Row mode execution

Batch mode execution

Row mode execution

is a query processing method used with traditional RDBMS tables, where

data is stored in row format. When a query is executed and accesses data in row store tables,

the execution tree operators and child operators read each required row, across all the

columns specified in the table schema. From each row that is read, SQL Server then retrieves

the columns that are required for the result set, as referenced by a SELECT statement, JOIN

predicate, or filter predicate.

Batch mode execution

is a query processing method used to process multiple rows together

(hence the term batch). Each column within a batch is stored as a vector in a separate area of

memory, so batch mode processing is vector-based. Batch mode processing also uses

algorithms that are optimized for the multi-core CPUs and increased memory throughput that

are found on modern hardware.

７

Note

Row mode execution is very efficient for OLTP scenarios, but can be less efficient when

scanning large amounts of data, for example in Data Warehousing scenarios.
