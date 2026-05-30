---
name: "sys.sp_help_notification"
title: "sp_help_notification"
category: "general"
description: "Reports a list of alerts for a given operator or a list of operators for a given alert. Transact-SQL syntax conventions The type of information to be returned. , which lists the alerts assigned to the supplied operator name, or which lists the operators responsible for the supplied alert name. , and can be one of these values."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_notification
  [ @object_type = ]
  'object_type'
  , [ @name = ]
  N
  'name'
  , [ @enum_type = ]
  'enum_type'
  , [ @notification_method = ] notification_method
  [ , [ @target_name = ]
  N
  'target_name'
  ]
  [ ; ]
---

## Description

Reports a list of alerts for a given operator or a list of operators for a given alert. Transact-SQL syntax conventions The type of information to be returned. , which lists the alerts assigned to the supplied operator name, or which lists the operators responsible for the supplied alert name. , and can be one of these values.

## Syntax

```sql
sp_help_notification
[ @object_type = ]
'object_type'
, [ @name = ]
N
'name'
, [ @enum_type = ]
'enum_type'
, [ @notification_method = ] notification_method
[ , [ @target_name = ]
N
'target_name'
]
[ ; ]
```
