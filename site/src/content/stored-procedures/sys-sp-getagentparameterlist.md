---
name: "sys.sp_getagentparameterlist"
title: "sp_getagentparameterlist"
category: "general"
description: "Returns a list of all replication agent parameters that can be set in an agent profile for the specified agent type. This stored procedure is executed at the Distributor where the agent is The replication agent for which the parameter is being added."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_getagentparameterlist [ @agent_type = ] agent_type
      [ ; ]
---

## Description

Returns a list of all replication agent parameters that can be set in an agent profile for the specified agent type. This stored procedure is executed at the Distributor where the agent is The replication agent for which the parameter is being added.

## Syntax

```sql
sp_getagentparameterlist [ @agent_type = ] agent_type
[ ; ]
```
