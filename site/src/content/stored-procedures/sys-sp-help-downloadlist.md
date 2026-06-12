---
name: "sys.sp_help_downloadlist"
title: "sp_help_downloadlist"
category: "general"
description: "system table for the supplied job, or all rows if no job is The job identification number for which to return information. must be specified, but both can't be specified. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_help_downloadlist
      [ [ @job_id = ]
      'job_id'
      ]
      [ , [ @job_name = ]
      N
      'job_name'
      ]
      [ , [ @operation = ]
      'operation'
      ]
      [ , [ @object_type = ]
      'object_type'
      ]
      [ , [ @object_name = ]
      N
      'object_name'
      ]
      [ , [ @target_server = ]
      N
      'target_server'
      ]
      [ , [ @has_error = ] has_error ]
      [ , [ @status = ] status ]
      [ , [ @date_posted = ] date_posted ]
      [ ; ]
---

## Description

system table for the supplied job, or all rows if no job is The job identification number for which to return information. must be specified, but both can't be specified. must be specified, but both can't be specified.

## Syntax

```sql
sp_help_downloadlist
[ [ @job_id = ]
'job_id'
]
[ , [ @job_name = ]
N
'job_name'
]
[ , [ @operation = ]
'operation'
]
[ , [ @object_type = ]
'object_type'
]
[ , [ @object_name = ]
N
'object_name'
]
[ , [ @target_server = ]
N
'target_server'
]
[ , [ @has_error = ] has_error ]
[ , [ @status = ] status ]
[ , [ @date_posted = ] date_posted ]
[ ; ]
```
