---
name: 'sys.sp_syscollector_create_collection_set'
title: 'sp_syscollector_create_collection_set'
category: 'general'
description: 'Creates a new collection set. You can use this stored procedure to create a custom collection Transact-SQL syntax conventions In cases where the Windows account configured as a proxy is a non-interactive or interactive user that hasn''t yet logged in, the profile directory will not exist, and the creation of the staging directory will fail. Therefore, if you''re using a proxy account on a domain con'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_create_collection_set
  [ @name = ]
  N
  'name'
  [ , [ @target = ]
  N
  'target'
  ]
  [ , [ @collection_mode = ] collection_mode ]
  [ , [ @days_until_expiration = ] days_until_expiration ]
  [ , [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ , [ @schedule_uid = ]
  'schedule_uid'
  ]
  [ , [ @schedule_name = ]
  N
  'schedule_name'
  ]
  [ , [ @logging_level = ] logging_level ]
  [ , [ @description = ]
  N
  'description'
  ]
  , [ @collection_set_id = ] collection_set_id
  OUTPUT
  [ , [ @collection_set_uid = ]
  'collection_set_uid'
  OUTPUT
  ]
  [ ; ]
---

## Description

Creates a new collection set. You can use this stored procedure to create a custom collection Transact-SQL syntax conventions In cases where the Windows account configured as a proxy is a non-interactive or interactive user that hasn't yet logged in, the profile directory will not exist, and the creation of the staging directory will fail. Therefore, if you're using a proxy account on a domain controller, you must specify an interactive account that has been used at least

## Syntax

```sql
sp_syscollector_create_collection_set
[ @name = ]
N
'name'
[ , [ @target = ]
N
'target'
]
[ , [ @collection_mode = ] collection_mode ]
[ , [ @days_until_expiration = ] days_until_expiration ]
[ , [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ , [ @schedule_uid = ]
'schedule_uid'
]
[ , [ @schedule_name = ]
N
'schedule_name'
]
[ , [ @logging_level = ] logging_level ]
[ , [ @description = ]
N
'description'
]
, [ @collection_set_id = ] collection_set_id
OUTPUT
[ , [ @collection_set_uid = ]
'collection_set_uid'
OUTPUT
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_syscollector_create_collection_set
```

### Example 2

```sql
msdb
```

### Example 3

```sql
0
```

### Example 4

```sql
USE
msdb;
GO
EXECUTE
sp_syscollector_start_collection_set @collection_set_id = 1;
```
