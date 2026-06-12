---
name: "sys.sp_unregister_custom_scripting"
title: "sp_unregister_custom_scripting"
category: "general"
description: "This stored procedure removes a user-defined custom stored procedure or Transact-SQL script file that was registered by executing executed at the Publisher on the publication database. The type of custom stored procedure or script being removed. be one of the following values. Registered custom stored procedure or script is executed when an Registered custom stored"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_unregister_custom_scripting
      [ @type = ]
      'type'
      [ , [ @publication = ]
      N
      'publication'
      ]
      [ , [ @article = ]
      N
      'article'
      ]
      [ ; ]
---

## Description

This stored procedure removes a user-defined custom stored procedure or Transact-SQL script file that was registered by executing executed at the Publisher on the publication database. The type of custom stored procedure or script being removed. be one of the following values.

## Syntax

```sql
sp_unregister_custom_scripting
[ @type = ]
'type'
[ , [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
[ ; ]
```
