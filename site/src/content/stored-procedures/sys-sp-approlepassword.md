---
name: "sys.sp_approlepassword"
title: "sp_approlepassword"
category: "general"
description: "Changes the password of an application role in the current database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_approlepassword
              [ @rolename = ]
              N
              'rolename'
              , [ @newpwd = ]
              N
              'newpwd'
              [ ; ]
---

## Description

Changes the password of an application role in the current database.

## Syntax

```sql
sp_approlepassword
[ @rolename = ]
N
'rolename'
, [ @newpwd = ]
N
'newpwd'
[ ; ]
```
