---
name: "sys.sp_add_agent_parameter"
title: "sp_add_agent_parameter"
category: "general"
description: "Adds a new parameter and its value to an agent profile. This stored procedure is executed at the Distributor on any database. The ID of the profile from the To find out what agent type this field value. The values are as follows:"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_agent_parameter [ @profile_id = ] profile_id
  , [ @parameter_name = ]
  'parameter_name'
  , [ @parameter_value = ]
  'parameter_value'
  [ ; ]
---

## Description

Adds a new parameter and its value to an agent profile. This stored procedure is executed at the Distributor on any database. The ID of the profile from the To find out what agent type this field value. The values are as follows:

## Syntax

```sql
sp_add_agent_parameter [ @profile_id = ] profile_id
, [ @parameter_name = ]
'parameter_name'
, [ @parameter_value = ]
'parameter_value'
[ ; ]
```
