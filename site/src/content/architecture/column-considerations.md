---
title: "Column considerations"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

Covering indexes can improve query performance because all the data needed to meet

the requirements of the query exists within the index itself. That is, only the index pages,

and not the data pages of the table or clustered index, are required to retrieve the

requested data; therefore, reducing overall disk I/O. For example, a query of columns

and

on a table that has a composite index created on columns

,

, and

can retrieve

the specified data from the index alone.

Such indexes have all the necessary

SARGable

columns in the index key, and

non-

SARGable

columns as

included

columns. This means that all the columns needed by the

query, either in the

,

, and

clauses, or in the

or

clauses, are present in the index.

There's potentially much less I/O to execute the query, if the index is narrow enough

when compared to the rows and columns in the table itself, meaning it's a small subset of

all columns.

Consider covering indexes when retrieving a small portion of a large table, and where that

small portion is defined by a fixed predicate.

Avoid creating a covering index with too many columns because that diminishes its

benefit while inflating database storage, I/O, and memory footprint.

Write queries that insert or modify as many rows as possible in a single statement,

instead of using multiple queries to update the same rows. This reduces the index update

overhead.

When you design an index consider the following column guidelines:

Keep the length of the index key short, particularly for clustered indexes.

Columns that are of the

,

,

,

,

,

,

, and

data types can't be specified as index key columns. However, columns

with these data types can be added to a nonclustered index as nonkey (included) index

columns. For more information, see the section

Use included columns in nonclustered

indexes

in this guide.

７

Note

A

covering

index is a

that satisfies all data access by a query

directly without accessing the base table.

```sql
A
```

```sql
B
```

```sql
A
```

```sql
B
```

```sql
C
```

`WHERE`

`JOIN`

```sql
GROUP BY
```

`SELECT`

`UPDATE`
