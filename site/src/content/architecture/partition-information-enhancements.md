---
title: "Partition information enhancements"
topic: "io-fundamentals"
description: "into the clustered index on column b to find the rows that meet the condition"
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

into the clustered index on column b to find the rows that meet the condition

and.

The following illustration is a logical representation of the skip scan operation. It shows table

with data in columns

and. The partitions are numbered 1 through 4 with the partition

boundaries shown by dashed vertical lines. A first-level seek operation to the partitions (not

shown in the illustration) has determined that partitions 1, 2, and 3 meet the seek condition

implied by the partitioning defined for the table and the predicate on column. That is,. The path traversed by the second-level seek portion of the skip scan operation is illustrated

by the curved line. Essentially, the skip scan operation seeks into each of these partitions for

rows that meet the condition. The total cost of the skip scan operation is the same as

that of three separate index seeks.

The execution plans of queries on partitioned tables and indexes can be examined by using the

Transact-SQL

statements

or

, or by using the

graphical execution plan output in SQL Server Management Studio. For example, you can

display the compile-time execution plan by selecting

Display Estimated Execution Plan

on the

Query Editor toolbar and the run-time plan by selecting

Include Actual Execution Plan.

Using these tools, you can ascertain the following information:

The operations such as

,

,

,

,

, and

that access

partitioned tables or indexes.

The partitions accessed by the query. For example, the total count of partitions accessed

and the ranges of contiguous partitions that are accessed are available in run-time

execution plans.

When the skip scan operation is used in a seek or scan operation to retrieve data from

one or more partitions.

provides enhanced partitioning information for both compile-time and run-time

execution plans. Execution plans now provide the following information:

An optional

attribute that indicates that an operator, such as a

,

,

,

,

, or

, is performed on a partitioned table.

A new

element with a

subelement that includes

as the leading index key column and filter conditions that specify range seeks on. The presence of two

subelements indicates that a skip scan

operation on

is used.

Summary information that provides a total count of the partitions accessed. This

information is available only in run-time plans.

To demonstrate how this information is displayed in both the graphical execution plan output

and the XML Showplan output, consider the following query on the partitioned table. This query updates data in two partitions.

The following illustration shows the properties of the

operator in the

runtime execution plan for this query. To view the definition of the

table and the

partition definition, see "Example" in this article.

```sql
T.b = 2
```

```sql
T.a
< 10
```

```sql
T
```

```sql
a
```

```sql
b
```

```sql
a
```

```sql
T.a <
10
```

```sql
b = 2
```

`SET`

```sql
SET SHOWPLAN_XML
```

```sql
SET STATISTICS XML
```

`scans`

`seeks`

`inserts`

`updates`

`merges`

`deletes`

`Partitioned`

`seek`

`scan`

`insert`

`update`

`merge`

`delete`

`SeekPredicateNew`

`SeekKeys`

`PartitionID`

`PartitionID`

`SeekKeys`

`PartitionID`

`fact_sales`

```sql
Clustered Index Seek
```

`fact_sales`

```sql
UPDATE fact_sales
SET quantity = quantity - 2
WHERE date_id
BETWEEN
20080802
AND
20080902;
```
