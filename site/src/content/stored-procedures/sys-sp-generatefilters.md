---
name: 'sys.sp_generatefilters'
title: 'sp_generatefilters'
category: 'general'
description: 'Creates filters on foreign key tables when a specified table is replicated. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to be filtered.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_generatefilters [ @publication = ]
  N
  'publication'
  [ ; ]
---

## Description

Creates filters on foreign key tables when a specified table is replicated. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to be filtered.

## Syntax

```sql
sp_generatefilters [ @publication = ]
N
'publication'
[ ; ]
```

## Permissions

06/23/2025 Applies to: SQL Server Creates filters on foreign key tables when a specified table is replicated. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions syntaxsql The name of the publication to be filtered. @publication is , with no default. (success) or (failure). is used in merge replication. Only members of the fixed server role or the fixed database role can execute . Related content
