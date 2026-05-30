---
name: "sys.sp_get_backup_diagnostics"
title: "managed_backup.sp_get_backup_diagnostics"
category: "general"
description: "The following example returns all the analytical events logged for the past 30 minutes"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  USE
  msdb;
  GO
  EXECUTE
  managed_backup.sp_get_backup_diagnostics
  @xevent_channel =
  'Admin'
  ,
  @begin_time =
  '2022-06-01'
  ,
  @end_time =
  '2022-06-10'
  ;
  USE
  msdb;
  GO
  EXECUTE
  managed_backup.sp_get_backup_diagnostics @xevent_channel =
  'Analytic'
  ;
---

## Description

The following example returns all the analytical events logged for the past 30 minutes

## Syntax

```sql
USE msdb;
GO
EXECUTE managed_backup.sp_get_backup_diagnostics
@xevent_channel =
'Admin'
,
@begin_time =
'2022-06-01'
,
@end_time =
'2022-06-10'
;
USE msdb;
GO
EXECUTE managed_backup.sp_get_backup_diagnostics @xevent_channel =
'Analytic'
;
```
