---
name: 'sys.sp_cdc_drop_job'
title: 'sys.sp_cdc_drop_job'
category: 'general'
description: 'Removes a change data capture cleanup or capture job for the current database from'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

The following example removes the cleanup job for the

database.

SQL

dbo.cdc_jobs (Transact-SQL)

sys.sp_cdc_disable_db (Transact-SQL)

sys.sp_cdc_add_job (Transact-SQL)

Related content

```sql
AdventureWorks2022
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_drop_job @job_type = N
'cleanup'
;
```
