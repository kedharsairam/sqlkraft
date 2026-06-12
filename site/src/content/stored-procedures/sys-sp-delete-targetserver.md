---
name: "sys.sp_delete_targetserver"
title: "sp_delete_targetserver"
category: "general"
description: "Removes the specified server from the list of available target servers."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_targetserver
  [ @server_name = ]
  N
  'server_name'
  [ , [ @clear_downloadlist = ] clear_downloadlist ]
  [ , [ @post_defection = ] post_defection ]
  [ ; ]
---

## Description

Removes the specified server from the list of available target servers.

## Syntax

```sql
sp_delete_targetserver
[ @server_name = ]
N
'server_name'
[ , [ @clear_downloadlist = ] clear_downloadlist ]
[ , [ @post_defection = ] post_defection ]
[ ; ]
```
