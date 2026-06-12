---
name: "sys.sp_readerrorlog"
title: "sp_readerrorlog"
category: "general"
description: "Allows you to read the contents of the SQL Server or SQL Server Agent error log file and filter The integer value of the log you want to view. ), the one before previous is 2 ( The integer value for the product whose log you want to view. SQL Server Agent."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_readerrorlog
              [ [ @p1 = ] p1 ]
              [ , [ @p2 = ] p2 ]
              [ , [ @p3 = ]
              N
              'p3'
              ]
              [ , [ @p4 = ]
              N
              'p4'
              ]
              [ ; ]
---

## Description

Allows you to read the contents of the SQL Server or SQL Server Agent error log file and filter The integer value of the log you want to view. ), the one before previous is 2 ( The integer value for the product whose log you want to view. SQL Server Agent. If a value isn't specified, the SQL Server The string value for a string you want to filter on when viewing the error log.

## Syntax

```sql
sp_readerrorlog
[ [ @p1 = ] p1 ]
[ , [ @p2 = ] p2 ]
[ , [ @p3 = ]
N
'p3'
]
[ , [ @p4 = ]
N
'p4'
]
[ ; ]
```
