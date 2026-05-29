---
name: 'sys.external_library_files'
title: 'sys.external_library_files'
category: 'databases-files'
description: 'SQL Server 2017 (14.x) and later'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

Article

•

11/18/2022

Applies to:

SQL Server 2017 (14.x) and later

Azure SQL Managed Instance

Lists a row for each file that makes up an external library.


## Description
external_library_id

int

ID of the external library object.

content

varbinary(max)

Content of the external library file artifact.

platform

tinyint

ID of the host platform on which SQL Server is installed.

platform_desc

nvarchar(60)

Name of the host platform. Valid values are

,

.

sys.external_libraries

CREATE EXTERNAL LIBRARY

ﾉ

Expand table

See also

```sql
WINDOWS
```

```sql
LINUX
```
