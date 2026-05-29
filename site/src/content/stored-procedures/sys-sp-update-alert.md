---
name: 'sys.sp_update_alert'
title: 'sp_update_alert'
category: 'general'
description: 'Updates the settings of an existing alert. Transact-SQL syntax conventions The name of the alert that is to be updated.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_alert
  [ @name = ]
  N
  'name'
  [ , [ @new_name = ]
  N
  'new_name'
  ]
  [ , [ @enabled = ] enabled ]
  [ , [ @message_id = ] message_id ]
  [ , [ @severity = ] severity ]
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
  [ , [ @job_id = ]
  'job_id'
  ]
  [ , [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @occurrence_count = ] occurrence_count ]
  [ , [ @count_reset_date = ] count_reset_date ]
  [ , [ @count_reset_time = ] count_reset_time ]
  [ , [ @last_occurrence_date = ] last_occurrence_date ]
  [ , [ @last_occurrence_time = ] last_occurrence_time ]
  [ , [ @last_response_date = ] last_response_date ]
  [ , [ @last_response_time = ] last_response_time ]
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

Updates the settings of an existing alert. Transact-SQL syntax conventions The name of the alert that is to be updated.

## Syntax

```sql
sp_update_alert
[ @name = ]
N
'name'
[ , [ @new_name = ]
N
'new_name'
]
[ , [ @enabled = ] enabled ]
[ , [ @message_id = ] message_id ]
[ , [ @severity = ] severity ]
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
[ , [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @occurrence_count = ] occurrence_count ]
[ , [ @count_reset_date = ] count_reset_date ]
[ , [ @count_reset_time = ] count_reset_time ]
[ , [ @last_occurrence_date = ] last_occurrence_date ]
[ , [ @last_occurrence_time = ] last_occurrence_time ]
[ , [ @last_response_date = ] last_response_date ]
[ , [ @last_response_time = ] last_response_time ]
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
