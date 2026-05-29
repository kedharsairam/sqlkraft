---
name: 'sys.sp_cdc_scan'
title: 'sys.sp_cdc_scan'
category: 'general'
description: 'Executes the change data capture log scan operation.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

(success) or

(failure).

None.

is called internally by

if the SQL Server Agent

capture job is being used by change data capture. The procedure can't be executed explicitly

when a change data capture log scan operation is already active, or when the database is

enabled for transactional replication. This stored procedure should be used by administrators

who want to customize the behavior of the capture job that is automatically configured.

Requires membership in the

fixed database role.

dbo.cdc_jobs (Transact-SQL)

Related content

```sql
0
```

```sql
1
```

```sql
sys.sp_cdc_scan
```

```sql
sys.sp_MScdc_capture_job
```
