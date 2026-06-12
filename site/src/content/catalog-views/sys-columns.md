---
name: "sys.columns"
title: "sys.columns"
category: "objects"
description: "Returns a row for each column of an object that has columns, such as views or tables. The following list contains the object types that have columns: Table-valued assembly functions (FT) Inline table-valued SQL functions (IF) Table-valued SQL functions (TF) ID of the object to which this column belongs."
tags: ["objects","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  sp_tableoption
      'text in row'
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a row for each column of an object that has columns, such as views or tables. The following list contains the object types that have columns: Table-valued assembly functions (FT) Inline table-valued SQL functions (IF) Table-valued SQL functions (TF) ID of the object to which this column belongs.

## Syntax

```sql
sp_tableoption
'text in row'
```

## Arguments

This function returns column or parameter information.

containing the identifier (ID) of the table or procedure.

An expression containing the name of the column or parameter.

argument, the

argument specifies the information type that the

function will return. The

argument can have any one of these values:

Description

Allows null values.

NULL: invalid input.

Column ID value corresponding to

When querying

multiple columns, gaps

may appear in the

sequence of Column

Expand table

Description

The TYPE COLUMN in the table holding the document

type information of the

ID of the full-text TYPE

COLUMN for the

column name

expression passed as

the second parameter

of this function.

Is column value system-generated. Corresponds to

: SQL Server

2016 (13.x) and later.

0: Not generated

1: Generated always at

2: Generated always at

Column is a column set. For more information, see

Column Sets

NULL: invalid input.

Column is a computed column.

NULL: invalid input.

Procedure parameter is of type CURSOR.

NULL: invalid input.

Column is deterministic. This property applies only to

computed columns and view columns.

NULL: invalid input.

Not a computed

column or view

Column is registered for full-text indexing.

Description

NULL: invalid input.

_(. and 20 more arguments)_

## Permissions
