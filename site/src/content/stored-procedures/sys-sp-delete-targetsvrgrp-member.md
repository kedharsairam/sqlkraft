---
name: 'sys.sp_delete_targetsvrgrp_member'
title: 'sp_delete_targetsvrgrp_member'
category: 'general'
description: 'Removes a target server from a target server group. Transact-SQL syntax conventions The name of the server to remove from the specified group.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_targetsvrgrp_member
  [ @group_name = ]
  N
  'group_name'
  , [ @server_name = ]
  N
  'server_name'
  [ ; ]
---

## Description

Removes a target server from a target server group. Transact-SQL syntax conventions The name of the server to remove from the specified group.

## Syntax

```sql
sp_delete_targetsvrgrp_member
[ @group_name = ]
N
'group_name'
, [ @server_name = ]
N
'server_name'
[ ; ]
```
