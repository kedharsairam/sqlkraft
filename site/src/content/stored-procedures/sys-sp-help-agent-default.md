---
name: "sys.sp_help_agent_default"
title: "sp_help_agent_default"
category: "general"
description: "Retrieves the ID of the default configuration for the agent type passed as parameter. This stored procedure is executed at Distributor on any database. Transact-SQL syntax conventions The ID of the default configuration for the type of agent. parameter and returns the ID of the default configuration for the , with no default, and can be one of the following values:"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_agent_default [ @profile_id = ] profile_id
  OUTPUT
  , [ @agent_type = ] agent_type
  [ ; ]
---

## Description

Retrieves the ID of the default configuration for the agent type passed as parameter. This stored procedure is executed at Distributor on any database. Transact-SQL syntax conventions The ID of the default configuration for the type of agent. parameter and returns the ID of the default configuration for the , with no default, and can be one of the following values:

## Syntax

```sql
sp_help_agent_default [ @profile_id = ] profile_id
OUTPUT
, [ @agent_type = ] agent_type
[ ; ]
```
