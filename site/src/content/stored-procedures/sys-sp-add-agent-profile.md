---
name: "sys.sp_add_agent_profile"
title: "sp_add_agent_profile"
category: "general"
description: "Creates a new profile for a replication agent. This stored procedure is executed at the Transact-SQL syntax conventions The ID associated with the newly inserted profile. parameter. If specified, the value is set to the new profile ID. The type of replication agent."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_agent_profile [ [ @profile_id = ] profile_id
  OUTPUT
  ]
  , [ @profile_name = ]
  'profile_name'
  , [ @agent_type = ] agent_type
  [ , [ @profile_type = ] profile_type ]
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @default = ] default ]
---

## Description

Creates a new profile for a replication agent. This stored procedure is executed at the Transact-SQL syntax conventions The ID associated with the newly inserted profile. parameter. If specified, the value is set to the new profile ID. The type of replication agent. , with no default, and can be one of these

## Syntax

```sql
sp_add_agent_profile [ [ @profile_id = ] profile_id
OUTPUT
]
, [ @profile_name = ]
'profile_name'
, [ @agent_type = ] agent_type
[ , [ @profile_type = ] profile_type ]
[ , [ @description = ]
N
'description'
]
[ , [ @default = ] default ]
```

## Permissions

When is executed, a row is added for the new custom profile in the MSagent_profiles table and the associated default parameters for this profile are added to the MSagent_parameters table. Only members of the fixed server role can execute . Work with Replication Agent Profiles Replication Agent Profiles sp_add_agent_parameter (Transact-SQL) sp_change_agent_parameter (Transact-SQL) sp_change_agent_profile (Transact-SQL) sp_drop_agent_parameter (Transact-SQL) sp_drop_agent_profile (Transact-SQL) sp_help_agent_parameter (Transact-SQL) sp_help_agent_profile (Transact-SQL) Related content sp_add_agent_profile (Transact-SQL) sp_change_agent_profile (Transact-SQL) sp_help_agent_profile (Transact-SQL) System stored procedures (Transact-SQL) Work with Replication Agent Profiles sp_add_agent_profile (Transact-SQL) sp_drop_agent_profile (Transact-SQL) sp_help_agent_parameter (Transact-SQL) Related content
