---
name: 'sys.sp_cdc_help_jobs'
title: 'sys.sp_cdc_help_jobs'
category: 'general'
description: 'Reports information about all change data capture cleanup or capture jobs in the current'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description
A flag indicating whether the capture job is to run continuously (

),

or run in one-time mode (

). For more information, see

sys.sp_cdc_add_job

.

is valid only for capture jobs.

The number of seconds between log scan cycles.

is valid only for capture jobs.

The number of minutes that change rows are to be retained in

change tables.

is valid only for cleanup jobs.

The maximum number of delete entries that can be deleted using a

single statement on cleanup.

Requires membership in the

fixed database role.

The following example returns information about the defined capture and cleanup jobs for the

database.

SQL

dbo.cdc_jobs (Transact-SQL)

sys.sp_cdc_add_job (Transact-SQL)

Related content

```sql
continuous
```

```sql
1
```

```sql
0
```

```sql
continuous
```

```sql
pollinginterval
```

```sql
pollinginterval
```

```sql
retention
```

```sql
retention
```

```sql
threshold
```

```sql
AdventureWorks2022
```

```sql
USE
AdventureWorks2022;
GO
EXECUTE
sys.sp_cdc_help_jobs;
GO
```
