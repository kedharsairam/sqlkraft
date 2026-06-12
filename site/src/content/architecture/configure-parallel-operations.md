---
title: "Configure parallel operations"
topic: "filestream"
description: "This article defines max degree of parallelism and explains how to modify this setting in SQL"
tags: ["filestream","configure-parallel-operations"]
pubDate: "2025-12-01"
---

This article defines max degree of parallelism and explains how to modify this setting in SQL

Server by using SQL Server Management Studio or Transact-SQL.

On multiprocessor systems that are running SQL Server Enterprise or higher, index statements

might use multiple processors (CPUs) to perform the scan, sort, and index operations

associated with the index statement just like other queries do. The number of CPUs used to run

a single index statement is determined by the

max degree of parallelism

server configuration

option, the current workload, and the index statistics.

The max degree of parallelism option determines the maximum number of processors to use in

parallel plan execution. If the SQL Server Database Engine detects that the system is busy, the

degree of parallelism of the index operation is automatically reduced before statement

execution starts. The Database Engine can also reduce the degree of parallelism if the leading

key column of a non-partitioned index has a limited number of distinct values or the frequency

of each distinct value varies significantly. For more information, see

Query Processing

Architecture Guide.

The number of processors that are used by the query optimizer typically provides optimal

performance. However, operations such as creating, rebuilding, or dropping very large

indexes are resource intensive and can cause insufficient resources for other applications

and database operations for the duration of the index operation.

When this problem occurs, you can manually configure the maximum number of

processors that are used to run the index statement by limiting the number of processors

to use for the index operation.

The

index option overrides the max degree of parallelism configuration option

only for the query specifying this option. The following table lists the valid integer values

７

Note

Parallel index operations aren't available in every SQL Server edition. For more

information, see.

`MAXDOP`
