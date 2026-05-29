---
name: "sys.sp_serveroption"
title: "sp_serveroption"
category: "general"
description: "Sets server options for remote servers and linked servers. Transact-SQL syntax conventions The name of the server for which to set the option. The option to set for the specified server. can be any of the following values. Affects distributed query execution against linked servers. If this option is set to SQL Server assumes that all characters in the linked server are compatible with the local se"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_serveroption
  [ @server = ]
  N
  'server'
  , [ @optname = ]
  'optname'
  , [ @optvalue = ]
  N
  'optvalue'
  [ ; ]
---

## Description

Sets server options for remote servers and linked servers. Transact-SQL syntax conventions The name of the server for which to set the option. The option to set for the specified server. can be any of the following values. Affects distributed query execution against linked servers. If this option is set to SQL Server assumes that all characters in the linked server are compatible with the local server, regarding character set and collation sequence (or sort order). This enables SQL

## Syntax

```sql
sp_serveroption
[ @server = ]
N
'server'
, [ @optname = ]
'optname'
, [ @optvalue = ]
N
'optvalue'
[ ; ]
```
