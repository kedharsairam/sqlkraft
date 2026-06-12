---
name: "sys.server_event_session_events"
title: "sys.server_event_session_events"
category: "compatibility"
description: "Returns a row for each event in an event session. The ID of the event session. Is not nullable. The ID of the event. This ID is unique within an event session object. Is The name of the event. Is not nullable."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "VIEW SERVER PERFORMANCE STATE"
---

## Description

Returns a row for each event in an event session. The ID of the event session. Is not nullable. The ID of the event. This ID is unique within an event session object. Is The name of the event. Is not nullable.

## Syntax

```sql
VIEW SERVER PERFORMANCE STATE
```

## Remarks

Azure SQL Managed Instance

Returns a row for each event in an event session.

Description

The ID of the event session. Is not nullable.

The ID of the event. This ID is unique within an event session object. Is

not nullable.

The name of the event. Is not nullable.

The name of the event package that contains the event. Is not nullable.

The name of the module that contains the event. Is not nullable.

The predicate expression that is applied to the event. Is nullable.

The XML predicate expression that is applied to the event. Is nullable.

2019 (15.x) and previous versions require

permission on the server.

2022 (16.x) and later versions require

permission on the

This view has the following relationship cardinalities.

Many to one

Expand table

Expand table
