---
name: "sys.sp_msx_enlist"
title: "sp_msx_enlist"
category: "general"
description: "Adds the current server to the list of available servers on the master server."
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

Adds the current server to the list of available servers on the master server.

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
