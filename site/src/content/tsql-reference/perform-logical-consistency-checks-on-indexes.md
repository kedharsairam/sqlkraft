---
name: "Perform logical consistency checks on indexes"
title: "Perform logical consistency checks on indexes"
category: "queries"
description: "exceeds the value configured with Resource Governor, the Database Engine uses the Resource"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

exceeds the value configured with Resource Governor, the Database Engine uses the Resource

Governor MAXDOP value, described in ALTER WORKLOAD GROUP (Transact-SQL). All semantic

rules used with the max degree of parallelism configuration option are applicable when you

use the MAXDOP query hint. For more information, see

Configure the max degree of

parallelism Server Configuration Option

.

For the specified table,

checks for the following:

Index, in-row, LOB, and row-overflow data pages are correctly linked.

Indexes are in their correct sort order.

Pointers are consistent.

The data on each page is reasonable, included computed columns.

Page offsets are reasonable.

Every row in the base table has a matching row in each nonclustered index, and vice-

versa.

Every row in a partitioned table or index is in the correct partition.

Link-level consistency between the file system and table when storing

data in the file system using FILESTREAM.

Logical consistency checking on indexes varies according to the compatibility level of the

database, as follows:

If the compatibility level is 100 (SQL Server 2008 (10.0.x)) or higher:

Unless

is specified,

performs both physical and logical

consistency checks on a single table and on all its nonclustered indexes. However, on

XML indexes, spatial indexes, and indexed views only physical consistency checks are

performed by default.

７

Note

If MAXDOP is set to zero then the server chooses the max degree of parallelism.

７

Note

To perform

on every table in the database, use

.

```sql
DBCC CHECKTABLE
```

```sql
NOINDEX
```

```sql
DBCC CHECKTABLE
```

```sql
DBCC CHECKTABLE
```
