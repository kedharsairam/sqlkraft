---
title: "Shrink a database"
topic: "collation"
description: "This article describes how to shrink a database in SQL Server by using Object Explorer in SQL Server M"
tags: ["collation","shrink-a-database"]
pubDate: "2025-12-01"
---

This article describes how to shrink a database in SQL Server by using Object Explorer in SQL

Server Management Studio or Transact-SQL.

Shrinking data files recovers space by moving pages of data from the end of the file to

unoccupied space closer to the front of the file. When enough free space is created at the end

of the file, data pages at end of the file can be deallocated and returned to the file system.

The database can't be made smaller than the minimum size of the database. The

minimum size is the size specified when the database was originally created, or the last

explicit size set by using a file-size-changing operation, such as. For

example, if a database was originally created with a size of 10 MB and grew to 100 MB,

the smallest size the database could be reduced to is 10 MB, even if all the data in the

database has been deleted.

You can't shrink a database while the database is being backed up. Conversely, you can't

back up a database while a shrink operation on the database is in process.

To view the current amount of free (unallocated) space in the database. For more

information, see

Display Data and Log Space Information for a Database

Consider the following information when you plan to shrink a database:

A shrink operation is most effective after an operation that creates a large amount of

unused storage space, such as a large DELETE statement, truncate table, or a drop

table operation.

Most databases require some free space to be available for regular day-to-day

operations. If you shrink a database repeatedly and notice that the database size grows

again, this indicates that the free space is required for regular operations. In these

cases, repeatedly shrinking the database is a wasted operation. Autogrow events

necessary to grow the database file(s) hinder performance.

```sql
DBCC SHRINKFILE
```
