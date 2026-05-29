---
title: 'PFS pages'
topic: 'query-processing'
description: 'Uniform extent, or full mixed extent'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Uniform extent, or full mixed extent

0

0

Mixed extent with free pages

0

1

To manage extents, the Database Engine uses the following conceptual algorithms:

To allocate a uniform extent, the Database Engine searches the GAM page for a

bit and

sets it to

.

To find a mixed extent with free pages, the Database Engine searches the SGAM page for

a

bit.

To allocate a mixed extent, the Database Engine searches the GAM page for a

bit, sets

it to

, and then also sets the corresponding bit on the SGAM page to

.

To deallocate an extent, the Database Engine makes sure that the bit on the GAM page is

set to

, and the bit on the SGAM page is set to

.

The Database Engine allocates extents from those available in the filegroup using a

proportional fill allocation

algorithm. For example, in a filegroup with two files, if one file has

double the free space of the other, two pages are allocated from that file for every one page

allocated from the other file. This means that if allocations continue, all files in a filegroup end

up with similar percentage of space used.

For more information, see

File and filegroup fill strategy

.

pages record the allocation status of each page and the amount of free

space on each page. A PFS page has 1 byte for each page it tracks. The byte records whether

the page is allocated, and if so, whether it's empty, 1 to 50 percent full, 51 to 80 percent full, 81

to 95 percent full, or 96 to 100 percent full.

After an extent has been allocated to an object, the Database Engine uses PFS pages to track

which pages in the extent have data or are free. This information is used when the Database

Engine allocates a new page. The amount of free space in a page is only maintained for heap

and text/LOB pages. This information is used when the Database Engine has to find a page

with enough free space available to hold a newly inserted row.

BTree indexes don't require page free space tracking because the point at which to insert a new

row is always determined by the index key values. If a page in a BTree index doesn't have

### Index Allocation Map (IAM)

### varchar(max)

### nvarchar(max)

### varbinary(max)

### xml

### json

```sql
1
```

```sql
0
```

```sql
1
```

```sql
1
```

```sql
0
```

```sql
1
```

```sql
1
```

```sql
0
```
