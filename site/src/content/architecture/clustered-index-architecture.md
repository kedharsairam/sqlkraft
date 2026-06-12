---
title: "Clustered index architecture"
topic: "index-architecture"
description: ""
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

If you don't create a clustered index, the table is stored as a heap, which is generally not

recommended.

Rowstore indexes are organized as B+ trees. Each page in an index B+ tree is called an index

node. The top node of the B+ tree is called the root node. The bottom nodes in the index are

called the leaf nodes. Any index levels between the root and the leaf nodes are collectively

known as intermediate levels. In a clustered index, the leaf nodes contain the data pages of the

underlying table. The root and intermediate level nodes contain index pages holding index

rows. Each index row contains a key value and a pointer to either an intermediate level page in

the B+ tree, or a data row in the leaf level of the index. The pages in each level of the index are

linked in a doubly linked list.

Clustered indexes have one row in

sys.partitions

for each partition used by the index, with. By default, a clustered index has a single partition. When a clustered index has

multiple partitions, each partition has a separate B+ tree structure that contains the data for

that specific partition. For example, if a clustered index has four partitions, there are four B+

tree structures, one in each partition.

Depending on the data types in the clustered index, each clustered index structure has one or

more allocation units in which to store and manage the data for a specific partition. At a

minimum, each clustered index has one

allocation unit per partition. The clustered

index also has one

allocation unit per partition if it contains large object (LOB)

columns such as. It also has one

allocation unit per partition

if it contains variable length columns that exceed the 8,060-byte row size limit.

The pages in the B+ tree structure are ordered on the value of the clustered index key. All

inserts are made on the page where the key value in the inserted row fits in the ordering

sequence among existing pages. Within a page, rows aren't necessarily stored in any physical

order. However, the page maintains a logical ordering of rows using an internal structure called

a

slot array. Entries in the slot array are maintained in the index key order.

This illustration shows the structure of a clustered index in a single partition.



Tip

When you create a

constraint, a unique index supporting the constraint is

created automatically. By default, this index is clustered; however, if this index doesn't

satisfy the desired properties of the clustered index, you can create the constraint as

nonclustered and create a different clustered index instead.

```sql
index_id = 1
```

`IN_ROW_DATA`

`LOB_DATA`

`ROW_OVERFLOW_DATA`

```sql
PRIMARY KEY
```
