---
name: 'sys.sp_helpxactsetjob'
title: 'sp_helpxactsetjob'
category: 'general'
description: 'Displays information on the Xactset job for an Oracle Publisher. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the non-SQL Server Publisher to which the job belongs. Next date that the job will run. Flag indicating if the job is broken.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpxactsetjob [ @publisher = ]
  N
  'publisher'
  [ ; ]
---

## Description

Displays information on the Xactset job for an Oracle Publisher. This stored procedure is executed at the Distributor on any database. Transact-SQL syntax conventions The name of the non-SQL Server Publisher to which the job belongs. Next date that the job will run. Flag indicating if the job is broken.

## Syntax

```sql
sp_helpxactsetjob [ @publisher = ]
N
'publisher'
[ ; ]
```
