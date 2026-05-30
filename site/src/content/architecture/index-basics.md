---
title: "Index basics"
topic: "index-architecture"
description: "Think about a regular book: at the end of the book, there's an index that helps to quickly locate"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

Think about a regular book: at the end of the book, there's an index that helps to quickly locate

information within the book. The index is a sorted list of keywords and next to each keyword is

a set of page numbers pointing to the pages where each keyword can be found.

A rowstore index is similar: it's an ordered list of values and for each value there are pointers to

the data

pages

where these values are located. The index itself is also stored on pages, referred

to as

index pages

. In a regular book, if the index spans multiple pages and you have to find

pointers to all the pages that contain the word

for example, you would have to leaf

through from the start of the index until you locate the index page that contains the keyword

. From there, you follow the pointers to all the book pages. This could be optimized further

if at the very beginning of the index, you create a single page that contains an alphabetical list

of where each letter can be found. For example: "A through D - page 121", "E through G - page

122" and so on. This extra page would eliminate the step of leafing through the index to find

the starting place. Such a page doesn't exist in regular books, but it does exist in a rowstore

index. This single page is referred to as the root page of the index. The root page is the starting

page of the tree structure used by an index. Following the tree analogy, the end pages that

contain pointers to the actual data are referred to as "leaf pages" of the tree.

An index is an on-disk or in-memory structure associated with a table or view that speeds

retrieval of rows from the table or view. A rowstore index contains keys built from the values in

one or more columns in the table or view. For rowstore indexes, these keys are stored in a tree

structure (B+ tree) that enables the Database Engine to find the rows associated with the key

values quickly and efficiently.

A rowstore index stores data logically organized as a table with rows and columns, and

physically stored in a row-wise data format called

rowstore

. There's an alternative way to store

data column-wise, called

columnstore

.

The design of the right indexes for a database and its workload is a complex balancing act

between query speed, index update cost, and storage cost. Narrow disk-based rowstore

indexes, or indexes with few columns in the index key, require less storage space and a smaller

update overhead. Wide indexes, on the other hand, might improve more queries. You might

have to experiment with several different designs before finding the most efficient set of

indexes. As the application evolves, indexes might need to change to maintain optimal

performance. Indexes can be added, modified, and removed without affecting the database

schema or application design. Therefore, you shouldn't hesitate to experiment with different

indexes.

The query optimizer in the Database Engine usually chooses the most effective indexes to

execute a query. To see which indexes the query optimizer uses for a specific query, in SQL

1

### Query

### Display Estimated Execution Plan

### Include Actual Execution Plan

### Understand the characteristics of the database and the application

### Understand the characteristics of the most frequently used queries

### Understand the data distribution in the columns used in the query predicates

```sql
SQL
```

```sql
SQL
```
