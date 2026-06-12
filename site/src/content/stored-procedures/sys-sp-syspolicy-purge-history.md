---
name: "sys.sp_syspolicy_purge_history"
title: "sp_syspolicy_purge_history"
category: "general"
description: "Removes the policy evaluation history according to the history retention interval setting. This stored procedure has no parameters. To view the history retention interval, you can use the following query: If the history retention interval is set to , policy evaluation history isn't removed."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_syspolicy_purge_history"
---

## Description

Removes the policy evaluation history according to the history retention interval setting. This stored procedure has no parameters. To view the history retention interval, you can use the following query: If the history retention interval is set to , policy evaluation history isn't removed.

## Syntax

`sp_syspolicy_purge_history`

## Permissions

06/23/2025 syntaxsql This stored procedure has no parameters. (success) or (failure). You must run in the context of the system database. To view the history retention interval, you can use the following query: SQL If the history retention interval is set to , policy evaluation history isn't removed.

## Examples

### Example 1

```sql
EXECUTE msdb.dbo.sp_syspolicy_purge_history;
GO
```
