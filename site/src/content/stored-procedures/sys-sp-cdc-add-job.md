---
name: 'sys.sp_cdc_add_job'
title: 'sys.sp_cdc_add_job'
category: 'general'
description: 'Creates a change data capture cleanup or capture job in the current database.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## A. Create a capture job

(success) or

(failure).

None.

A cleanup job is created using the default values when the first table in the database is enabled

for change data capture. A capture job is created using the default values when the first table

in the database is enabled for change data capture and no transactional publications exist for

the database. When a transactional publication exists, the transactional log reader is used to

drive the capture mechanism, and a separate capture job isn't required or allowed.

Because the cleanup and capture jobs are created by default, this stored procedure is

necessary only when a job has been explicitly dropped and must be recreated.

The name of the job is

or

, where

is the name of the current database. If a job with the same name already

exists, the name is appended with a period (

) followed by a unique identifier, for example:

.

To view the current configuration of a cleanup or capture job, use

sys.sp_cdc_help_jobs

. To

change the configuration of a job, use

sys.sp_cdc_change_job

.

Requires membership in the

fixed database role.

The following example creates a capture job. This example assumes that the existing cleanup

job was explicitly dropped and must be recreated. The job is created using the default values.

SQL

## B. Create a cleanup job

The following example creates a cleanup job in the AdventureWorks2022 database. The

parameter

@start_job

is set to

and

@retention

is set to 5760 minutes (96 hours). This

example assumes that the existing cleanup job was explicitly dropped and must be recreated.

SQL

dbo.cdc_jobs (Transact-SQL)

sys.sp_cdc_enable_table (Transact-SQL)

What is change data capture (CDC)?

Related content

```sql
0
```

```sql
1
```

```sql
cdc.<database_name>_cleanup
```

```sql
cdc.<database_name>_capture
```

```sql
<database_name>
```

```sql
.
```

```sql
cdc.AdventureWorks_capture.A1ACBDED-13FC-428C-8302-10100EF74F52
```

```sql
0
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_add_job @job_type = N
'capture'
;
GO
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_add_job
@job_type = N
'cleanup'
,
@start_job = 0,
@
retention
= 5760;
```
