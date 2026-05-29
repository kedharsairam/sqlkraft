---
title: "Access Data"
topic: "filestream"
description: |
  Article
  
  •
  
  01/22/2024
  
  Applies to:
  
  SQL Server
  
  This article describes how to use the Transact-SQL INSERT, UPDATE, and DELETE statements to
  
  manage FILESTREAM data.
  
  To add a row to a table that supp
tags:
  - "filestream"
  - "access-data"
pubDate: 2025-12-01
---

Article

•

01/22/2024

Applies to:

SQL Server

This article describes how to use the Transact-SQL INSERT, UPDATE, and DELETE statements to

manage FILESTREAM data.

To add a row to a table that supports FILESTREAM data, use the Transact-SQL INSERT

statement. When you insert data into a FILESTREAM column, you can insert NULL or a

value.

The following example shows how to insert

. When the FILESTREAM value is

, the

Database Engine doesn't create a file in the file system.

SQL

The following example shows how to use

to create a zero-length record. This is useful

for when you want to obtain a file handle, but will be manipulating the file by using Win32

APIs.

SQL

７

Note

The examples in this article require the FILESTREAM-enabled database and table that are

created in

and

.

```sql
NULL
NULL
INSERT
INSERT
INTO
Archive.dbo.Records
VALUES
(NEWID(), 1,
NULL
);
GO
INSERT
INTO
Archive.dbo.Records
VALUES
(NEWID(), 2,
```