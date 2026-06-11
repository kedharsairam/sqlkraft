---
title: "Override degrees of parallelism"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

### Database Engine Configuration - MaxDOP page

Starting with SQL Server 2014 (12.x) and database compatibility level 110, the

statement can be executed in parallel. Other forms of insert operators work the same way as

described for SQL Server 2012 (11.x).

Starting with SQL Server 2016 (13.x) and database compatibility level 130, the

statement can be executed in parallel when inserting into heaps or clustered

columnstore indexes (CCI), and using the TABLOCK hint. Inserts into local temporary tables

(identified by the # prefix) and global temporary tables (identified by ## prefixes) are also

enabled for parallelism using the TABLOCK hint. For more information, see

INSERT (Transact-

SQL)

.

Static and keyset-driven cursors can be populated by parallel execution plans. However, the

behavior of dynamic cursors can be provided only by serial execution. The Query Optimizer

always generates a serial execution plan for a query that is part of a dynamic cursor.

The degree of parallelism sets the number of processors to use in parallel plan execution. This

configuration can be set at various levels:

1. Server level, using the

server configuration option

.

Applies to:

SQL Server

2. Workload level, using the

Resource Governor workload group configuration

option

.

Applies to:

SQL Server

3. Database level, using the

database scoped configuration

.

Applies to:

SQL Server and Azure SQL Database

4. Query or index statement level, using the

query hint

or

index option.

For example, you can use the MAXDOP option to control, by increasing or reducing, the

number of processors dedicated to an online index operation. In this way, you can

balance the resources used by an index operation with those of the concurrent users.

Applies to:

SQL Server and Azure SQL Database

７

Note

SQL Server 2019 (15.x) introduces automatic recommendations for setting the

MAXDOP server configuration option during the installation process. The setup user

interface allows you to either accept the recommended settings or enter your own

value. For more information, see

.

### MAXDOP recommendations

```sql
SELECT ... INTO
```

```sql
INSERT ...
SELECT
```
