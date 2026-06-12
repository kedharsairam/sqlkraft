---
title: "View size of sparse file"
topic: "collation"
description: "This topic describes how to use Transact-SQL to verify that a SQL Server database file is a sparse file and to find out its actual and maximum sizes."
tags: ["collation","view-size-of-sparse-file"]
pubDate: 2025-12-01
---

This topic describes how to use Transact-SQL to verify that a SQL Server database file is a

sparse file and to find out its actual and maximum sizes. Sparse files, which are a feature of the

NTFS file system, are used by SQL Server database snapshots.

1. On the instance of SQL Server:

Select the

column from either

in the database snapshot or

from. The value indicates whether the file is a sparse file, as follows:

1 = File is a sparse file.

0 = File is not a sparse file.

To view the number of bytes that each sparse file of a snapshot is currently using on disk, query

the

column of the SQL Server

sys.dm_io_virtual_file_stats

dynamic

management view.

７

Note

During database snapshot creation, sparse files are created by using the file names in the

CREATE DATABASE statement. These file names are stored in

in the

column. In

(whether in the source database or in a

snapshot), the

column always contains the names of the source database

files.

７

Note

Sparse files grow in 64-kilobyte (KB) increments; thus, the size of a sparse file on disk is

always a multiple of 64 KB.
