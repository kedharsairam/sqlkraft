---
name: 'sys.sp_cdc_help_jobs'
title: 'sys.sp_cdc_help_jobs'
category: 'general'
description: 'Reports information about all change data capture cleanup or capture jobs in the current Transact-SQL syntax conventions The maximum number of transactions to process in each scan is valid only for capture jobs. The maximum number of scan cycles to execute in order to extract is valid only for capture jobs.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_cdc_help_jobs
  [ ; ]
---

## Description

Reports information about all change data capture cleanup or capture jobs in the current Transact-SQL syntax conventions The maximum number of transactions to process in each scan is valid only for capture jobs. The maximum number of scan cycles to execute in order to extract is valid only for capture jobs.

## Syntax

```sql
sys.sp_cdc_help_jobs
[ ; ]
```
