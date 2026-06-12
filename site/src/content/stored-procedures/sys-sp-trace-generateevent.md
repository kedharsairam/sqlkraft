---
name: "sys.sp_trace_generateevent"
title: "sp_trace_generateevent"
category: "general"
description: "Creates a user-defined event. The event can be collected using , with no default. The ID must be in the range from inclusive. This range represents user-defined events. In SQL Trace, use to add an event with this ID to a trace to capture events with the same ID fired from this stored procedure. deprecated. All other SQL Trace related stored procedures are Arguments"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_trace_generateevent
      [ @eventid = ] eventid
      [ , [ @userinfo = ]
      N
      'userinfo'
      ]
      [ , [ @userdata = ] userdata ]
      [ ; ]
---

## Description

Creates a user-defined event. The event can be collected using , with no default. The ID must be in the range from inclusive. This range represents user-defined events. In SQL Trace, use to add an event with this ID to a trace to capture events with the same ID fired from this stored procedure. deprecated.

## Syntax

```sql
sp_trace_generateevent
[ @eventid = ] eventid
[ , [ @userinfo = ]
N
'userinfo'
]
[ , [ @userdata = ] userdata ]
[ ; ]
```
