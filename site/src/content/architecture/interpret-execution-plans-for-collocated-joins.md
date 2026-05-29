---
title: 'Interpret execution plans for collocated joins'
topic: 'query-processing'
description: 'The Showplan methods'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

The Showplan methods

,

, and

don't report the

partition information described in this article, with the following exception. As part of the

predicate, the partitions to be accessed are identified by a range predicate on the computed

column representing the partition ID. The following example shows the

predicate for a

operator. Partitions 2 and 3 are accessed, and the seek operator filters

on the rows that meet the condition

.

Output

A partitioned heap is treated as a logical index on the partition ID. Partition elimination on a

partitioned heap is represented in an execution plan as a

operator with a

predicate on partition ID. The following example shows the Showplan information provided:

SQL

Join collocation can occur when two tables are partitioned using the same or equivalent

partitioning function and the partitioning columns from both sides of the join are specified in

the join condition of the query. The Query Optimizer can generate a plan where the partitions

of each table that have equal partition IDs are joined separately. Collocated joins can be faster

than non-collocated joins because they can require less memory and processing time. The

Query Optimizer chooses a non-collocated plan or a collocated plan based on cost estimates.

In a collocated plan, the

join reads one or more joined table or index partitions

from the inner side. The numbers within the

operators represent the partition

numbers.

When parallel plans for collocated joins are generated for partitioned tables or indexes, a

Parallelism operator appears between the

and the

join operators.

```sql
SHOWPLAN_ALL
```

```sql
SHOWPLAN_TEXT
```

```sql
STATISTICS PROFILE
```

```sql
SEEK
```

```sql
SEEK
```

```sql
Clustered Index Seek
```

```sql
date_id BETWEEN 20080802 AND 20080902
```

```sql
Table Scan
```

```sql
SEEK
```

```sql
Nested Loops
```

```sql
Constant Scan
```

```sql
Constant Scan
```

```sql
Nested Loops
```

```sql
|--Clustered Index Seek(OBJECT:([db_sales_test].[dbo].[fact_sales].[ci]),
SEEK:([PtnId1000] >= (2) AND [PtnId1000] \<= (3)
AND [db_sales_test].[dbo].[fact_sales].[date_id] >= (20080802)
AND [db_sales_test].[dbo].[fact_sales].[date_id] <= (20080902))
ORDERED FORWARD)
```

```sql
|
-- Table Scan (OBJECT: ([db].[dbo].[T]), SEEK: ([PtnId1001]=[Expr1011]) ORDERED
FORWARD)
```
