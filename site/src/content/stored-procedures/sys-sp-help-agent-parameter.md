---
name: 'sys.sp_help_agent_parameter'
title: 'sp_help_agent_parameter'
category: 'general'
description: 'Returns all the parameters of a profile from the procedure is executed at the Distributor where the agent is running, on any database. Transact-SQL syntax conventions The ID of the profile from the , which returns all parameters.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_agent_parameter [ [ @profile_id = ] profile_id ]
  [ ; ]
---

## Description

Returns all the parameters of a profile from the procedure is executed at the Distributor where the agent is running, on any database. Transact-SQL syntax conventions The ID of the profile from the , which returns all parameters.

## Syntax

```sql
sp_help_agent_parameter [ [ @profile_id = ] profile_id ]
[ ; ]
```

## Permissions

is used in all types of replication. Only members of the fixed server role or the fixed database role can execute . Work with Replication Agent Profiles sp_add_agent_parameter (Transact-SQL) sp_drop_agent_parameter (Transact-SQL) System stored procedures (Transact-SQL) Related content
