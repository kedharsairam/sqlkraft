---
name: "sys.sp_serveroption"
title: "sp_serveroption"
category: "general"
description: "Sets server options for remote servers and linked servers."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_serveroption
              [ @server = ]
              N
              'server'
              , [ @optname = ]
              'optname'
              , [ @optvalue = ]
              N
              'optvalue'
              [ ; ]
---

## Description

Sets server options for remote servers and linked servers.

## Syntax

```sql
sp_serveroption
[ @server = ]
N
'server'
, [ @optname = ]
'optname'
, [ @optvalue = ]
N
'optvalue'
[ ; ]
```
