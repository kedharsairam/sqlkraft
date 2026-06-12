---
name: "sys.sp_table_validation"
title: "sp_table_validation"
category: "general"
description: "If the Distribution Agent is executing , specifies whether the Distribution Agent should shut down immediately upon completion of the validation. @shutdown_agent , with a default of , the replication agent doesn't shut down. If , error 20578 is raised and the replication agent is signaled to shut down. This parameter is ignored when is executed directly by a user. The table name of the view used f"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_table_validation [ @table = ]
  'table'
  [ , [ @expected_rowcount = ] type_of_check_requested
  OUTPUT
  ]
  [ , [ @expected_checksum = ] expected_checksum
  OUTPUT
  ]
  [ , [ @rowcount_only = ] rowcount_only ]
  [ , [ @owner = ]
  'owner'
  ]
  [ , [ @full_or_fast = ] full_or_fast ]
  [ , [ @shutdown_agent = ] shutdown_agent ]
  [ , [ @table_name = ]
  'table_name'
  ]
  [ , [ @column_list = ]
  'column_list'
  ]
  [ ; ]
---

## Description

If the Distribution Agent is executing , specifies whether the Distribution Agent should shut down immediately upon completion of the validation. @shutdown_agent , with a default of , the replication agent doesn't shut down. If , error 20578 is raised and the replication agent is signaled to shut down. This parameter is ignored when is executed directly by a user. The table name of the view used for output messages. , with a default of The list of columns that should be used in the checksum function. , with a default of. Enables validation of merge articles to specify a column list that excludes computed and timestamp columns. If performing a checksum validation and the expected checksum equals the checksum in the returns a message that the table passed checksum validation.

## Syntax

```sql
sp_table_validation [ @table = ]
'table'
[ , [ @expected_rowcount = ] type_of_check_requested
OUTPUT
]
[ , [ @expected_checksum = ] expected_checksum
OUTPUT
]
[ , [ @rowcount_only = ] rowcount_only ]
[ , [ @owner = ]
'owner'
]
[ , [ @full_or_fast = ] full_or_fast ]
[ , [ @shutdown_agent = ] shutdown_agent ]
[ , [ @table_name = ]
'table_name'
]
[ , [ @column_list = ]
'column_list'
]
[ ; ]
```

## Remarks

If the Distribution Agent is executing

, specifies whether the Distribution

Agent should shut down immediately upon completion of the validation.

@shutdown_agent

, with a default of

, the replication agent doesn't shut down. If

, error 20578 is raised

and the replication agent is signaled to shut down. This parameter is ignored when

is executed directly by a user.

The table name of the view used for output messages.

, with a default of

The list of columns that should be used in the checksum function.

column_list

, with a default of. Enables validation of merge articles to specify a column

list that excludes computed and timestamp columns.

If performing a checksum validation and the expected checksum equals the checksum in the

returns a message that the table passed checksum validation.

Otherwise, it returns a message that the table might be out of synchronization and reports the

difference between the expected and the actual number of rows.

If performing a rowcount validation and the expected number of rows equals the number in

returns a message that the table passed rowcount validation.

Otherwise, it returns a message that the table might be out of synchronization and reports the

difference between the expected and the actual number of rows.

is used in all types of replication.

isn't supported for

Oracle Publishers.

Checksum computes a 32-bit cyclic redundancy check (CRC) on the entire row image on the

page. It doesn't selectively check columns and can't operate on a view or vertical partition of

the table. Also, the checksum skips the contents of

columns (by design).
