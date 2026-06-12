---
name: "sys.sp_change_agent_parameter"
title: "sp_change_agent_parameter"
category: "general"
description: "Changes a parameter of a replication agent profile stored in the table. This stored procedure is executed at the Distributor where the agent is running, on any profiles, the parameters that can be changed depend on the type of agent. To find out what If a parameter is supported for a given , but isn't defined in the agent profile, an error is returned."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_change_agent_parameter
      [ @profile_id = ] profile_id
      , [ @parameter_name = ]
      N
      'parameter_name'
      , [ @parameter_value = ]
      N
      'parameter_value'
      [ ; ]
---

## Description

Changes a parameter of a replication agent profile stored in the table. This stored procedure is executed at the Distributor where the agent is running, on any profiles, the parameters that can be changed depend on the type of agent. To find out what If a parameter is supported for a given , but isn't defined in the agent profile, an error is returned. To add a parameter to an agent profile, you must execute

## Syntax

```sql
sp_change_agent_parameter
[ @profile_id = ] profile_id
, [ @parameter_name = ]
N
'parameter_name'
, [ @parameter_value = ]
N
'parameter_value'
[ ; ]
```
