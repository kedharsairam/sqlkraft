---
name: "sys.fn_get_parameter"
title: "managed_backup.fn_get_parameter"
category: "system"
description: "2016 (13.x) and later versions Returns a table of 0, 1, or more rows of parameter and value pairs. Use this stored procedure to review all or a specific configuration settings for Smart Admin. If the parameter has never been configured, the function returns 0 rows."
tags: ["system","function"]
pubDate: "2026-05-29"
syntax: "managed_backup.fn_get_parameter ('parameter_name' | '' | NULL )"
---

## Description

2016 (13.x) and later versions Returns a table of 0, 1, or more rows of parameter and value pairs. Use this stored procedure to review all or a specific configuration settings for Smart Admin. If the parameter has never been configured, the function returns 0 rows.

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
