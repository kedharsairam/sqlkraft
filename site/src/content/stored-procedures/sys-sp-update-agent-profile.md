---
name: "sys.sp_update_agent_profile"
title: "sp_update_agent_profile"
category: "general"
description: "Updates the profile used by a replication agent. This stored procedure is executed at the Distributor on the distribution database. , with no default, and can be one of these values."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_update_agent_profile
  [ @agent_type = ] agent_type
  , [ @agent_id = ] agent_id
  , [ @profile_id = ] profile_id
  [ ; ]
---

## Description

Updates the profile used by a replication agent. This stored procedure is executed at the Distributor on the distribution database. , with no default, and can be one of these values.

## Syntax

```sql
sp_update_agent_profile
[ @agent_type = ] agent_type
, [ @agent_id = ] agent_id
, [ @profile_id = ] profile_id
[ ; ]
```
