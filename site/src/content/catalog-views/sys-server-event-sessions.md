---
name: "sys.server_event_sessions"
title: "sys.server_event_sessions"
category: "compatibility"
description: "Lists all the server-scoped event session definitions that exist in SQL Server or Azure SQL The unique ID of the event session. Not nullable. The user-defined name for identifying the event session. name Determines how event loss is handled. The default is nullable."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  event_retention_mode_desc =
  ALLOW_SINGLE_EVENT_LOSS
  M
---

## Description

Lists all the server-scoped event session definitions that exist in SQL Server or Azure SQL The unique ID of the event session. Not nullable. The user-defined name for identifying the event session. name Determines how event loss is handled. The default is nullable.

## Syntax

```sql
event_retention_mode_desc =
ALLOW_SINGLE_EVENT_LOSS
M
```
