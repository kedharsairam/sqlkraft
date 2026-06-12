---
name: "sys.sp_addscriptexec"
title: "sp_addscriptexec"
category: "general"
description: "file) to all Subscribers of a publication. This stored procedure is executed at the Publisher on the publication database. The full path to the SQL script file. Indicates whether the Distribution Agent or Merge Agent should stop when an error is encountered during script processing. = the agent continues the script and ignores the error."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_addscriptexec
      [ @publication = ]
      N
      'publication'
      , [ @scriptfile = ]
      N
      'scriptfile'
      [ , [ @skiperror = ] skiperror ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ ; ]
---

## Description

file) to all Subscribers of a publication. This stored procedure is executed at the Publisher on the publication database. The full path to the SQL script file. Indicates whether the Distribution Agent or Merge Agent should stop when an error is encountered during script processing. = the agent continues the script and ignores the error.

## Syntax

```sql
sp_addscriptexec
[ @publication = ]
N
'publication'
, [ @scriptfile = ]
N
'scriptfile'
[ , [ @skiperror = ] skiperror ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
