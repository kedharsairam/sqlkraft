---
name: "sys.sp_repladdcolumn"
title: "sp_repladdcolumn"
category: "general"
description: "Adds a column to an existing published table article. Allows the new column to be added to all publishers that publish this table, or just add the column to a specific publication that publishes the table. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the table article that contains the new column to add. This stored procedure is "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_repladdcolumn
  [ @source_object = ]
  N
  'source_object'
  , [ @column = ]
  N
  'column'
  , [ @typetext = ]
  N
  'typetext'
  [ , [ @publication_to_add = ]
  N
  'publication_to_add'
  ]
  [ , [ @from_agent = ] from_agent ]
  [ , [ @schema_change_script = ]
  N
  'schema_change_script'
  ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ ; ]
---

## Description

Adds a column to an existing published table article. Allows the new column to be added to all publishers that publish this table, or just add the column to a specific publication that publishes the table. This stored procedure is executed at the Publisher on the publication Transact-SQL syntax conventions The name of the table article that contains the new column to add. This stored procedure is deprecated, and is being supported for backward compatibility. It

## Syntax

```sql
sp_repladdcolumn
[ @source_object = ]
N
'source_object'
, [ @column = ]
N
'column'
, [ @typetext = ]
N
'typetext'
[ , [ @publication_to_add = ]
N
'publication_to_add'
]
[ , [ @from_agent = ] from_agent ]
[ , [ @schema_change_script = ]
N
'schema_change_script'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```
