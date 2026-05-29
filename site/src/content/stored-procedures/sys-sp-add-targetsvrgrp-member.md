---
name: 'sys.sp_add_targetsvrgrp_member'
title: 'sp_add_targetsvrgrp_member'
category: 'general'
description: 'Adds the specified target server to the specified target server group. Transact-SQL syntax conventions The name of the server that should be added to the specified group.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_targetsvrgrp_member
  [ @group_name = ]
  'group_name'
  , [ @server_name = ]
  N
  'server_name'
  [ ; ]
---

## Description

Adds the specified target server to the specified target server group. Transact-SQL syntax conventions The name of the server that should be added to the specified group.

## Syntax

```sql
sp_add_targetsvrgrp_member
[ @group_name = ]
'group_name'
, [ @server_name = ]
N
'server_name'
[ ; ]
```
