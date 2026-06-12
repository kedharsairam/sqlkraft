---
name: "sys.dm_exec_xml_handles"
title: "sys.dm_exec_xml_handles"
category: "execution"
description: "Returns information about active handles that have been opened by is specified, this function returns information about XML handles If 0 is specified, the function returns information about all XML handles for all sessions."
tags: ["execution","dmv"]
pubDate: "2026-05-29"
syntax: "dm_exec_xml_handles (session_id | 0 )"
---

## Description

Returns information about active handles that have been opened by is specified, this function returns information about XML handles If 0 is specified, the function returns information about all XML handles for all sessions.

## Syntax

```sql
dm_exec_xml_handles (session_id | 0 )
```
