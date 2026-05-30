---
name: "sys.dm_os_host_info"
title: "sys.dm_os_host_info"
category: "os"
description: "SQL Server 2017 (14.x) and later Returns one row that displays operating system version information. The type of operating system. Can be Description of the operating system. Microsoft Windows operating system release (version number). For a list of values and descriptions, see On Linux, this column returns an empty string. Service pack level of the Windows operating system. On Linux, this column "
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: "host_service_pack_level"
---

## Description

SQL Server 2017 (14.x) and later Returns one row that displays operating system version information. The type of operating system. Can be Description of the operating system. Microsoft Windows operating system release (version number). For a list of values and descriptions, see On Linux, this column returns an empty string. Service pack level of the Windows operating system. On Linux, this column returns an empty string.

## Syntax

`host_service_pack_level`

## Permissions

Article • 03/31/2025 SQL Server 2017 (14.x) and later Returns one row that displays operating system version information. The type of operating system. Can be or . Description of the operating system. Microsoft Windows operating system release (version number). For a list of values and descriptions, see Operating system version (Windows) . On Linux, this column returns an empty string. Service pack level of the Windows operating system. On Linux, this column returns an empty string. Windows Stock Keeping Unit (SKU) ID. For a list of SKU IDs and descriptions, see GetProductInfo function . Is nullable. On Linux, this column returns . Windows locale identifier (LCID) of the operating system. For a list of LCID values and descriptions, see Locale IDs Assigned by Microsoft . Can't be . This view is similar to sys.dm_os_windows_info , adding columns to differentiate Windows and Linux. On SQL Server 2019 (15.x) and earlier versions, the permission on is granted to the public role by default. If revoked, you require permission on the server. ﾉ
