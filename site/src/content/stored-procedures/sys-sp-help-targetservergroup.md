---
name: "sys.sp_help_targetservergroup"
title: "sp_help_targetservergroup"
category: "general"
description: "Lists all target servers in the specified group. If no group is specified, SQL Server returns information about all target server groups."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_targetservergroup [ [ @name = ]
              N
              'name'
              ]
              [ ; ]
---

## Description

Lists all target servers in the specified group. If no group is specified, SQL Server returns information about all target server groups.

## Syntax

```sql
sp_help_targetservergroup [ [ @name = ]
N
'name'
]
[ ; ]
```
