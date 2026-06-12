---
name: "sys.sp_purge_jobhistory"
title: "sp_purge_jobhistory"
category: "general"
description: "Removes the history records for a job in the SQL Server Agent service."
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

Removes the history records for a job in the SQL Server Agent service.

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

`NULL`

### Example 2

`sp_purge_jobhistory`

### Example 3

```sql
0
```

### Example 4

```sql
1
```

### Example 5

`sp_purge_jobhistory`

### Example 6

`sp_purge_jobhistory`

### Example 7

`sp_purge_jobhistory`

### Example 8

`msdb`
