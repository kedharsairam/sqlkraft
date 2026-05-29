---
name: 'sys.fn_get_parameter'
title: 'managed_backup.fn_get_parameter'
category: 'system'
description: 'SQL Server 2016 (13.x) and later versions Returns a table of 0, 1, or more rows of parameter and value pairs. Use this stored procedure to review all or a specific configuration settings for Smart Admin. If the parameter has never been configured, the function returns 0 rows. Transact-SQL syntax conventions Name of the parameter. parameter_name is . If NULL or an empty string is supplied as an arg'
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: 'managed_backup.fn_get_parameter (''parameter_name'' | '''' | NULL )'
---

## Description

SQL Server 2016 (13.x) and later versions Returns a table of 0, 1, or more rows of parameter and value pairs. Use this stored procedure to review all or a specific configuration settings for Smart Admin. If the parameter has never been configured, the function returns 0 rows. Transact-SQL syntax conventions Name of the parameter. parameter_name is . If NULL or an empty string is supplied as an argument to the function, name-values pairs for all configured Smart Admin

## Syntax

```sql
managed_backup.fn_get_parameter ('parameter_name' | '' | NULL )
```

## Examples

### Example 1

```sql
USE MSDB
GO
SELECT *
FROM managed_backup.fn_get_parameter (NULL)
USE MSDB
GO
SELECT *
FROM managed_backup.fn_get_parameter ('SSMBackup2WANotificationEmailIds')
```
