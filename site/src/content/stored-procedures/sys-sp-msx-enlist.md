---
name: 'sys.sp_msx_enlist'
title: 'sp_msx_enlist'
category: 'general'
description: 'Adds the current server to the list of available servers on the master server. Transact-SQL syntax conventions The name of the multiserver administration (master) server. The location of the target server to add. stored procedure edits the registry. Manual editing of the registry isn''t recommended, because inappropriate or incorrect changes can cause serious configuration problems for your system.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_msx_enlist
  [ @msx_server_name = ]
  N
  'msx_server_name'
  [ , [ @location = ]
  N
  'location'
  ]
  [ ; ]
---

## Description

Adds the current server to the list of available servers on the master server. Transact-SQL syntax conventions The name of the multiserver administration (master) server. The location of the target server to add. stored procedure edits the registry. Manual editing of the registry isn't recommended, because inappropriate or incorrect changes can cause serious configuration problems for your system. Therefore, only experienced users should use the

## Syntax

```sql
sp_msx_enlist
[ @msx_server_name = ]
N
'msx_server_name'
[ , [ @location = ]
N
'location'
]
[ ; ]
```
