---
name: "sys.fn_get_health_status"
title: "managed_backup.fn_get_health_status"
category: "system"
description: "SQL Server 2016 (13.x) and later versions Returns a table of 0, one or more rows of aggregated count of the errors reported by Extended Events for a specified period of time. The function is used to report health status of services under Smart Admin. Currently SQL Server managed backup to Microsoft Azure is supported under the Smart Admin umbrella. So the errors returned are related to SQL Server"
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: |
  managed_backup.fn_get_health_status([@begin_time = ] 'time_1' , [ @end_time = ]
  'time_2')
---

## Description

SQL Server 2016 (13.x) and later versions Returns a table of 0, one or more rows of aggregated count of the errors reported by Extended Events for a specified period of time. The function is used to report health status of services under Smart Admin. Currently SQL Server managed backup to Microsoft Azure is supported under the Smart Admin umbrella. So the errors returned are related to SQL Server managed backup to Microsoft Azure.

## Syntax

```sql
managed_backup.fn_get_health_status([@begin_time = ] 'time_1' , [ @end_time = ]
'time_2')
```
