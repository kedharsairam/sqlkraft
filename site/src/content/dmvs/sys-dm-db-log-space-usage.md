---
name: 'sys.dm_db_log_space_usage'
title: 'sys.dm_db_log_space_usage'
category: 'log'
description: 'SQL database in Microsoft Fabric Returns space usage information for the transaction log. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a The occupied size of the log as a percent of the total The amount of space used since the last log backup SQL Server 2014 (12.x) and later versions, SQL Server 2019 (15.x) and earlier versions require SQ'
tags: ["log", "dmv"]
pubDate: 2026-05-29
syntax: 'total_log_size_in_bytes'
---

## Description

SQL database in Microsoft Fabric Returns space usage information for the transaction log. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a The occupied size of the log as a percent of the total The amount of space used since the last log backup SQL Server 2014 (12.x) and later versions, SQL Server 2019 (15.x) and earlier versions require SQL Server 2022 (16.x) and later versions, and Azure SQL Managed Instance require

## Syntax

```sql
total_log_size_in_bytes
```

## Permissions

SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns space usage information for the transaction log. Database ID. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a logical server. The size of the log The occupied size of the log The occupied size of the log as a percent of the total log size The amount of space used since the last log backup SQL Server 2014 (12.x) and later versions, and SQL Database. SQL Server 2019 (15.x) and earlier versions require permission. SQL Server 2022 (16.x) and later versions, and Azure SQL Managed Instance require permission. On SQL Database , , and service objectives, and for databases in , the server admin account, the Microsoft Entra admin account, or membership in the server role is required. On all other SQL Database service objectives, ７ All transaction log files are combined. ﾉ
