---
name: "sys.sp_stop_job"
title: "sp_stop_job"
category: "general"
description: "Instructs SQL Server Agent to stop the execution of a job. Transact-SQL syntax conventions The identification number of the job to stop."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_stop_job
  [ [ @job_name = ]
  N
  'job_name'
  ]
  [ , [ @job_id = ]
  'job_id'
  ]
  [ , [ @originating_server = ]
  N
  'originating_server'
  ]
  [ , [ @server_name = ]
  N
  'server_name'
  ]
  [ ; ]
---

## Description

Instructs SQL Server Agent to stop the execution of a job. Transact-SQL syntax conventions The identification number of the job to stop. The name of the originating server. If specified, all multiserver jobs are stopped. . Specify this parameter only when Multi Server Administration (MSX/TSX) feature isn't supported on Azure SQL Managed

## Syntax

```sql
sp_stop_job
[ [ @job_name = ]
N
'job_name'
]
[ , [ @job_id = ]
'job_id'
]
[ , [ @originating_server = ]
N
'originating_server'
]
[ , [ @server_name = ]
N
'server_name'
]
[ ; ]
```

## Permissions

The name of the specific target server on which to stop a multiserver job. @server_name is , with a default of . Specify this parameter only when calling at an originating server for a multiserver job. (success) or (failure). None. sends a stop signal to the database. Some processes can be stopped immediately and some must reach a stable point (or an entry point to the code path) before they can stop. Some long-running Transact-SQL statements such as , , and some commands can take a long time to finish. When these commands are running, it might take a while before the job is canceled. Stopping a job causes a "Job Canceled" entry to be recorded in the job history. If a job is currently executing a step of type or , the process being run (for example, MyProgram.exe) is forced to end prematurely. Premature ending can result in unpredictable behavior such as files in use by the process being held open. Thus, should be used only in extreme circumstances if the job contains steps of type or . This stored procedure shares the name of with a similar object for the Azure Elastic Jobs service for Azure SQL Database . For information about the elastic jobs version, see jobs.sp_stop_job (Azure Elastic Jobs) . ７ Note Only one of the first three parameters can be specified.
