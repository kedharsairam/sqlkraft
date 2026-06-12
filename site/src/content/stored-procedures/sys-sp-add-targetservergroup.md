---
name: "sys.sp_add_targetservergroup"
title: "sp_add_targetservergroup"
category: "general"
description: "Adds the specified server group."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_targetservergroup [ @name = ]
              'name'
              [ ; ]
---

## Description

Adds the specified server group.

## Syntax

```sql
sp_add_targetservergroup [ @name = ]
'name'
[ ; ]
```

## Permissions

06/23/2025 syntaxsql The name of the server group to create. @name is , with no default. @name can't contain commas. (success) or (failure). None. Target server groups provide an easy way to target a job at a collection of target servers. For more information, see sp_apply_job_to_targets. SQL sp_add_targetservergroup (Transact-SQL) sp_help_targetservergroup (Transact-SQL) sp_update_targetservergroup (Transact-SQL)
