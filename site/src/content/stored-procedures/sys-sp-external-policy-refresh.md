---
name: "sys.sp_external_policy_refresh"
title: "sp_external_policy_refresh"
category: "general"
description: "Forces immediate download of latest published policies for the whole instance (for every (incremental policy download). (success) or a nonzero number (failure). If there are any ongoing pull requests by the background task or by another user, the request waits until the former task is finished and starts a new pull. – This ensures that the result of calling this proc explicitly always results in a"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_external_policy_refresh [ @type = ]
              'type'
              [ ; ]
---

## Description

Forces immediate download of latest published policies for the whole instance (for every (incremental policy download). (success) or a nonzero number (failure). If there are any ongoing pull requests by the background task or by another user, the request waits until the former task is finished and starts a new pull. – This ensures that the result of calling this proc explicitly always results in a refreshed cache.

## Syntax

```sql
sp_external_policy_refresh [ @type = ]
'type'
[ ; ]
```
