---
name: "sys.sp_articlefilter"
title: "sp_articlefilter"
category: "general"
description: "Filters data that is published based on a table article. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_articlefilter
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @filter_name = ]
              N
              'filter_name'
              ]
              [ , [ @filter_clause = ]
              N
              'filter_clause'
              ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ ; ]
---

## Description

Filters data that is published based on a table article. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_articlefilter
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @filter_name = ]
N
'filter_name'
]
[ , [ @filter_clause = ]
N
'filter_clause'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Define an Article Define and Modify a Static Row Filter sp_addarticle (Transact-SQL) sp_articleview (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) Replication stored procedures (Transact-SQL)
## Examples

### Example 1

`sp_articlefilter`

### Example 2

`sp_articlefilter`

### Example 3

`filter`

### Example 4

`filter_clause`

### Example 5

`sp_articlefilter`

### Example 6

`type`

### Example 7

`sysarticles`

### Example 8

```sql
1
```

### Example 9

```sql
0
```

### Example 10

```sql
DECLARE
@publication
AS sysname;
DECLARE
@
table
AS sysname;
DECLARE
@filterclause
AS nvarchar (500);
DECLARE
@filtername
AS nvarchar (386);
DECLARE
@schemaowner
AS sysname;
SET
@publication = N
'AdvWorksProductTran'
;
SET
@
table
= N
'Product'
;
SET
@filterclause = N
'[DiscontinuedDate] IS NULL'
;
SET
@filtername = N
'filter_out_discontinued'
;
SET
@schemaowner = N
'Production'
;
-- Add a horizontally and vertically filtered article for the Product table.
-- Manually set @schema_option to ensure that the Production schema
-- is generated at the Subscriber (0x8000000).
EXEC sp_addarticle
@publication = @publication,
@article = @table,
@source_object = @table,
@source_owner = @schemaowner,
@schema_option = 0x80030F3,
@vertical_partition = N'true',
@type = N'logbased',
@filter_clause = @filterclause;
-- (Optional) Manually call the stored procedure to create the
-- horizontal filtering stored procedure. Since the type is
-- 'logbased', this stored procedures is executed automatically.
EXEC sp_articlefilter
```

_(. and 6 more examples)_
