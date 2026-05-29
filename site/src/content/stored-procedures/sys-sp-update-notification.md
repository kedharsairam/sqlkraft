---
name: 'sys.sp_update_notification'
title: 'sp_update_notification'
category: 'general'
description: 'Updates the notification method of an alert notification. Transact-SQL syntax conventions The name of the alert associated with this notification. The operator who is notified when the alert occurs. The method by which the operator is notified.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_notification
  [ @alert_name = ]
  N
  'alert_name'
  , [ @operator_name = ]
  N
  'operator_name'
  , [ @notification_method = ] notification_method
  [ ; ]
---

## Description

Updates the notification method of an alert notification. Transact-SQL syntax conventions The name of the alert associated with this notification. The operator who is notified when the alert occurs. The method by which the operator is notified.

## Syntax

```sql
sp_update_notification
[ @alert_name = ]
N
'alert_name'
, [ @operator_name = ]
N
'operator_name'
, [ @notification_method = ] notification_method
[ ; ]
```
