---
title: "Column Collation"
topic: "collation"
description: "You can override the database collation for , , , , , and data by specifying a differe"
tags: ["collation","column-collation"]
pubDate: 2025-12-01
---

You can override the database collation for

,

,

,

,

, and

data

by specifying a different collation for a specific column of a table and using one of the

following:

The COLLATE clause of

CREATE TABLE

and

ALTER TABLE

, as seen in the examples below.

Consider one of the existing tables defined below:

To convert the column in-place to use UTF-8, run an

statement that sets

the required data type and a UTF-8 enabled collation:

This method is easy to implement, however it's a possibly blocking operation which

may become an issue for large tables and busy applications.

Consider one of the existing tables defined below:

```sql
ALTER COLUMN
-- NVARCHAR column is encoded in UTF-16 because a supplementary character enabled collation is used
CREATE
TABLE dbo.MyTable (CharCol
NVARCHAR (50)
COLLATE
Latin1_General_100_CI_AI_SC);
-- VARCHAR column is encoded the Latin code page and therefore is not Unicode capable
CREATE
TABLE dbo.MyTable (CharCol
VARCHAR (50)
COLLATE
Latin1_General_100_CI_AI);
ALTER
TABLE dbo.MyTable
ALTER
COLUMN
CharCol
VARCHAR (50)
COLLATE
Latin1_General_100_CI_AI_SC_UTF8
-- NVARCHAR column is encoded in UTF-16 because a supplementary character enabled collation is used
CREATE
TABLE dbo.MyTable (CharCol
NVARCHAR (50)
COLLATE
Latin1_General_100_CI_AI_SC);
GO
-- VARCHAR column is encoded using the Latin code page and therefore is not
Unicode capable
```
