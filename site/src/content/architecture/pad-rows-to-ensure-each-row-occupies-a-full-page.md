---
title: "Pad rows to ensure each row occupies a full page"
topic: "query-processing"
description: "One possible strategy for avoiding excessive page latch contention is to pad rows with a"
tags: ["query-processing","architecture"]
pubDate: "2026-05-29"
---

One possible strategy for avoiding excessive page latch contention is to pad rows with a

column to ensure that each row uses a full page. This strategy is an option when the overall

data size is small and you need to address

page latch contention caused by the following

combination of factors:

Small row size

Shallow B-tree

Access pattern with a high rate of random insert, select, update, and delete operations

Small tables, such as temporary queue tables

By padding rows to occupy a full page you require SQL to allocate more pages, making more

pages available for inserts and reducing

page latch contention.

A script similar to the following can be used to pad rows to occupy an entire page:

This technique is explained for completeness; in practice SQLCAT has only used this on a small

table with 10,000 rows in a single performance engagement. This technique has a limited

application because it increases memory pressure on SQL Server for large tables and can result

in non-buffer latch contention on non-leaf pages. The extra memory pressure can be a

significant limiting factor for application of this technique. With the amount of memory

available in a modern server, a large proportion of the working set for OLTP workloads is

typically held in memory. When the data set increases to a size that it no longer fits in memory,

a significant drop-off in performance occurs. Therefore, this technique is something that is only

applicable to small tables. This technique isn't used by SQLCAT for scenarios such as last

page/trailing page insert contention for large tables.

７

Note

Use the smallest char possible that forces one row per page to reduce the extra CPU

requirements for the padding value and the extra space required to log the row. Every

byte counts in a high performance system.

）

Important

`EX`

`EX`

```sql
ALTER
TABLE mytable
ADD
Padding
CHAR (5000)
DEFAULT
NOT
NULL (
'X'
);
```
