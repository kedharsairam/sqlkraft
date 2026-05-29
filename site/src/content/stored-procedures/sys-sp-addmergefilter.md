---
name: 'sys.sp_addmergefilter'
title: 'sp_addmergefilter'
category: 'general'
description: 'Adds a new merge filter to create a partition based on a join with another table. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication in which the merge filter is being added. The name of the article on which the merge filter is being added.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addmergefilter
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  , [ @filtername = ]
  N
  'filtername'
  , [ @join_articlename = ]
  N
  'join_articlename'
  , [ @join_filterclause = ]
  N
  'join_filterclause'
  [ , [ @join_unique_key = ] join_unique_key ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ , [ @filter_type = ] filter_type ]
  [ ; ]
---

## Description

Adds a new merge filter to create a partition based on a join with another table. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication in which the merge filter is being added. The name of the article on which the merge filter is being added.

## Syntax

```sql
sp_addmergefilter
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
, [ @filtername = ]
N
'filtername'
, [ @join_articlename = ]
N
'join_articlename'
, [ @join_filterclause = ]
N
'join_filterclause'
[ , [ @join_unique_key = ] join_unique_key ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @filter_type = ] filter_type ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Define an Article Define and Modify a Join Filter Between Merge Articles Join Filters sp_changemergefilter (Transact-SQL) sp_dropmergefilter (Transact-SQL) sp_helpmergefilter (Transact-SQL) Replication stored procedures (Transact-SQL) Related content

## Examples

### Example 1

```sql
sp_addmergefilter
```

### Example 2

```sql
DECLARE
@publication
AS
sysname;
DECLARE
@table1
AS
sysname;
DECLARE
@table2
AS
sysname;
DECLARE
@table3
AS
sysname;
DECLARE
@salesschema
AS
sysname;
DECLARE
@hrschema
AS
sysname;
DECLARE
@filterclause
AS
nvarchar
(1000);
SET
@publication = N
'AdvWorksSalesOrdersMerge'
;
SET
@table1 = N
'Employee'
;
SET
@table2 = N
'SalesOrderHeader'
;
SET
@table3 = N
'SalesOrderDetail'
;
SET
@salesschema = N
'Sales'
;
SET
@hrschema = N
'HumanResources'
;
SET
@filterclause = N
'Employee.LoginID = HOST_NAME()'
;
-- Add a filtered article for the Employee table.
EXEC sp_addmergearticle
@publication = @publication,
@article = @table1,
@source_object = @table1,
```
