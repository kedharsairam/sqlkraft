---
name: "sys.sp_set_session_context"
title: "sp_set_session_context"
category: "general"
description: "SQL Server 2016 (13.x) and later versions SQL analytics endpoint in Microsoft SQL database in Microsoft Fabric Sets a key-value pair in the session context. Transact-SQL syntax conventions with no default. The maximum key size is 128 bytes. The value for the specified key. frees the memory. The maximum size is 8,000 bytes."
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

SQL Server 2016 (13.x) and later versions SQL analytics endpoint in Microsoft SQL database in Microsoft Fabric Sets a key-value pair in the session context. Transact-SQL syntax conventions with no default. The maximum key size is 128 bytes. The value for the specified key. frees the memory. The maximum size is 8,000 bytes. Arguments for extended stored procedures must be entered in the specific order as

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
