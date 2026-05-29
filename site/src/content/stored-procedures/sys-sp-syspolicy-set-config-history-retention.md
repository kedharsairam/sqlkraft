---
name: 'sys.sp_syspolicy_set_config_history_retention'
title: 'sp_syspolicy_set_config_history_retention'
category: 'general'
description: 'Specifies the number of days to keep policy evaluation history for Policy-Based Management. Transact-SQL syntax conventions The number of days to retain Policy-Based Management history. in the context of the , the history isn''t automatically removed. To view the current value for history retention, run the following query:'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_syspolicy_set_config_history_retention'
---

## Description

Specifies the number of days to keep policy evaluation history for Policy-Based Management. Transact-SQL syntax conventions The number of days to retain Policy-Based Management history. in the context of the , the history isn't automatically removed. To view the current value for history retention, run the following query:

## Syntax

```sql
sp_syspolicy_set_config_history_retention
```

## Remarks

Applies to:

Specifies the number of days to keep policy evaluation history for Policy-Based Management.

Transact-SQL syntax conventions

The number of days to retain Policy-Based Management history.

(success) or

You must run

in the context of the

, the history isn't automatically removed.

To view the current value for history retention, run the following query:

## Examples

### Example 1

```sql
SELECT
current_value
FROM
msdb.dbo.syspolicy_configuration
WHERE
name
=
'HistoryRetentionInDays'
;
```

### Example 2

```sql
EXECUTE
msdb.dbo.sp_syspolicy_set_config_history_retention @
value
= 28;
GO
```
