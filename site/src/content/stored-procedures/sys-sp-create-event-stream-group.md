---
name: "sys.sp_create_event_stream_group"
title: "sys.sp_create_event_stream_group"
category: "general"
description: "Creates an event group stream for the Transact-SQL syntax conventions Specifies the name of the event stream group you want to create. , with no default, and can't be Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During preview, this feature is subject to change. For current supportability, see"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_create_event_stream_group
  [ @stream_group_name = ]
  N
  'stream_group_name'
  , [ @destination_type = ]
  N
  'destination_type'
  , [ @destination_location = ]
  N
  'destination_location'
  , [ @destination_credential = ]
  N
  'destination_credential'
  [ , [ @max_message_size_kb = ] max_message_size_kb ]
  [ , [ @partition_key_scheme = ]
  N
  'partition_key_scheme'
  ]
  [ , [ @partition_key_column_name = ]
  N
  'partition_key_column_name'
  ]
  [ , [ @encoding = ]
  N
  'encoding'
  ]
  [ ; ]
---

## Description

Creates an event group stream for the Transact-SQL syntax conventions Specifies the name of the event stream group you want to create. , with no default, and can't be Change event streaming is currently in Azure SQL Database (preview feature database scoped configuration not required). During preview, this feature is subject to change. For current supportability, see

## Syntax

```sql
sys.sp_create_event_stream_group
[ @stream_group_name = ]
N
'stream_group_name'
, [ @destination_type = ]
N
'destination_type'
, [ @destination_location = ]
N
'destination_location'
, [ @destination_credential = ]
N
'destination_credential'
[ , [ @max_message_size_kb = ] max_message_size_kb ]
[ , [ @partition_key_scheme = ]
N
'partition_key_scheme'
]
[ , [ @partition_key_column_name = ]
N
'partition_key_column_name'
]
[ , [ @encoding = ]
N
'encoding'
]
[ ; ]
```
