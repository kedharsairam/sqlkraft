---
title: "Parallel query execution strategy for partitioned objects"
topic: "query-processing"
description: "In this case, multiple worker threads on the outer side of the join each read and work on a"
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

In this case, multiple worker threads on the outer side of the join each read and work on a

different partition.

The following illustration demonstrates a parallel query plan for a collocated join.

The query processor uses a parallel execution strategy for queries that select from partitioned

objects. As part of the execution strategy, the query processor determines the table partitions

required for the query, and the proportion of worker threads to allocate to each partition. In

most cases, the query processor allocates an equal or almost equal number of worker threads

to each partition, and then executes the query in parallel across the partitions. The following

paragraphs explain worker thread allocation in greater detail.

If the number of worker threads is less than the number of partitions, the query processor

assigns each worker thread to a different partition, initially leaving one or more partitions

without an assigned worker thread. When a worker thread finishes executing on a partition, the

query processor assigns it to the next partition until each partition has been assigned a single

worker thread. This is the only case in which the query processor reallocates worker threads to

other partitions.

Shows worker thread reassigned after it finishes. If the number of worker threads is equal to

the number of partitions, the query processor assigns one worker thread to each partition.

When a worker thread finishes, it isn't reallocated to another partition.

If the number of worker threads is greater than the number of partitions, the query processor

allocates an equal number of worker threads to each partition. If the number of worker threads

isn't an exact multiple of the number of partitions, the query processor allocates one additional

worker thread to some partitions in order to use all of the available worker threads. If there is

only one partition, all worker threads will be assigned to that partition. In the diagram below,

there are four partitions and 14 worker threads. Each partition has 3 worker threads assigned,

and two partitions have an additional worker thread, for a total of 14 worker thread

assignments. When a worker thread finishes, it isn't reassigned to another partition.

Although the above examples suggest a straightforward way to allocate worker threads, the

actual strategy is more complex and accounts for other variables that occur during query

execution. For example, if the table is partitioned and has a clustered index on column A and a

query has the predicate clause

, the query processor will allocate one

or more worker threads to each of these three seek values (A=13, A=17, and A=25) instead of

each table partition. It is only necessary to execute the query in the partitions that contain

these values, and if all of these seek predicates happen to be in the same table partition, all of

the worker threads will be assigned to the same table partition.

To take another example, suppose that the table has four partitions on column A with

boundary points (10, 20, 30), an index on column B, and the query has a predicate clause. Because the table partitions are based on the values of A, the values of B

can occur in any of the table partitions. Thus, the query processor will seek for each of the

three values of B (50, 100, 150) in each of the four table partitions. The query processor will

assign worker threads proportionately so that it can execute each of these 12 query scans in

parallel.

Table Partition 1: A < 10

B=50, B=100, B=150

Table Partition 2: A >= 10 AND A < 20

B=50, B=100, B=150

ﾉ

Expand table

```sql
WHERE A IN (13, 17, 25)
```

```sql
WHERE
B IN (50, 100, 150)
```
