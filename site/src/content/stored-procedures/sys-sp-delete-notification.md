---
name: "sys.sp_delete_notification"
title: "sp_delete_notification"
category: "general"
description: "Removes a SQL Server Agent notification definition for a specific alert and operator."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_delete_notification
      [ @alert_name = ]
      N
      'alert_name'
      , [ @operator_name = ]
      N
      'operator_name'
      [ ; ]
---

## Description

Removes a SQL Server Agent notification definition for a specific alert and operator.
## Syntax

```sql
sp_delete_notification
[ @alert_name = ]
N
'alert_name'
, [ @operator_name = ]
N
'operator_name'
[ ; ]
```

## Remarks

Removes a SQL Server Agent notification definition for a specific alert and operator.

The name of the alert.

@alert_name

, with no default.

The name of the operator.

@operator_name

, with no default.

(success) or

Removing a notification removes only the notification; the alert and the operator are left intact.

sp_delete_notification (Transact-SQL)

sp_help_notification (Transact-SQL)

sp_update_notification (Transact-SQL)

sp_add_operator (Transact-SQL)

System stored procedures (Transact-SQL)
