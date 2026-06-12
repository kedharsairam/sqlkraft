---
name: "sys.sp_update_notification"
title: "sp_update_notification"
category: "general"
description: "Updates the notification method of an alert notification."
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

Updates the notification method of an alert notification.

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
