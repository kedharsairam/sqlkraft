---
title: "Parallel query example"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

Setting the max degree of parallelism option to 0 (default) enables SQL Server to use all

available processors up to a maximum of 64 processors in a parallel plan execution. Although

sets a runtime target of 64 logical processors when MAXDOP option is set to 0, a

different value can be manually set if needed. Setting MAXDOP to 0 for queries and indexes

allows SQL Server to use all available processors up to a maximum of 64 processors for the

given queries or indexes in a parallel plan execution. MAXDOP isn't an enforced value for all

parallel queries, but rather a tentative target for all queries eligible for parallelism. This means

that if not enough worker threads are available at runtime, a query might execute with a lower

degree of parallelism than the MAXDOP server configuration option.

The following query counts the number of orders placed in a specific quarter, starting on April

1, 2000, and in which at least one line item of the order was received by the customer later

than the committed date. This query lists the count of such orders grouped by each order

priority and sorted in ascending priority order.

This example uses theoretical table and column names.

Assume the following indexes are defined on the

and

tables:



Tip

For more information, see

for guidelines on configuring

MAXDOP at the server, database, query, or hint level.

Here is one possible parallel plan generated for the query previously shown:

Output

The illustration below shows a query plan executed with a degree of parallelism equal to 4 and

involving a two-table join.

The parallel plan contains three parallelism operators. Both the Index Seek operator of the

index and the Index Scan operator of the

index are

performed in parallel. This produces several exclusive streams. This can be determined from the

nearest Parallelism operators above the Index Scan and Index Seek operators, respectively.

Both are repartitioning the type of exchange. That is, they are just reshuffling data among the

streams and producing the same number of streams on their output as they have on their

input. This number of streams is equal to the degree of parallelism.

The parallelism operator above the

Index Scan operator is repartitioning its

input streams using the value of

as a key. In this way, the same values of

end up in the same output stream. At the same time, output streams maintain the

order on the

column to meet the input requirement of the Merge Join operator.

The parallelism operator above the Index Seek operator is repartitioning its input streams using

the value of. Because its input isn't sorted on the

column values and

this is the join column in the

operator, the Sort operator between the parallelism

and Merge Join operators make sure that the input is sorted for the

operator on

the join columns. The

operator, like the Merge Join operator, is performed in parallel.

The topmost parallelism operator gathers results from several streams into a single stream.

Partial aggregations performed by the Stream Aggregate operator below the parallelism

operator are then accumulated into a single

value for each different value of the

in the Stream Aggregate operator above the parallelism operator. Because

`lineitem`

`orders`

```sql
SELECT o_orderpriority,
COUNT (*)
AS
Order_Count
FROM orders
WHERE o_orderdate >=
'2000/04/01'
AND o_orderdate <
DATEADD (mm, 3,
'2000/04/01'
)
AND
EXISTS (
SELECT
*
FROM lineitem
WHERE l_orderkey = o_orderkey
AND l_commitdate < l_receiptdate
)
GROUP
BY o_orderpriority
ORDER
BY o_orderpriority
```

```sql
CREATE
INDEX l_order_dates_idx
ON lineitem (l_orderkey, l_receiptdate, l_commitdate, l_shipdate)
CREATE
UNIQUE
INDEX o_datkeyopr_idx
ON
ORDERS (o_orderdate, o_orderkey, o_custkey, o_orderpriority)
|--Stream Aggregate(GROUP BY:([ORDERS].[o_orderpriority])
DEFINE:([Expr1005]=COUNT(*)))
|--Parallelism(Gather Streams, ORDER BY:
([ORDERS].[o_orderpriority] ASC))
|--Stream Aggregate(GROUP BY:
([ORDERS].[o_orderpriority])
DEFINE:([Expr1005]=Count(*)))
|--Sort(ORDER BY:([ORDERS].[o_orderpriority] ASC))
|--Merge Join(Left Semi Join, MERGE:
([ORDERS].[o_orderkey])=
([LINEITEM].[l_orderkey]),
RESIDUAL:([ORDERS].[o_orderkey]=
[LINEITEM].[l_orderkey]))
|--Sort(ORDER BY:([ORDERS].[o_orderkey] ASC))
| |--Parallelism(Repartition Streams,
PARTITION COLUMNS:
([ORDERS].[o_orderkey]))
| |--Index Seek(OBJECT:
([tpcd1G].[dbo].[ORDERS].[O_DATKEYOPR_IDX]),
SEEK:([ORDERS].[o_orderdate] >=
Apr 1 2000 12:00AM AND
[ORDERS].[o_orderdate] <
Jul 1 2000 12:00AM) ORDERED)
|--Parallelism(Repartition Streams,
PARTITION COLUMNS:
([LINEITEM].[l_orderkey]),
ORDER BY:([LINEITEM].[l_orderkey] ASC))
|--Filter(WHERE:
([LINEITEM].[l_commitdate]<
[LINEITEM].[l_receiptdate]))
|--Index Scan(OBJECT:
([tpcd1G].[dbo].[LINEITEM].[L_ORDER_DATES_IDX]), ORDERED)
```

`o_datkey_ptr`

`l_order_dates_idx`

`l_order_dates_idx`

`L_ORDERKEY`

`L_ORDERKEY`

`L_ORDERKEY`

`O_ORDERKEY`

`O_ORDERKEY`

```sql
Merge Join
```

```sql
Merge Join
```

`Sort`

`SUM`

`O_ORDERPRIORITY`
