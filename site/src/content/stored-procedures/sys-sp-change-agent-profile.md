---
name: "sys.sp_change_agent_profile"
title: "sp_change_agent_profile"
category: "general"
description: "Changes a parameter of a replication agent profile stored in the stored procedure is executed at the Distributor on any database. The new value of the property. This table describes the profile properties that can be changed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_change_agent_profile
  [ @profile_id = ] profile_id
  , [ @property = ]
  N
  'property'
  , [ @value = ]
  N
  'value'
  [ ; ]
---

## Description

Changes a parameter of a replication agent profile stored in the stored procedure is executed at the Distributor on any database. The new value of the property. This table describes the profile properties that can be changed.

## Syntax

```sql
sp_change_agent_profile
[ @profile_id = ] profile_id
, [ @property = ]
N
'property'
, [ @value = ]
N
'value'
[ ; ]
```
