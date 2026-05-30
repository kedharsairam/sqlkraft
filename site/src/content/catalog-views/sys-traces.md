---
name: "sys.traces"
title: "sys.traces"
category: "compatibility"
description: "catalog view contains the current running traces on the system. This view is intended as a replacement for the For a complete list of supported trace events, see SQL Server Event Class Reference Path of the trace file. This value is null when the trace is a rowset Maximum trace file size limit in megabytes (MB). This value is null when the trace is a rowset trace. Time to stop the running trace. M"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sp_trace_create
  sp_trace_setevent
  sp_trace_setfilter
  sp_trace_setstatus
---

## Description

catalog view contains the current running traces on the system. This view is intended as a replacement for the For a complete list of supported trace events, see SQL Server Event Class Reference Path of the trace file. This value is null when the trace is a rowset Maximum trace file size limit in megabytes (MB). This value is null when the trace is a rowset trace. Time to stop the running trace. Maximum number of rollover files. This value is null if the Max

## Syntax

```sql
sp_trace_create
sp_trace_setevent
sp_trace_setfilter
sp_trace_setstatus
```
