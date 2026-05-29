---
name: 'sys.fn_virtualfilestats'
title: 'sys.fn_virtualfilestats'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

## A. Displaying statistical information for a database


## Description
Number of bytes read issued on the file.

Total amount of time, in milliseconds, that users waited for the read I/Os to

complete on the file.

Number of writes made on the file.

Number of bytes written made on the file.

Total amount of time, in milliseconds, that users waited for the write I/Os to

complete on the file.

Sum of

and

.

Value of the file handle.

Physical file size (count of bytes) on disk.

For database files, this is the same value as

in

, but is

expressed in bytes rather than pages.

For database snapshot sparse files, this is the space the operating system is

using for the file.

is a system table-valued function that gives statistical information, such as

the total number of I/Os performed on a file. You can use this function to help keep track of

the length of time users have to wait to read or write to a file. The function also helps identify

the files that encounter large numbers of I/O activity.

Requires VIEW SERVER STATE permission on the server.

The following example displays statistical information for file ID 1 in the database with an ID of

.

## B. Displaying statistical information for a named database and

## file

## C. Displaying statistical information for all databases and files

SQL

The following example displays statistical information for the log file in the

AdventureWorks2025 sample database. The system function

is used to specify the

database_id

parameter.

SQL

The following example displays statistical information for all files in all databases in the

instance of SQL Server.

SQL

DB_ID (Transact-SQL)

FILE_IDEX (Transact-SQL)

sys.database_files (Transact-SQL)

sys.master_files (Transact-SQL)

Last updated on 11/18/2025

See Also

```sql
1
```

```sql
DB_ID
```

```sql
SELECT
*
FROM
fn_virtualfilestats(1, 1);
GO
```

```sql
SELECT
*
FROM
fn_virtualfilestats(DB_ID(N
'AdventureWorks2022'
), 2);
GO
```

```sql
SELECT
*
FROM
fn_virtualfilestats(
NULL
,
NULL
);
GO
```
