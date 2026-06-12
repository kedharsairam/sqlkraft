---
title: "SORT_IN_TEMPDB"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  When you create or rebuild an index, by setting the SORT_IN_TEMPDB option to ON you can

  dire
tags:
  - "filestream"
  - "sort-in-tempdb"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you create or rebuild an index, by setting the SORT_IN_TEMPDB option to ON you can

direct the SQL Server Database Engine to use

to store the intermediate sort results

that are used to build the index. Although this option increases the amount of temporary disk

space that is used to create an index, the option could reduce the time that is required to

create or rebuild an index when

is on a set of disks different from that of the user

database. For more information about

, see

Configure the index create memory Server

Configuration Option.

As the Database Engine builds an index, it goes through the following phases:

The Database Engine first scans the data pages of the base table to retrieve key values

and builds an index leaf row for each data row. When the internal sort buffers have been

filled with leaf index entries, the entries are sorted and written to disk as an intermediate

sort run. The Database Engine then resumes the data page scan until the sort buffers are

again filled. This pattern of scanning multiple data pages followed by sorting and writing

a sort run continues until all the rows of the base table have been processed.

In a clustered index, the leaf rows of the index are the data rows of the table; therefore,

the intermediate sort runs contain all the data rows. In a nonclustered index, the leaf rows

may contain nonkey columns, but are generally smaller than a clustered index. If the

index keys are large, or there are several nonkey columns included in the index, a

nonclustered sort run can be large. For more information about including nonkey

columns, see

Create Indexes with Included Columns.

The Database Engine merges the sorted runs of index leaf rows into a single, sorted

stream. The sort merge component of the Database Engine starts with the first page of

each sort run, finds the lowest key in all the pages, and passes that leaf row to the index

create component. The next lowest key is processed, and then the next, and so on. When

the last leaf index row is extracted from a sort run page, the process shifts to the next

page from that sort run. When all the pages in a sort run extent have been processed, the

extent is freed. As each leaf index row is passed to the index create component, it is

included in a leaf index page in the buffer. Each leaf page is written as it is filled. As leaf

pages are written, the Database Engine also builds the upper levels of the index. Each

upper level index page is written when it is filled.
