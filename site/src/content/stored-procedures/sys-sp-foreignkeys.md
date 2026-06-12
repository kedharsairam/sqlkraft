---
name: "sys.sp_foreignkeys"
title: "sp_foreignkeys"
category: "general"
description: "Returns the foreign keys that reference primary keys on the table in the linked server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_foreignkeys
              [ @table_server = ]
              N
              'table_server'
              [ , [ @pktab_name = ]
              N
              'pktab_name'
              ]
              [ , [ @pktab_schema = ]
              N
              'pktab_schema'
              ]
              [ , [ @pktab_catalog = ]
              N
              'pktab_catalog'
              ]
              [ , [ @fktab_name = ]
              N
              'fktab_name'
              ]
              [ , [ @fktab_schema = ]
              N
              'fktab_schema'
              ]
              [ , [ @fktab_catalog = ]
              N
              'fktab_catalog'
              ]
              [ ; ]
---

## Description

Returns the foreign keys that reference primary keys on the table in the linked server.

## Syntax

```sql
sp_foreignkeys
[ @table_server = ]
N
'table_server'
[ , [ @pktab_name = ]
N
'pktab_name'
]
[ , [ @pktab_schema = ]
N
'pktab_schema'
]
[ , [ @pktab_catalog = ]
N
'pktab_catalog'
]
[ , [ @fktab_name = ]
N
'fktab_name'
]
[ , [ @fktab_schema = ]
N
'fktab_schema'
]
[ , [ @fktab_catalog = ]
N
'fktab_catalog'
]
[ ; ]
```
