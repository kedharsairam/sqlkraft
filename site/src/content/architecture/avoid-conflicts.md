---
title: "Avoid Conflicts"
topic: "filestream"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  Applications that use SqlOpenFilestream() to open Win32 file handles for reading or writing
  
  FILESTREAM BLOB data can encounter conflict errors with Tr
tags:
  - "filestream"
  - "avoid-conflicts"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Applications that use SqlOpenFilestream() to open Win32 file handles for reading or writing

FILESTREAM BLOB data can encounter conflict errors with Transact-SQL statements that are

managed in a common transaction. This includes Transact-SQL or MARS queries that take a

long time to finish execution. Applications must be carefully designed to help avoid these types

of conflicts.

When SQL Server Database Engine or applications try to open FILESTREAM BLOBs, the

Database Engine checks the associated transaction context. The Database Engine allows or

denies the request based on whether the open operation is working with DDL statements, DML

statements, retrieving data, or managing transactions. The following table shows how the

Database Engine determines whether a Transact-SQL statement will be allowed or denied

based on the type of files that are open in the transaction.

DDL statements that work with database metadata, such as

CREATE TABLE, CREATE INDEX, DROP TABLE, and ALTER TABLE.

Allowed

Are blocked and fail

with a time-out.

DML statements that work with the data that is stored in the

database, such as UPDATE, DELETE, and INSERT.

Allowed

Denied

SELECT

Allowed

Allowed

COMMIT TRANSACTION

Denied*

Denied*.

SAVE TRANSACTION

Denied*

Denied*

ROLLBACK

Allowed*

Allowed*

* The transaction is canceled, and open handles for the transaction context are invalidated. The

application must close all open handles.

ﾉ

Expand table