---
name: "sys.fn_get_current_xevent_settings"
title: "managed_backup.fn_get_current_xevent_settings"
category: "system"
description: "2016 (13.x) and later versions Returns 1 row for each Extended Event type supported by Smart Admn. Use this function to return or review the current Extended Event settings to identify the type of events that are configurable and the current configurations. This function does not have any arguments. Admin, analytic, and operational channels of the Extende"
tags: ["system","function"]
pubDate: 2026-05-29
syntax: "smart_admin.fn_get_current_xevent_settings ()"
---

## Description

2016 (13.x) and later versions Returns 1 row for each Extended Event type supported by Smart Admn. Use this function to return or review the current Extended Event settings to identify the type of events that are configurable and the current configurations. This function does not have any arguments.

## Syntax

```sql
smart_admin.fn_get_current_xevent_settings ()
```

## Examples

### Example 1

```sql
SELECT *
FROM smart_admin.fn_get_current_xevent_settings ()
```
