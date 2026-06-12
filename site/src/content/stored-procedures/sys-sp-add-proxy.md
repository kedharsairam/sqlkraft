---
name: "sys.sp_add_proxy"
title: "sp_add_proxy"
category: "general"
description: "Adds the specified SQL Server Agent proxy."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_add_proxy
  [ @proxy_name = ]
  'proxy_name'
  , [ @enabled = ] is_enabled
  , [ @description = ]
  'description'
  , [ @credential_name = ]
  'credential_name'
  , [ @credential_id = ] credential_id
  , [ @proxy_id = ] id
  OUTPUT
  [ ; ]
---

## Description

Adds the specified SQL Server Agent proxy.

## Syntax

```sql
sp_add_proxy
[ @proxy_name = ]
'proxy_name'
, [ @enabled = ] is_enabled
, [ @description = ]
'description'
, [ @credential_name = ]
'credential_name'
, [ @credential_id = ] credential_id
, [ @proxy_id = ] id
OUTPUT
[ ; ]
```
