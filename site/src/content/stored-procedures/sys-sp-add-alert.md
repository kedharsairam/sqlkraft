---
name: 'sys.sp_add_alert'
title: 'sp_add_alert'
category: 'general'
description: 'Transact-SQL syntax conventions The name of the alert. The name appears in the e-mail or pager message sent in response to the alert. It must be unique and can contain the percent ( The message error number that defines the alert. (It usually corresponds to an error number in'
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

```sql
sp_add_alert
```

### Example 2

```sql
msdb
```

### Example 3

```sql
sys.messages
```

### Example 4

```sql
RAISERROR
```

### Example 5

```sql
WITH LOG
```

### Example 6

```sql
sys.messages
```

### Example 7

```sql
sp_altermessage
```

### Example 8

```sql
xp_logevent
```

### Example 9

```sql
xp_logevent
```

### Example 10

```sql
master
```


*(... and 9 more examples)*
