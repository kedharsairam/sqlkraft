---
name: "sys.sp_clean_db_free_space"
title: "sp_clean_db_free_space"
category: "general"
description: "Removes residual information on data pages. cleans all pages in all data files of the database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_clean_db_free_space"
---

## Description

Removes residual information on data pages. cleans all pages in all data files of the database.

## Syntax

`sp_clean_db_free_space`

## Remarks

Azure SQL Managed Instance

Removes residual information on data pages.

cleans all pages in all

data files of the database.

The name of the database to clean.

, with no default.

Specifies an interval to delay before the cleanup of each page, in seconds.

@cleaning_delay

, with a default of. This delay helps reduce the load on the I/O system at the expense of

increasing the duration of the cleanup process.

(success) or

system stored procedure moves all rows on a page, including the

ghosted records if any, to the beginning of the page, and then zero-initializes the remainder of

the data space on the page. In environments where the physical security of the data files or the

## Examples

### Example 1

`sp_clean_db_free_space`

### Example 2

`sp_clean_db_free_space`

### Example 3

`sp_clean_db_free_space`

### Example 4

`db_owner`

### Example 5

`AdventureWorks2025`

### Example 6

```sql
USE master
;
GO
EXECUTE sp_clean_db_free_space @dbname = N
'AdventureWorks2022'
;
```
