---
name: "sys.sp_set_session_context"
title: "sp_set_session_context"
category: "general"
description: "2016 (13.x) and later versions SQL analytics endpoint in Microsoft SQL database in Microsoft Fabric Sets a key-value pair in the session context. with no default. The maximum key size is 128 bytes. The value for the specified key. frees the memory. The maximum size is 8,000 bytes."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_set_session_context
  [ @key = ]
  N
  'key'
  , [ @value = ]
  'value'
  [ , [ @read_only = ] read_only ]
  [ ; ]
---

## Description

2016 (13.x) and later versions SQL analytics endpoint in Microsoft SQL database in Microsoft Fabric Sets a key-value pair in the session context. with no default. The maximum key size is 128 bytes. The value for the specified key. frees the memory. The maximum size is 8,000 bytes.

## Syntax

```sql
sp_set_session_context
[ @key = ]
N
'key'
, [ @value = ]
'value'
[ , [ @read_only = ] read_only ]
[ ; ]
```
