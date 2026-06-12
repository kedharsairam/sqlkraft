---
name: "sys.sp_set_parameter"
title: "managed_backup.sp_set_parameter"
category: "general"
description: "2016 (13.x) and later versions Sets the value of the specified Smart Admin system parameter. The available parameters are related to SQL Server managed backup to Microsoft Azure. These parameters are used to set the email notifications, enable specific extended events, and enable user set policy based management policies. You must specify the parameter name and the Transact-SQL syntax c"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  SSMBackup2WANotificationEmailIds
              SSMBackup2WADebugXevent
              SSMBackup2WAEnableUserDefinedPolicy
              FileRetentionDebugXevent
---

## Description

2016 (13.x) and later versions Sets the value of the specified Smart Admin system parameter. The available parameters are related to SQL Server managed backup to Microsoft Azure. These parameters are used to set the email notifications, enable specific extended events, and enable user set policy based management policies. You must specify the parameter name and the ## Syntax

```sql
SSMBackup2WANotificationEmailIds
SSMBackup2WADebugXevent
SSMBackup2WAEnableUserDefinedPolicy
FileRetentionDebugXevent
```
