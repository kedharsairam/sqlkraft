---
title: "Display partition information by using other Showplan methods"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: "2026-05-29"
---

Update

Delete

Merge

As shown in the previous illustration, this attribute is displayed in the properties of the

operator in which it is defined. In the XML Showplan output, this attribute appears as

in the

node of the operator in which it is defined.

In XML Showplan output, the

element appears in the operator in which it is

defined. It can contain up to two occurrences of the

subelement. The first

item specifies the first-level seek operation at the partition ID level of the logical index. That is,

this seek determines the partitions that must be accessed to satisfy the conditions of the query.

The second

item specifies the second-level seek portion of the skip scan operation

that occurs within each partition identified in the first-level seek.

In run-time execution plans, partition summary information provides a count of the partitions

accessed and the identity of the actual partitions accessed. You can use this information to

verify that the correct partitions are accessed in the query and that all other partitions are

eliminated from consideration.

The following information is provided:

, and.

is the total number of partitions accessed by the query.

, in XML Showplan output, is the partition summary information that

appears in the new

element in

node of the operator in which it

is defined. The following example shows the contents of the

element,

indicating that two total partitions are accessed (partitions 2 and 3).

XML

```sql
Partitioned="1"
```

`RelOp`

`SeekPredicateNew`

`SeekKeys`

`SeekKeys`

`SeekKeys`

```sql
Actual Partition Count
```

```sql
Partitions Accessed
```

```sql
Actual Partition Count
```

```sql
Partitions Accessed
```

`RuntimePartitionSummary`

`RelOp`

`RuntimePartitionSummary`

```sql
<RunTimePartitionSummary>
<PartitionsAccessed
PartitionCount
=
"2"
>
<PartitionRange
Start
=
"2"
End
=
"3"
/>
</PartitionsAccessed>
</RunTimePartitionSummary>
```
