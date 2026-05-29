---
title: sys.dm_external_script_requests
name: sys.dm_external_script_requests
category: execution
description:
pubDate: 2026-05-29
---

Registration of these functions is performed when the feature is installed, and registered

functions can't be added or deleted.

The following example displays the cumulative number of external script executions for the R

language.

SQL

The following example displays the cumulative number of external script executions for the

Python language.

SQL

System Dynamic Management Views

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_external_script_requests

sp_execute_external_script (Transact-SQL)

## Applies to:

## Note

## Machine

## Learning Services (R, Python) in SQL Server 2017 and later

## R Services in SQL Server

## 2016

## Machine Learning Services in Azure SQL Managed Instance

## Note

```sql
SELECT
counter_name, counter_value
FROM
sys.dm_external_script_execution_stats
WHERE
language
=
'R'
;
```

```sql
SELECT
counter_name, counter_value
FROM
sys.dm_external_script_execution_stats
WHERE
language
=
'Python'
;
```
