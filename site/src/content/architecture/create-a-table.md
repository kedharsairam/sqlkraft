---
title: "Create a Table"
topic: "filestream"
description: "This topic shows how to create a table for storing FILESTREAM data. When the database has a FILESTREAM filegroup, you can create or modify tables to s"
tags: ["filestream","create-a-table"]
pubDate: 2025-12-01
---

This topic shows how to create a table for storing FILESTREAM data.

When the database has a FILESTREAM filegroup, you can create or modify tables to store

FILESTREAM data. To specify that a column contains FILESTREAM data, you create a

column and add the FILESTREAM attribute.

1. In SQL Server Management Studio, click

to display the Query Editor.

2. Copy the Transact-SQL code from the following example into the Query Editor. This

Transact-SQL code creates a FILESTREAM-enabled table called Records.

3. To create the table, click.

The following code example shows how to create a table that is named. The

column is a

column and is required to use FILESTREAM data with Win32 APIs. The

column is a. The

column is a

column and is

used to store the

in the file system.

７

Note

This example refers to the Archive database that is created in.

```sql
Records
Id
ROWGUIDCOL
SerialNumber
UNIQUE INTEGER
Chart
FILESTREAM
Chart
CREATE
TABLE
Archive.dbo.Records (
[
Id
] [uniqueidentifier] ROWGUIDCOL
NOT
NULL
UNIQUE
,
[SerialNumber]
INTEGER
UNIQUE
,
[Chart] VARBINARY(
MAX
) FILESTREAM
NULL
);
GO
```
