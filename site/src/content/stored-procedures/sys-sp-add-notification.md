---
name: "sys.sp_add_notification"
title: "sp_add_notification"
category: "general"
description: "Sets up a notification for an alert. The alert for this notification. The operator to be notified when the alert occurs. The method by which the operator is notified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_notification [ @alert_name = ]
  'alert'
  ,
  [ @operator_name = ]
  'operator'
  ,
  [ @notification_method = ] notification_method
  [ ; ]
---

## Description

Sets up a notification for an alert. The alert for this notification. The operator to be notified when the alert occurs. The method by which the operator is notified.

## Syntax

```sql
sp_add_notification [ @alert_name = ]
'alert'
,
[ @operator_name = ]
'operator'
,
[ @notification_method = ] notification_method
[ ; ]
```
