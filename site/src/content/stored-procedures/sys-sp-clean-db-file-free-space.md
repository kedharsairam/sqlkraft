---
name: "sys.sp_clean_db_file_free_space"
title: "sp_clean_db_file_free_space"
category: "general"
description: "Azure SQL Managed Instance Removes residual information on data pages. cleans all pages in only one file of a database. Transact-SQL syntax conventions The name of the database to clean. , with no default. The data file ID to clean. , with no default. Specifies an interval to delay before the cleanup of each page, in seconds. @cleaning_delay , with a default of . This delay helps reduce the load o"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_clean_db_file_free_space"
---

## Description

Azure SQL Managed Instance Removes residual information on data pages. cleans all pages in only one file of a database. Transact-SQL syntax conventions The name of the database to clean. , with no default. The data file ID to clean. , with no default. Specifies an interval to delay before the cleanup of each page, in seconds. @cleaning_delay , with a default of . This delay helps reduce the load on the I/O system at the expense of increasing the duration of the cleanup process.

## Syntax

```sql
sp_clean_db_file_free_space
```

## Remarks

Applies to:

Azure SQL Managed Instance

Removes residual information on data pages.

cleans all pages in

only one file of a database.

Transact-SQL syntax conventions

The name of the database to clean.

, with no default.

The data file ID to clean.

, with no default.

Specifies an interval to delay before the cleanup of each page, in seconds.

@cleaning_delay

, with a default of

. This delay helps reduce the load on the I/O system at the expense of

increasing the duration of the cleanup process.

(success) or

## Examples

### Example 1

```sql
sp_clean_db_file_free_space
```

### Example 2

```sql
sp_clean_db_file_free_space
```

### Example 3

```sql
sp_clean_db_file_free_space
```

### Example 4

```sql
sp_clean_db_file_free_space
```

### Example 5

```sql
AdventureWorks2025
```

### Example 6

```sql
USE
master
;
GO
EXECUTE
sp_clean_db_file_free_space
@dbname = N
'AdventureWorks2022'
,
@fileid = 1;
```
