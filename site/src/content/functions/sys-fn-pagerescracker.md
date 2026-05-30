---
name: "sys.fn_pagerescracker"
title: "sys.fn_PageResCracker"
category: "system"
description: "SQL Server 2019 (15.x) Transact-SQL syntax conventions Is the 8-byte hexadecimal format of a database page resource. is used to convert the 8-byte hexadecimal representation of a database page to a rowset that contains the database ID, file ID and page ID of the page. You can obtain a valid page resource from the sys.dm_exec_requests (Transact-SQL) dynamic management view or the sys.sysprocesses s"
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_PageResCracker"
---

## Description

SQL Server 2019 (15.x) Transact-SQL syntax conventions Is the 8-byte hexadecimal format of a database page resource. is used to convert the 8-byte hexadecimal representation of a database page to a rowset that contains the database ID, file ID and page ID of the page. You can obtain a valid page resource from the sys.dm_exec_requests (Transact-SQL) dynamic management view or the sys.sysprocesses system view. If an invalid page resource is used then the return is NULL. The primary use of is to facilitate joins between these views and the

## Syntax

`sys.fn_PageResCracker`

## Remarks

Applies to:

SQL Server 2019 (15.x)

Returns the

for the given

Transact-SQL syntax conventions

page_resource

Is the 8-byte hexadecimal format of a database page resource.

Description

Database ID

is used to convert the 8-byte hexadecimal representation of a database

page to a rowset that contains the database ID, file ID and page ID of the page.

You can obtain a valid page resource from the

column of the

sys.dm_exec_requests (Transact-SQL)

dynamic management view or the

sys.sysprocesses

(Transact-SQL)

system view. If an invalid page resource is used then the return is NULL.

The primary use of

is to facilitate joins between these views and the

Expand table

## Examples

### Example 1

```sql
VIEW SERVER STATE
```

### Example 2

`sys.fn_PageResCracker`

### Example 3

```sql
SELECT page_info.*
FROM sys.dm_exec_requests
AS d
CROSS
APPLY sys.fn_PageResCracker (d.page_resource)
AS r
CROSS
APPLY sys.dm_db_page_info(r.db_id, r.file_id, r.page_id,
'DETAILED'
)
AS page_info
```
