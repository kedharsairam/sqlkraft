---
title: "Read index pages"
topic: "index-architecture"
description: "The storage engine reads index pages serially in key order."
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

The storage engine reads index pages serially in key order. For example, this illustration shows

a simplified representation of a set of leaf pages that contains a set of keys and the

intermediate index node mapping the leaf pages. For more information about the structure of

pages in an index, see

Clustered and nonclustered indexes.

The storage engine uses the information in the intermediate index page above the leaf level to

schedule serial read-aheads for the pages that contain the keys. If a request is made for all the

keys from

to

, the storage engine first reads the index page above the leaf page.

However, it doesn't just read each data page in sequence from page 504 to page 556 (the last

page with keys in the specified range). Instead, the storage engine scans the intermediate

index page and builds a list of the leaf pages that must be read. The storage engine then

schedules all the reads in key order. The storage engine also recognizes that pages 504/505

and 527/528 are contiguous and performs a single scatter read to retrieve the adjacent pages

in a single operation. When there are many pages to be retrieved in a serial operation, the

storage engine schedules a block of reads at a time. When a subset of these reads is

completed, the storage engine schedules an equal number of new reads until all the required

reads are scheduled.

The storage engine uses

prefetching

to speed base table lookups from nonclustered indexes.

The leaf rows of a nonclustered index contain pointers to the data rows that contain each

specific key value. As the storage engine reads through the leaf pages of the nonclustered

index, it also starts scheduling asynchronous reads for the data rows whose pointers were

already retrieved. This allows the storage engine to retrieve data rows from the underlying

table before it completes the scan of the nonclustered index. Prefetching is used regardless of

whether the table has a clustered index. SQL Server Enterprise edition uses more prefetching

than other editions of SQL Server, allowing more pages to be read ahead. The level of

prefetching isn't configurable in any edition. For more information about nonclustered indexes,

see

Clustered and nonclustered indexes.

`ABC`

`DEF`
