---
title: sys.dm_os_windows_info
name: sys.dm_os_windows_info
category: execution
description:
pubDate: 2026-05-29
---

Article

•

03/31/2025

SQL Server 2017 (14.x) and later

## Returns one row that displays operating system version information.

The type of operating system. Can be

or

.

Description of the operating system.

Microsoft Windows operating system release (version number).

For a list of values and descriptions, see

Operating system version

(Windows)

.

On Linux, this column returns an empty string.

Service pack level of the Windows operating system.

On Linux, this column returns an empty string.

Windows Stock Keeping Unit (SKU) ID. For a list of SKU IDs and

descriptions, see

GetProductInfo function

. Is nullable.

On Linux, this column returns

.

Windows locale identifier (LCID) of the operating system. For a list

of LCID values and descriptions, see

Locale IDs Assigned by

Microsoft

. Can't be

.

This view is similar to

sys.dm_os_windows_info

, adding columns to differentiate Windows and Linux.

On SQL Server 2019 (15.x) and earlier versions, the

permission on

is

granted to the public role by default. If revoked, you require

permission on the

server.

ﾉ

On SQL Server 2022 (16.x) and later versions, you require

permission on the server.

The following example returns all columns from the

view.

SQL

Here is a sample result set on Windows Server 2019 Standard:

Windows

Windows Server

2019 Standard

10.0

7

1033

Here is a sample result set on Ubuntu Linux 22.04:

Linux

Ubuntu

22.04

1033

sys.dm_os_sys_info (Transact-SQL)

sys.dm_os_windows_info (Transact-SQL)

ﾉ

ﾉ

```sql
host_platform
```

```sql
Windows
```

```sql
Linux
```

```sql
host_distribution
```

```sql
host_release
```

```sql
host_service_pack_level
```

```sql
host_sku
```

```sql
NULL
```

```sql
os_language_version
```

```sql
NULL
```

```sql
SELECT
```

```sql
sys.dm_os_host_info
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER PERFORMANCE STATE
```

```sql
sys.dm_os_host_info
```

```sql
NULL
```

```sql
SELECT
host_platform,
host_distribution,
host_release,
host_service_pack_level,
host_sku,
os_language_version
FROM
sys.dm_os_host_info;
```
