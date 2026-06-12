---
name: "Supported data types"
title: "Supported data types"
category: "data-types"
description: "When working with parquet files,"
tags: ["tsql","data-types"]
pubDate: "2026-05-29"
---

When working with parquet files, will generate one parquet file per available CPU, up to the configured maximum degree of parallelism (MAXDOP). Each file can grow up to 190 GB, after that SQL Server will generate more Parquet files as needed.

The query hint will only affect the SELECT part of. It has no influence on the number of parquet files. Only database-level MAXDOP and instance-level MAXDOP is considered.

Takes a shared lock on the SCHEMARESOLUTION object.

CETAS can be used to store result sets with the following SQL data types: binary

varbinary

char

varchar

nchar

nvarchar

smalldate

date

datetime

datetime2

datetimeoffset

time

decimal

numeric

float

real

bigint

tinyint

smallint

int

bigint

bit

money

smallmoney

```sql
CREATE EXTERNAL TABLE AS SELECT
```

```sql
OPTION (MAXDOP n)
```

```sql
CREATE EXTERNAL TABLE AS
SELECT
```
