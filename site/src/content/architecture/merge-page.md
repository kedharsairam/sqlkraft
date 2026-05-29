---
title: "Merge page"
topic: "query-processing"
description: "causes the index page to split. For an internal page, this means when there's no more room to"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

causes the index page to split. For an internal page, this means when there's no more room to

add another key value and pointer, and for a leaf page, it means that the row would be too

large to fit on the page once all the delta records are incorporated. The statistics information in

the page header for a leaf page keeps track of how much space is required to consolidate the

delta records. This information is adjusted as each new delta record is added.

A split operation is done in two atomic steps. In the following diagram, assume a leaf-page

forces a split because a key with value 5 is being inserted, and a nonleaf page exists pointing to

the end of the current leaf-level page (key value 4).

Allocate two new pages

and

, and split the rows from old

page onto these

new pages, including the newly inserted row. A new slot in the

page mapping table

is used to

store the physical address of page

. Pages

and

aren't accessible to any concurrent

operations yet. In addition, the logical pointer from

to

is set. Then, in one atomic step

update the page mapping table to change the pointer from old

to new

.

The nonleaf page points to

but there's no direct pointer from a nonleaf page to

.

is only reachable via

. To create a pointer from a nonleaf page to

, allocate a new

nonleaf page (internal index page), copy all the rows from old nonleaf page, and add a new

row to point to

. Once this is done, in one atomic step, update the page mapping table to

change the pointer from old nonleaf page to new nonleaf page.

When a

operation results in a page having less than 10 percent of the maximum page

size (8 KB), or with a single row on it, that page is merged with a contiguous page.



### Step 1:

### Step 2:

### Step 3:

When a row is deleted from a page, a delta record for the delete is added. Additionally, a check

is made to determine if the index page (nonleaf page) qualifies for merge. This check verifies if

the remaining space after deleting the row is less than 10 percent of maximum page size. If it

does qualify, the merge is performed in three atomic steps.

In the following image, assume a

operation deletes the key value 10.

A delta page representing key value

(blue triangle) is created and its pointer in the

nonleaf page

is set to the new delta page. Additionally a special merge-delta page (green

triangle) is created, and it's linked to point to the delta page. At this stage, both pages (delta

page and merge-delta page) aren't visible to any concurrent transaction. In one atomic step,

the pointer to the leaf-level page

in the page mapping table is updated to point to the

merge-delta page. After this step, the entry for key value

in

now points to the merge-

delta page.

The row representing key value

in the nonleaf page

needs to be removed, and

the entry for key value

updated to point to

. To do this, a new nonleaf page

is

allocated and all the rows from

are copied, except for the row representing key value

;

then the row for key value

is updated to point to page

. Once this is done, in one atomic

step, the page mapping table entry pointing to

is updated to point to

.

is no

longer reachable.

The leaf-level pages

and

are merged and the delta pages removed. To do this, a

new page

is allocated and the rows from

and

are merged, and the delta page

changes are included in the new

. Then, in one atomic step, the page mapping table entry

pointing to page

is updated to point to page

.



```sql
P1
```

```sql
P2
```

```sql
P1
```

```sql
P2
```

```sql
P1
```

```sql
P2
```

```sql
P1
```

```sql
P2
```

```sql
P1
```

```sql
P1
```

```sql
P1
```

```sql
P2
```

```sql
P2
```

```sql
P1
```

```sql
P2
```

```sql
P2
```

```sql
DELETE
```

```sql
DELETE
```

```sql
10
```

```sql
Pp1
```

```sql
P1
```

```sql
10
```

```sql
Pp1
```

```sql
7
```

```sql
Pp1
```

```sql
10
```

```sql
P1
```

```sql
Pp2
```

```sql
Pp1
```

```sql
7
```

```sql
10
```

```sql
P1
```

```sql
Pp1
```

```sql
Pp2
```

```sql
Pp1
```

```sql
P2
```

```sql
P1
```

```sql
P3
```

```sql
P2
```

```sql
P1
```

```sql
P3
```

```sql
P1
```

```sql
P3
```
