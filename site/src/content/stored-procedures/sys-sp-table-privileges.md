---
name: "sys.sp_table_privileges"
title: "sp_table_privileges"
category: "general"
description: "Returns a list of table permissions (such as The table used to return catalog information. Wildcard pattern matching is supported. The table owner of the table used to return catalog information. Wildcard pattern matching is supported. If the owner isn't specified, the default table visibility rules of the underlying DBMS apply."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_table_privileges
              [ @table_name = ]
              N
              'table_name'
              [ , [ @table_owner = ]
              N
              'table_owner'
              ]
              [ , [ @table_qualifier = ]
              N
              'table_qualifier'
              ]
              [ , [ @f
              U
              se
              P
              attern = ] f
              U
              se
              P
              attern ]
              [ ; ]
---

## Description

Returns a list of table permissions (such as The table used to return catalog information. Wildcard pattern matching is supported. The table owner of the table used to return catalog information. Wildcard pattern matching is supported. If the owner isn't specified, the default table visibility rules of the underlying DBMS apply. If the current user owns a table with the specified name, the columns of that table are returned.

## Syntax

```sql
sp_table_privileges
[ @table_name = ]
N
'table_name'
[ , [ @table_owner = ]
N
'table_owner'
]
[ , [ @table_qualifier = ]
N
'table_qualifier'
]
[ , [ @f
U se
P attern = ] f
U se
P attern ]
[ ; ]
```
