---
name: 'sys.sp_cdc_change_job'
title: 'sys.sp_cdc_change_job'
category: 'general'
description: 'Modifies the configuration of a change data capture cleanup or capture job in the current'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## A. Change a capture job

Maximum number of delete entries that can be deleted using a single statement on cleanup.

@threshold

is

, with a default of

, which indicates no change for this parameter.

@threshold

is valid only for cleanup jobs.

(success) or

(failure).

None.

If a parameter is omitted, the associated value in the

dbo.cdc_jobs

table isn't updated. A

parameter set explicitly to

is treated as though the parameter is omitted.

Specifying a parameter that is invalid for the job type causes the statement to fail.

Changes to a job don't take effect until the job is stopped by using

sys.sp_cdc_stop_job

and

restarted by using

sys.sp_cdc_start_job

.

Requires membership in the

fixed database role.

The following example updates the

@job_type

,

@maxscans

, and

@maxtrans

parameters of a

capture job in the

database. The other valid parameters for a capture job,

@continuous

and

@pollinginterval

, are omitted; their values aren't modified.

SQL

## B. Change a cleanup job

The following example updates a cleanup job in the

database. All valid

parameters for this job type, except

@threshold

, are specified. The value of

@threshold

isn't

modified.

SQL

dbo.cdc_jobs (Transact-SQL)

sys.sp_cdc_enable_table (Transact-SQL)

sys.sp_cdc_add_job (Transact-SQL)

Related content

```sql
NULL
```

```sql
0
```

```sql
1
```

```sql
NULL
```

```sql
AdventureWorks2022
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_change_job
@job_type = N
'capture'
,
```

```sql
AdventureWorks2022
```

```sql
@maxscans = 1000,
@
maxtrans
= 15;
GO
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_change_job
@job_type = N
'cleanup'
,
@
retention
= 2880;
GO
```
