---
title: "IAM pages"
topic: "query-processing"
description: ""
tags: ["query-processing","architecture"]
pubDate: 2026-05-29
---

enough free space, a new page is added, and approximately half of the original page data is

moved to the new page.

A new PFS, GAM, or SGAM page is added in the data file for every additional range that it

keeps track of.

There's a new PFS page 8,088 pages after the first PFS page, and additional PFS pages in

subsequent 8,088 page intervals. In a data file, page ID 1 is a PFS page, page ID 8088 is a PFS

page, page ID 16176 is a PFS page, and so on.

Similarly, there's a pair of GAM and SGAM pages starting from pages 2 and 3 respectively, and

repeating for every GAM interval of about 64,000 extents or 4 GiB.

The following diagram shows the first occurrence of PFS, GAM, and SGAM pages at the

beginning of a data file following the file header page. As the file grows, new PFS, GAM, and

SGAM pages appear at their respective intervals.

An

page maps the extents used by an allocation unit in a GAM

interval. An allocation unit is associated with a partition of a heap or index, and can be one of

three types:

IN_ROW_DATA

Holds non-LOB data pages, or portions of LOB data that might fit in row.

LOB_DATA

Holds LOB data pages, used by data types such as

,

,

,

, and.

ROW_OVERFLOW_DATA

Holds LOB data pages used by variable length data types such as

,

,

, or

sql_variant

when the data exceeds the 8,060-byte row size limit.

Each partition of a heap or index always contains at least one

allocation unit. It

can also contain

and

allocation units, depending on the data

types and the row sizes present in the partition.

Similar to a GAM or SGAM page, an IAM page covers a 4-GiB interval in a file. If the allocation

unit contains extents from more than one file, or more than one 4-GiB interval of a file, multiple

IAM pages are linked in an IAM chain. Therefore, each allocation unit has at least one IAM page

for each file where it has extents. There might also be more than one IAM page in a file, if the

range of the extents allocated to the allocation unit in the file exceeds the range that a single

IAM page can record. An IAM page in a file can track extents in that file, and in any other file of

the same database.

Unlike PFS, GAM, and SGAM pages that repeat at fixed intervals, IAM pages are allocated as

required for each allocation unit. The

system view

points to the first IAM page for an allocation unit. All the IAM pages for that allocation unit are

linked in an IAM chain.

）

Important

The

system view isn't supported and is subject to

change. Compatibility isn't guaranteed. This view isn't available in Azure SQL Database.

## DCM pages

`IN_ROW_DATA`

`LOB_DATA`

`ROW_OVERFLOW_DATA`

`sys.system_internals_allocation_units`

`sys.system_internals_allocation_units`
