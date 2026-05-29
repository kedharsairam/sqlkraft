---
name: "sys.sp_delete_proxy"
title: "sp_delete_proxy"
category: "general"
description: "Removes the specified proxy. Transact-SQL syntax conventions The proxy identification number of the proxy to remove. , with a default of The name of the proxy to remove. , with a default of"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_delete_proxy
  [ [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ ; ]
---

## Description

Removes the specified proxy. Transact-SQL syntax conventions The proxy identification number of the proxy to remove. , with a default of The name of the proxy to remove. , with a default of

## Syntax

```sql
sp_delete_proxy
[ [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ ; ]
```

## Remarks

Applies to:

Removes the specified proxy.

Transact-SQL syntax conventions

The proxy identification number of the proxy to remove.

, with a default of

The name of the proxy to remove.

@proxy_name

, with a default of

(success) or

## Examples

### Example 1

```sql
sp_delete_proxy
```

### Example 2

```sql
Catalog application proxy
```

### Example 3

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_delete_proxy
@proxy_name = N
'Catalog application proxy'
;
GO
```
