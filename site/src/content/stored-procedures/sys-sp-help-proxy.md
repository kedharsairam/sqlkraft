---
name: "sys.sp_help_proxy"
title: "sp_help_proxy"
category: "general"
description: "Lists information for one or more proxies. The proxy identification number of the proxy to list information for."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_proxy
      [ [ @proxy_id = ] proxy_id ]
      [ , [ @proxy_name = ]
      N
      'proxy_name'
      ]
      [ , [ @subsystem_name = ]
      N
      'subsystem_name'
      ]
      [ , [ @name = ]
      N
      'name'
      ]
      [ ; ]
---

## Description

Lists information for one or more proxies. The proxy identification number of the proxy to list information for.

## Syntax

```sql
sp_help_proxy
[ [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ , [ @subsystem_name = ]
N
'subsystem_name'
]
[ , [ @name = ]
N
'name'
]
[ ; ]
```
