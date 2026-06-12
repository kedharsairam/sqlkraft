---
name: "sys.sp_enumcustomresolvers"
title: "sp_enumcustomresolvers"
category: "general"
description: "Returns a list of all available business logic handlers and custom resolvers registered at the Distributor. This stored procedure is executed at the Publisher on any database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_enumcustomresolvers [ [ @distributor = ]
      N
      'distributor'
      ]
      [ ; ]
---

## Description

Returns a list of all available business logic handlers and custom resolvers registered at the Distributor. This stored procedure is executed at the Publisher on any database.

## Syntax

```sql
sp_enumcustomresolvers [ [ @distributor = ]
N
'distributor'
]
[ ; ]
```
