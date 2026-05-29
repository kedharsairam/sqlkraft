---
name: 'sys.time_zone_info'
title: 'sys.time_zone_info'
category: 'objects'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL analytics endpoint in Microsoft

Fabric

Warehouse in Microsoft Fabric


## returns information about supported time zones.

## Description
Name of the time zone in Windows standard format. For example,

or

.

Current offset to UTC. For example,

or

.

True if currently observing daylight saving time.

All time zones installed on the computer are stored in the following registry hive:

.

Any user with


## permissions can access this system catalog view.
GETUTCDATE (Transact-SQL)

AT TIME ZONE (Transact-SQL)

Date and time data types and functions (Transact-SQL)

Server-wide Configuration Catalog Views (Transact-SQL)

Last updated on 06/05/2025

ﾉ

Expand table

Related content

```sql
sys.time_zone_info
```

```sql
name
```

```sql
Cen. Australia Standard Time
```

```sql
Central European Standard Time
```

```sql
current_utc_offset
```

```sql
+01:00
```

```sql
-07:00
```

```sql
is_currently_dst
```

```sql
KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones
```

```sql
CONNECT
```
