---
name: "sys.sp_helptrigger"
title: "sp_helptrigger"
category: "general"
description: "Returns the type or types of data manipulation language (DML) triggers defined on the specified table for the current database. can't be used with data definition language (DDL) triggers. Query the The name of the table in the current database for which to return trigger information."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helptrigger
      [ @tabname = ]
      N
      'tabname'
      [ , [ @triggertype = ]
      'triggertype'
      ]
      [ ; ]
---

## Description

Returns the type or types of data manipulation language (DML) triggers defined on the specified table for the current database. can't be used with data definition language (DDL) triggers. Query the The name of the table in the current database for which to return trigger information. The type of DML trigger to return information about.

## Syntax

```sql
sp_helptrigger
[ @tabname = ]
N
'tabname'
[ , [ @triggertype = ]
'triggertype'
]
[ ; ]
```
