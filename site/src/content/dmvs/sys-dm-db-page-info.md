---
name: "sys.dm_db_page_info"
title: "sys.dm_db_page_info"
category: "execution"
description: "2019 (15.x) and later versions SQL database in Microsoft Fabric Returns information about a page in a database. The function returns one row that contains the header information from the page, including the function replaces the need to use . Valid input is the ID number of a database. The default is NULL, however sending a NULL value for this parameter will result in an error. Valid"
tags: ["execution","dmv"]
pubDate: "2026-05-29"
syntax: |
  sys.dm_db_page_info (
      D
      atabase
      I
      d ,
      F
      ile
      I
      d ,
      P
      age
      I
      d ,
      M
      ode )
---

## Description

2019 (15.x) and later versions SQL database in Microsoft Fabric Returns information about a page in a database. The function returns one row that contains the header information from the page, including the function replaces the need to use. Valid input is the ID number of a database. The default is NULL, however sending a NULL value for this parameter will result in an error.

## Syntax

```sql
sys.dm_db_page_info (
D atabase
I d ,
F ile
I d ,
P age
I d ,
M ode )
```

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
