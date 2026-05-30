---
name: "sys.sp_mergearticlecolumn"
title: "sp_mergearticlecolumn"
category: "general"
description: "Partitions a merge publication vertically. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions The name of the article in the publication. Identifies the columns on which to create the vertical partition. , all columns in the source table are added columns from an article, execute for each column to be removed from the specified"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_mergearticlecolumn"
---

## Description

Partitions a merge publication vertically. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions The name of the article in the publication. Identifies the columns on which to create the vertical partition. , all columns in the source table are added columns from an article, execute for each column to be removed from the specified

## Syntax

`sp_mergearticlecolumn`

## Permissions

Only members of the fixed server role or fixed database role can execute . Define and Modify a Join Filter Between Merge Articles Define and Modify a Parameterized Row Filter for a Merge Article Filter Published Data Replication stored procedures (Transact-SQL) Related content

## Examples

### Example 1

`sp_mergearticlecolumn`

### Example 2

```sql
DECLARE
@publication
AS sysname;
DECLARE
@table1
AS sysname;
DECLARE
@table2
AS sysname;
DECLARE
@table3
AS sysname;
DECLARE
@salesschema
AS sysname;
DECLARE
@hrschema
AS sysname;
DECLARE
@filterclause
AS nvarchar (1000);
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
@type = N'table',
@source_owner = @hrschema,
@schema_option = 0x0004CF1,
@description = N'article for the Employee table',
@subset_filterclause = @filterclause;
-- Add an article for the SalesOrderHeader table that is filtered
-- based on Employee and horizontally filtered.
EXEC sp_addmergearticle
@publication = @publication,
@article = @table2,
@source_object = @table2,
```
