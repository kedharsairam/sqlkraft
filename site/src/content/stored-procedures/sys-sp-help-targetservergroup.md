---
name: 'sys.sp_help_targetservergroup'
title: 'sp_help_targetservergroup'
category: 'general'
description: 'Lists all target servers in the specified group. If no group is specified, SQL Server returns information about all target server groups. Transact-SQL syntax conventions The name of the target server group for which to return information. Identification number of the server group'
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

Lists all target servers in the specified group. If no group is specified, SQL Server returns information about all target server groups. Transact-SQL syntax conventions The name of the target server group for which to return information. Identification number of the server group

## Syntax

```sql
sp_help_targetservergroup [ [ @name = ]
N
'name'
]
[ ; ]
```
