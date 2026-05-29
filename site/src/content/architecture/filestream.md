---
title: "FILESTREAM"
topic: "filestream"
description: |
  09/03/2025
  
  Applies to:
  
  SQL Server
  
  - Windows only
  
  FILESTREAM enables SQL Server-based applications to store unstructured data, such as
  
  documents and images, on the file system. Applications can us
tags:
  - "filestream"
  - "filestream"
pubDate: 2025-12-01
---

09/03/2025

Applies to:

SQL Server

- Windows only

FILESTREAM enables SQL Server-based applications to store unstructured data, such as

documents and images, on the file system. Applications can use the rich streaming APIs and

performance of the file system and at the same time maintain transactional consistency

between the unstructured data and corresponding structured data.

FILESTREAM integrates the SQL Server Database Engine with an NTFS or ReFS file systems by

storing

binary large object (BLOB) data as files on the file system. Transact-SQL

statements can insert, update, query, search, and back up FILESTREAM data. Win32 file system

interfaces provide streaming access to the data.

FILESTREAM uses the NT system cache for caching file data. Caching files in the system cache

helps reduce any impact that FILESTREAM data might have on Database Engine performance.

The SQL Server buffer pool isn't used; therefore, this memory is available for query processing.

FILESTREAM isn't automatically enabled when you install or upgrade SQL Server. You must

enable FILESTREAM by using SQL Server Configuration Manager and SQL Server Management

Studio. To use FILESTREAM, you must create or modify a database to contain a special type of

filegroup. Then, create or modify a table so that it contains a

column with the

FILESTREAM attribute. After you complete these tasks, you can use Transact-SQL and Win32 to

manage the FILESTREAM data.

In SQL Server, BLOBs can be standard

data that stores the data in tables, or

FILESTREAM

objects that store the data in the file system. The size and use of

the data determines whether you should use database storage or file system storage. If the

following conditions are true, you should consider using FILESTREAM:

Objects that are being stored are, on average, larger than 1 MB.

Fast read access is important.

You're developing applications that use a middle tier for application logic.

For smaller objects, storing

BLOBs in the database often provides better

streaming performance.