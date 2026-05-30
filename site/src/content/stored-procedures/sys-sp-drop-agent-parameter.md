---
name: "sys.sp_drop_agent_parameter"
title: "sp_drop_agent_parameter"
category: "general"
description: "Drops one or all parameters from a profile in the table. This stored procedure is executed at the Distributor where the agent is running, on any database. Transact-SQL syntax conventions The ID of the profile for which a parameter is to be dropped. , with no default. The name of the parameter to be dropped. @parameter_name , with a default of , all parameters for the specified profile are dropped."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_drop_agent_parameter"
---

## Description

Drops one or all parameters from a profile in the table. This stored procedure is executed at the Distributor where the agent is running, on any database. Transact-SQL syntax conventions The ID of the profile for which a parameter is to be dropped. , with no default. The name of the parameter to be dropped. @parameter_name , with a default of , all parameters for the specified profile are dropped. is used in all types of replication.

## Syntax

`sp_drop_agent_parameter`

## Permissions

Only members of the fixed server role can execute . sp_add_agent_parameter (Transact-SQL) sp_help_agent_parameter (Transact-SQL) System stored procedures (Transact-SQL) Related content

## Remarks

Applies to:

Drops one or all parameters from a profile in the

table. This stored

procedure is executed at the Distributor where the agent is running, on any database.

Transact-SQL syntax conventions

The ID of the profile for which a parameter is to be dropped.

@profile_id

, with no default.

The name of the parameter to be dropped.

@parameter_name

, with a default of

, all parameters for the specified profile are dropped.

(success) or

is used in all types of replication.
