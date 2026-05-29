---
title: 'GAM and SGAM pages'
topic: 'query-processing'
description: 'Starting with SQL Server 2019 (15.x), the'
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Starting with SQL Server 2019 (15.x), the

sys.dm_db_page_info

system function returns

information about a page in a database. The function returns one row that contains page

header data, including the object ID, index ID, and partition ID. In many cases, this function can

be used as a supported alternative for the unsupported

command.

Each data file contains a small number of special system pages that track the metadata

describing extents and pages. For example, system pages track which extents in a data file are

allocated, and how much free space pages have. This section describes these system pages.

The Database Engine uses two types of allocation maps to record extent allocation:

GAM pages record the extents have been allocated. Each GAM page covers an interval of

approximately 64,000 extents, or about 4 gigabytes (GiB) of data, called a

GAM interval

.

The GAM page has 1 bit for each extent in the interval it covers. If the bit is

, the extent

is free; if the bit is

, the extent is allocated.

SGAM pages record which extents are currently being used as mixed extents and also

have at least one unused page. Each SGAM page also covers an interval of approximately

64,000 extents, or about 4 GiB of data. The SGAM has 1 bit for each extent in the interval

it covers. If the bit is

, the extent is being used as a mixed extent and has a free page. If

the bit is

, the extent isn't used as a mixed extent, or is a mixed extent where all pages

are used.

To summarize, each extent has the following bit patterns set in the GAM and SGAM pages,

based on its current use.

Free, not being used

1

0

The

system function isn't supported and is subject

to change. Compatibility isn't guaranteed.

ﾉ

Expand table

### Page Free Space (PFS)

```sql
DBCC PAGE
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
0
```

```sql
sys.dm_db_database_page_allocations
```
