---
name: "sys.sp_scriptdynamicupdproc"
title: "sp_scriptdynamicupdproc"
category: "general"
description: "statement that creates a dynamic update stored procedure. statement within the custom stored procedure is built dynamically based on the syntax that indicates which columns to change. Use this stored procedure if the number of indexes on the subscribing table is growing and the number of columns being changed is small. This stored procedure is run at the Publisher on the publication database. Tran"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: "sp_scriptdynamicupdproc"
---

## Description

statement that creates a dynamic update stored procedure. statement within the custom stored procedure is built dynamically based on the syntax that indicates which columns to change. Use this stored procedure if the number of indexes on the subscribing table is growing and the number of columns being changed is small. This stored procedure is run at the Publisher on the publication database. The article ID. , with no default. Returns a result set that consists of a single column. The result set forms the statement used to create the custom stored procedure. is used in transactional replication. The default scripting logic includes all columns within the statement and uses a bitmap to determine the columns that have changed. If a column didn't change, the column is set back to itself, which usually

## Syntax

`sp_scriptdynamicupdproc`

## Remarks

Generates the

statement that creates a dynamic update stored procedure.

statement within the custom stored procedure is built dynamically based on the

syntax that indicates which columns to change. Use this stored procedure if the number

of indexes on the subscribing table is growing and the number of columns being changed is

small. This stored procedure is run at the Publisher on the publication database.

The article ID.

, with no default.

Returns a result set that consists of a single

column. The result set forms the

statement used to create the custom stored procedure.

is used in transactional replication. The default

scripting logic

includes all columns within the

statement and uses a bitmap to determine the columns

that have changed. If a column didn't change, the column is set back to itself, which usually

causes no problems. If the column is indexed, extra processing occurs. The dynamic approach

includes only the columns that have changed, which provides an optimal

## Examples

### Example 1

`UPDATE`

### Example 2

`sp_scriptdynamicupdproc`

### Example 3

```sql
1
```

### Example 4

`authors`

### Example 5

`pubs`

### Example 6

`UPDATE`

### Example 7

```sql
'MCALL sp_mupd_authors'
```

### Example 8

```sql
EXECUTE sp_scriptdynamicupdproc @artid =
'1'
;
CREATE
PROCEDURE
[sp_mupd_authors] (@c1
VARCHAR (11),
@c2
VARCHAR (40),
@c3
VARCHAR (20),
@c4
CHAR (12),
@c5
VARCHAR (40),
@c6
VARCHAR (20),
@c7
CHAR (2),
@c8
CHAR (5),
@c9
BIT
,
@pkc1
VARCHAR (11),
@
bitmap
BINARY (2))
AS
DECLARE
@stmt
AS
NVARCHAR (4000), @spacer
AS
NVARCHAR (1);
SELECT
@spacer = N
''
;
SELECT
@stmt = N
'UPDATE [authors] SET '
;
IF SUBSTRING(@bitmap, 1, 1) & 2 = 2
BEGIN
SELECT
@stmt = @stmt + @spacer + N
'[au_lname]'
+ N
'=@2'
;
SELECT
@spacer = N
','
;
```
