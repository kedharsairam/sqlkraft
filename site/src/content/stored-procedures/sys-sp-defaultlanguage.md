---
name: "sys.sp_defaultlanguage"
title: "sp_defaultlanguage"
category: "general"
description: "Changes the default language of for a SQL Server login. Server login, or a Windows user or group. The default language of the login. must be a valid language on the server. If server default language (defined by the Changing the server default language doesn't change the default language for existing logins. This feature will be removed in a future version of SQL Se"
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_defaultlanguage
      [ @loginame = ]
      N
      'loginame'
      [ , [ @language = ]
      N
      'language'
      ]
      [ ; ]
---

## Description

Changes the default language of for a SQL Server login. Server login, or a Windows user or group. The default language of the login. must be a valid language on the server. If server default language (defined by the Changing the server default language doesn't change the default language for existing logins. This feature will be removed in a future version of SQL Server.

## Syntax

```sql
sp_defaultlanguage
[ @loginame = ]
N
'loginame'
[ , [ @language = ]
N
'language'
]
[ ; ]
```
