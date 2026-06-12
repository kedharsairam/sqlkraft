---
name: "Working with parquet"
title: "Working with parquet"
category: "queries"
description: "In Azure Synapse Analytics dedicated SQL pools, and Analytics Platform System, PolyBase"
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

In Azure Synapse Analytics dedicated SQL pools, and Analytics Platform System, PolyBase

can consume a maximum of 33,000 files per folder when running 32 concurrent PolyBase

queries. This maximum number includes both files and subfolders in each HDFS folder. If

the degree of concurrency is less than 32, a user can run PolyBase queries against folders

in HDFS that contain more than 33,000 files. We recommend that users of Hadoop and

PolyBase keep file paths short and use no more than 30,000 files per HDFS folder. When

too many files are referenced, a JVM out-of-memory exception occurs.

In serverless SQL pools, external tables can't be created in a location where you currently

have data. To reuse a location that has been used to store data, the location must be

manually deleted on ADLS. For more limitations and best practices, see

Filter optimization

## best practices.

In Azure Synapse Analytics dedicated SQL pools, and Analytics Platform System, when

selects from an RCFile, the column values in the RCFile must not

contain the pipe (

) character.

SET ROWCOUNT (Transact-SQL)

has no effect on CREATE EXTERNAL TABLE AS SELECT. To

achieve a similar behavior, use

TOP (Transact-SQL).

Review

Naming and Referencing Containers, Blobs, and Metadata

for limitations on file names.

The following characters present in data can cause errors including rejected records with

to Parquet files.

In Azure Synapse Analytics and Analytics Platform System, this also applies to ORC files.

(quotation mark character)

To use

containing these characters, you must first run the

statement to export the data to delimited text files where

you can then convert them to Parquet or ORC by using an external tool.

```sql
CREATE
EXTERNAL TABLE AS SELECT
```

```sql
|
```

```sql
CREATE EXTERNAL TABLE AS SELECT
```

```sql
|
"
```

```sql
\r\n
\r
\n
```

```sql
CREATE EXTERNAL TABLE AS SELECT
```

```sql
CREATE EXTERNAL TABLE AS SELECT
```
