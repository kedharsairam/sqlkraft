---
name: 'sys.sp_help_agent_profile'
title: 'sp_help_agent_profile'
category: 'general'
description: 'Displays the profile of a specified agent. This stored procedure is executed at the Distributor on Transact-SQL syntax conventions , and can be one of these values.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_agent_profile
  [ [ @agent_type = ] agent_type ]
  [ , [ @profile_id = ] profile_id ]
  [ ; ]
---

## Description

Displays the profile of a specified agent. This stored procedure is executed at the Distributor on Transact-SQL syntax conventions , and can be one of these values.

## Syntax

```sql
sp_help_agent_profile
[ [ @agent_type = ] agent_type ]
[ , [ @profile_id = ] profile_id ]
[ ; ]
```
