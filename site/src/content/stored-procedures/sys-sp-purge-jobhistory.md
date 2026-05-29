---
name: 'sys.sp_purge_jobhistory'
title: 'sp_purge_jobhistory'
category: 'general'
description: 'Removes the history records for a job in the SQL Server Agent service. Transact-SQL syntax conventions The name of the job for which to delete the history records. must be specified, but both can''t be specified. fixed server role or members of the users don''t specify these arguments, the job history for all local and multiserver jobs is deleted within the time specified by users don''t specify thes'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_purge_jobhistory
  [ [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @job_id = ]
  'job_id'
  ]
  [ , [ @oldest_date = ] oldest_date ]
  [ ; ]
---

## Description

Removes the history records for a job in the SQL Server Agent service. Transact-SQL syntax conventions The name of the job for which to delete the history records. must be specified, but both can't be specified. fixed server role or members of the users don't specify these arguments, the job history for all local and multiserver jobs is deleted within the time specified by users don't specify these arguments, the job history for all local jobs is

## Syntax

```sql
sp_purge_jobhistory
[ [ @job_name = ]
N
'job_name'
]
[ , [ @job_id = ]
'job_id'
]
[ , [ @oldest_date = ] oldest_date ]
[ ; ]
```

## Examples

### Example 1

```sql
NULL
```

### Example 2

```sql
sp_purge_jobhistory
```

### Example 3

```sql
0
```

### Example 4

```sql
1
```

### Example 5

```sql
sp_purge_jobhistory
```

### Example 6

```sql
sp_purge_jobhistory
```

### Example 7

```sql
sp_purge_jobhistory
```

### Example 8

```sql
msdb
```
