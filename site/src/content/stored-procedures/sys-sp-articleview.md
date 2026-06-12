---
name: "sys.sp_articleview"
title: "sp_articleview"
category: "general"
description: "Creates the view that defines the published article when a table is filtered vertically or horizontally. This view is used as the filtered source of the schema and data for the destination tables. Only unsubscribed articles can be modified by this stored procedure. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_articleview
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @view_name = ]
              N
              'view_name'
              ]
              [ , [ @filter_clause = ]
              N
              'filter_clause'
              ]
              [ , [ @change_active = ] change_active ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ , [ @refreshsynctranprocs = ] refreshsynctranprocs ]
              [ , [ @internal = ] internal ]
              [ ; ]
---

## Description

Creates the view that defines the published article when a table is filtered vertically or horizontally. This view is used as the filtered source of the schema and data for the destination tables. Only unsubscribed articles can be modified by this stored procedure. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_articleview
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @view_name = ]
N
'view_name'
]
[ , [ @filter_clause = ]
N
'filter_clause'
]
[ , [ @change_active = ] change_active ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @refreshsynctranprocs = ] refreshsynctranprocs ]
[ , [ @internal = ] internal ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. Define an Article Define and Modify a Static Row Filter sp_addarticle (Transact-SQL) sp_articlefilter (Transact-SQL) sp_changearticle (Transact-SQL) sp_droparticle (Transact-SQL) sp_helparticle (Transact-SQL) Replication stored procedures (Transact-SQL)
## Examples

### Example 1

`sp_articleview`

### Example 2

`sp_articleview`

### Example 3

`type`

### Example 4

```sql
5
```

### Example 5

`sp_articleview`

### Example 6

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
@publication = @publication,
@article = @table,
@filter_clause = @filterclause,
@filter_name = @filtername;
-- Add all columns to the article.
EXEC sp_articlecolumn
@publication = @publication,
```
