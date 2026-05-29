---
title: 'Discontinued features in SQL Server 2019 (15.x)'
topic: 'query-processing'
description: '(Python package in SQL Server Machine Learning Services)'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Python

microsoftml

(Python package in SQL Server Machine Learning Services)

R

olapR

(R package in SQL Server Machine Learning Services)

R

sqlrutils

(R package in SQL Server Machine Learning Services)

R

MicrosoftML

(R package in SQL Server Machine Learning Services)

SQL Server Big Data Clusters retired on February 28, 2025. For more information, see

Big

data options on the Microsoft SQL Server platform

.

SQL Server PolyBase scale-out groups will be retired. Scale out group functionality is

removed from the product in SQL Server 2022 (16.x). PolyBase data virtualization

continues to be fully supported as a scale-up feature in SQL Server.

Support for Hadoop (HDFS) external data sources will be retired for SQL Server PolyBase.

See

Changes to PolyBase support in SQL Server

.

In SQL Server 2022 (16.x) and later versions, Hadoop external data sources are no longer

supported. You must manually recreate external data sources previously created with

, and any external table that uses this external data source. You must also

configure your external data sources to use new connectors when connecting to Azure

Storage.

Azure Blob Storage

ADLS Gen 2

In July 2024, Stretch Database was discontinued in all supported versions of SQL Server.

The following database scoped configuration options are discontinued:

ﾉ

Expand table

```sql
TYPE
= HADOOP
```

```sql
wasb[s]
abs
```

```sql
abfs[s]
adls
```

```sql
DISABLE_BATCH_MODE_ADAPTIVE_JOIN
DISABLE_BATCH_MODE_MEMORY_GRANT_FEEDBACK
DISABLE_INTERLEAVED_EXECUTION_TVF
```
