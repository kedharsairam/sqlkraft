---
name: "sys.sp_add_alert"
title: "sp_add_alert"
category: "general"
description: "Transact-SQL syntax conventions The name of the alert. The name appears in the e-mail or pager message sent in response to the alert. It must be unique and can contain the percent ( The message error number that defines the alert. (It usually corresponds to an error number in"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_alert [ @name = ]
  N
  'name'
  [ , [ @message_id = ] message_id ]
  [ , [ @severity = ] severity ]
  [ , [ @enabled = ] enabled ]
  [ , [ @delay_between_responses = ] delay_between_responses ]
  [ , [ @notification_message = ]
  N
  'notification_message'
  ]
  [ , [ @include_event_description_in = ] include_event_description_in ]
  [ , [ @database_name = ]
  N
  'database_name'
  ]
  [ , [ @event_description_keyword = ]
  N
  'event_description_keyword'
  ]
  [ , { [ @job_id = ] job_id | [ @job_name = ]
  N
  'job_name'
  } ]
  [ , [ @raise_snmp_trap = ] raise_snmp_trap ]
  [ , [ @performance_condition = ]
  N
  'performance_condition'
  ]
  [ , [ @category_name = ]
  N
  'category_name'
  ]
  [ , [ @wmi_namespace = ]
  N
  'wmi_namespace'
  ]
  [ , [ @wmi_query = ]
  N
  'wmi_query'
  ]
  [ ; ]
---

## Description

Transact-SQL syntax conventions The name of the alert. The name appears in the e-mail or pager message sent in response to the alert. It must be unique and can contain the percent ( The message error number that defines the alert. (It usually corresponds to an error number in

## Syntax

```sql
sp_add_alert [ @name = ]
N
'name'
[ , [ @message_id = ] message_id ]
[ , [ @severity = ] severity ]
[ , [ @enabled = ] enabled ]
[ , [ @delay_between_responses = ] delay_between_responses ]
[ , [ @notification_message = ]
N
'notification_message'
]
[ , [ @include_event_description_in = ] include_event_description_in ]
[ , [ @database_name = ]
N
'database_name'
]
[ , [ @event_description_keyword = ]
N
'event_description_keyword'
]
[ , { [ @job_id = ] job_id | [ @job_name = ]
N
'job_name'
} ]
[ , [ @raise_snmp_trap = ] raise_snmp_trap ]
[ , [ @performance_condition = ]
N
'performance_condition'
]
[ , [ @category_name = ]
N
'category_name'
]
[ , [ @wmi_namespace = ]
N
'wmi_namespace'
]
[ , [ @wmi_query = ]
N
'wmi_query'
]
[ ; ]
```

## Examples

### Example 1

`sp_add_alert`

### Example 2

`msdb`

### Example 3

`sys.messages`

### Example 4

`RAISERROR`

### Example 5

```sql
WITH LOG
```

### Example 6

`sys.messages`

### Example 7

`sp_altermessage`

### Example 8

`xp_logevent`

### Example 9

`xp_logevent`

### Example 10

`master`

_(... and 9 more examples)_
