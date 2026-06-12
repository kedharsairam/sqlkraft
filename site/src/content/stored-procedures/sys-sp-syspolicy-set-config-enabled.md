---
name: "sys.sp_syspolicy_set_config_enabled"
title: "sp_syspolicy_set_config_enabled"
category: "general"
description: "Enables or disables Policy-Based Management. Determines whether Policy-Based Management is enabled."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_syspolicy_set_config_enabled"
---

## Description

Enables or disables Policy-Based Management. Determines whether Policy-Based Management is enabled.

## Syntax

`sp_syspolicy_set_config_enabled`

## Permissions

SQL) 06/23/2025 syntaxsql Determines whether Policy-Based Management is enabled. @value is sqlvariant , and can be one of the following values: 0 or - Disabled 1 or - Enabled (success) or (failure). You must run in the context of the system database. Requires membership in the fixed database role.

## Examples

### Example 1

```sql
EXECUTE msdb.dbo.sp_syspolicy_set_config_enabled @
value
= 1;
GO
```
