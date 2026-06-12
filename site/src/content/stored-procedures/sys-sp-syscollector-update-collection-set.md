---
name: "sys.sp_syscollector_update_collection_set"
title: "sp_syscollector_update_collection_set"
category: "general"
description: "Used to modify the properties of a user-defined collection set or to rename a user-defined In cases where the Windows account configured as a proxy is a non-interactive or interactive user that hasn't yet logged in, the profile directory will not exist, and the creation of the staging directory will fail. Therefore, if you're using a proxy account on a domain contro"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_syscollector_update_collection_set
              [ [ @collection_set_id = ] collection_set_id ]
              [ , [ @name = ]
              N
              'name'
              ]
              [ , [ @new_name = ]
              N
              'new_name'
              ]
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
              [ ; ]
---

## Description

Used to modify the properties of a user-defined collection set or to rename a user-defined In cases where the Windows account configured as a proxy is a non-interactive or interactive user that hasn't yet logged in, the profile directory will not exist, and the creation of the staging directory will fail.

## Syntax

```sql
sp_syscollector_update_collection_set
[ [ @collection_set_id = ] collection_set_id ]
[ , [ @name = ]
N
'name'
]
[ , [ @new_name = ]
N
'new_name'
]
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
[ ; ]
```
