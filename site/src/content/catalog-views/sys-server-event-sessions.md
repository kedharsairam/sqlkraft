---
name: 'sys.server_event_sessions'
title: 'sys.server_event_sessions'
category: 'compatibility'
description: 'Lists all the server-scoped event session definitions that exist in SQL Server or Azure SQL The unique ID of the event session. Not nullable. The user-defined name for identifying the event session. name Determines how event loss is handled. The default is nullable. Can be one of the following values: Describes how event loss is handled. The default is . Not nullable. Can be one of the . Events ca'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  event_retention_mode_desc =
  ALLOW_SINGLE_EVENT_LOSS
  M
---

## Description

Lists all the server-scoped event session definitions that exist in SQL Server or Azure SQL The unique ID of the event session. Not nullable. The user-defined name for identifying the event session. name Determines how event loss is handled. The default is nullable. Can be one of the following values: Describes how event loss is handled. The default is . Not nullable. Can be one of the . Events can be lost from the session.

## Syntax

```sql
event_retention_mode_desc =
ALLOW_SINGLE_EVENT_LOSS
M
```
