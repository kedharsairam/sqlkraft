---
name: 'sys.sp_add_proxy'
title: 'sp_add_proxy'
category: 'general'
description: 'Adds the specified SQL Server Agent proxy. Transact-SQL syntax conventions The name of the proxy to create. The or an empty string, the name of the proxy defaults to the Specifies whether the proxy is enabled. The , the proxy isn''t enabled, and can''t be used by a job step. A description of the proxy. The description is description allows you to document the proxy, but isn''t otherwise used by SQL S'
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

Adds the specified SQL Server Agent proxy. Transact-SQL syntax conventions The name of the proxy to create. The or an empty string, the name of the proxy defaults to the Specifies whether the proxy is enabled. The , the proxy isn't enabled, and can't be used by a job step. A description of the proxy. The description is description allows you to document the proxy, but isn't otherwise used by SQL Server Agent.

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
