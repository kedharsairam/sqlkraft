---
name: "sys.sp_syspolicy_set_log_on_success"
title: "sp_syspolicy_set_log_on_success"
category: "general"
description: "Specifies whether successful policy evaluations are logged in the Policy History log for Policy- Based Management. Determines whether successful policy evaluations are logged. one of the following values: - Successful policy evaluations aren't logged. - Successful policy evaluations are logged. in the context of the system database. , only failed policy evaluations"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_syspolicy_set_log_on_success"
---

## Description

Specifies whether successful policy evaluations are logged in the Policy History log for Policy- Based Management. Determines whether successful policy evaluations are logged. one of the following values: - Successful policy evaluations aren't logged. - Successful policy evaluations are logged. in the context of the system database. , only failed policy evaluations are logged.

## Syntax

`sp_syspolicy_set_log_on_success`

## Remarks

Specifies whether successful policy evaluations are logged in the Policy History log for Policy-

Based Management.

Determines whether successful policy evaluations are logged.

, and can be

one of the following values:

- Successful policy evaluations aren't logged.

- Successful policy evaluations are logged.

(success) or

You must run

in the context of the

system database.

, only failed policy evaluations are logged.

## Examples

### Example 1

```sql
EXECUTE msdb.dbo.sp_syspolicy_set_log_on_success @
value
= 1;
GO
```
